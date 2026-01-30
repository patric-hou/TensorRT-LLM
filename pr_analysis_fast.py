#!/usr/bin/env python3
"""
Optimized PR Analysis Script for TensorRT-LLM repository.
Fetches merged PRs from GitHub API and analyzes blockers with minimal API calls.
"""

import json
import os
import random
import time
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import requests

# GitHub API configuration
GITHUB_API = "https://api.github.com"
REPO_OWNER = "NVIDIA"
REPO_NAME = "TensorRT-LLM"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Rate limiting - more aggressive without token
REQUEST_DELAY = 1.0 if not GITHUB_TOKEN else 0.1

def get_headers():
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


def api_request(url: str, params: Dict = None, retries: int = 3) -> Optional[Any]:
    """Make API request with retry logic."""
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=get_headers(), params=params, timeout=30)

            if response.status_code == 200:
                time.sleep(REQUEST_DELAY)
                return response.json()
            elif response.status_code == 403:
                reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
                remaining = response.headers.get('X-RateLimit-Remaining', '?')
                print(f"Rate limited (remaining: {remaining}). Waiting...")
                wait_time = max(reset_time - time.time(), 60)
                time.sleep(min(wait_time, 120))
            elif response.status_code == 404:
                return None
            else:
                print(f"Error {response.status_code}: {url}")
                time.sleep(2 ** attempt)
        except Exception as e:
            print(f"Request error: {e}")
            time.sleep(2 ** attempt)

    return None


def get_merged_prs_count() -> int:
    """Get approximate count of merged PRs using search API."""
    url = f"{GITHUB_API}/search/issues"
    params = {
        "q": f"repo:{REPO_OWNER}/{REPO_NAME} is:pr is:merged",
        "per_page": 1
    }
    result = api_request(url, params)
    if result:
        return result.get("total_count", 0)
    return 0


def get_merged_prs_basic(per_page: int = 100, max_pages: int = 30) -> List[Dict]:
    """Get list of merged PRs with basic info."""
    all_prs = []

    for page in range(1, max_pages + 1):
        url = f"{GITHUB_API}/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
        params = {
            "state": "closed",
            "sort": "updated",
            "direction": "desc",
            "per_page": per_page,
            "page": page
        }

        print(f"Fetching PR list page {page}...")
        prs = api_request(url, params)

        if not prs:
            break

        # Filter for merged PRs only
        merged_prs = [pr for pr in prs if pr.get("merged_at")]
        all_prs.extend(merged_prs)

        print(f"  Found {len(merged_prs)} merged PRs (total: {len(all_prs)})")

        if len(prs) < per_page or len(all_prs) >= 2000:
            break

    return all_prs


def get_pr_reviews(pr_number: int) -> List[Dict]:
    """Get reviews for a PR."""
    url = f"{GITHUB_API}/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pr_number}/reviews"
    result = api_request(url, {"per_page": 100})
    return result if result else []


def get_pr_timeline(pr_number: int) -> List[Dict]:
    """Get timeline events for a PR - includes reviews, commits, comments."""
    url = f"{GITHUB_API}/repos/{REPO_OWNER}/{REPO_NAME}/issues/{pr_number}/timeline"
    headers = get_headers()
    headers["Accept"] = "application/vnd.github.mockingbird-preview+json"

    try:
        response = requests.get(url, headers=headers, params={"per_page": 100}, timeout=30)
        if response.status_code == 200:
            time.sleep(REQUEST_DELAY)
            return response.json()
    except:
        pass
    return []


def analyze_pr_fast(pr_data: Dict, get_reviews: bool = True) -> Dict[str, Any]:
    """
    Fast analysis of a single PR with minimal API calls.
    """
    pr_number = pr_data["number"]

    # Basic PR info (already in pr_data)
    result = {
        "pr_number": pr_number,
        "pr_url": pr_data["html_url"],
        "title": pr_data["title"],
        "author": pr_data["user"]["login"],
        "created_at": pr_data["created_at"],
        "merged_at": pr_data["merged_at"],
        "merge_duration_hours": 0,
        "commit_count": pr_data.get("commits", 1),  # Often available in list response
        "additions": pr_data.get("additions", 0),
        "deletions": pr_data.get("deletions", 0),
        "changed_files": pr_data.get("changed_files", 0),
        "blockers": [],
        "blocker_summary": defaultdict(int),
    }

    # Calculate merge duration
    try:
        created = datetime.fromisoformat(pr_data["created_at"].replace("Z", "+00:00"))
        merged = datetime.fromisoformat(pr_data["merged_at"].replace("Z", "+00:00"))
        result["merge_duration_hours"] = (merged - created).total_seconds() / 3600
    except:
        pass

    # Analyze title for potential issues
    title = pr_data.get("title", "")
    if not title.startswith("["):
        result["blockers"].append({"type": "possible_title_format_issue"})
        result["blocker_summary"]["possible_title_format_issue"] = 1

    # Get reviews (1 API call per PR)
    if get_reviews:
        reviews = get_pr_reviews(pr_number)
        changes_requested_count = 0
        for review in reviews:
            state = review.get("state", "").upper()
            if state == "CHANGES_REQUESTED":
                changes_requested_count += 1
                result["blockers"].append({
                    "type": "changes_requested",
                    "reviewer": review.get("user", {}).get("login", "unknown"),
                    "time": review.get("submitted_at", ""),
                })

        if changes_requested_count > 0:
            result["blocker_summary"]["changes_requested"] = changes_requested_count

    return result


def sample_prs(all_prs: List[Dict], target_count: int) -> List[Dict]:
    """Sample PRs randomly if we have more than target_count."""
    if len(all_prs) <= target_count:
        return all_prs
    return random.sample(all_prs, target_count)


def format_duration(hours: float) -> str:
    """Format duration in human-readable format."""
    if hours < 1:
        return f"{hours * 60:.0f}m"
    elif hours < 24:
        return f"{hours:.1f}h"
    else:
        days = hours / 24
        return f"{days:.1f}d"


def generate_report(analyzed_prs: List[Dict], total_merged: int) -> str:
    """Generate markdown report from analyzed PRs."""

    # Calculate statistics
    durations = [pr["merge_duration_hours"] for pr in analyzed_prs if pr["merge_duration_hours"] > 0]
    commit_counts = [pr["commit_count"] for pr in analyzed_prs if pr["commit_count"] > 0]

    avg_duration = sum(durations) / len(durations) if durations else 0
    sorted_durations = sorted(durations)
    median_duration = sorted_durations[len(sorted_durations) // 2] if sorted_durations else 0
    min_duration = min(durations) if durations else 0
    max_duration = max(durations) if durations else 0

    avg_commits = sum(commit_counts) / len(commit_counts) if commit_counts else 0
    median_commits = sorted(commit_counts)[len(commit_counts) // 2] if commit_counts else 0

    # Percentiles
    p25_duration = sorted_durations[int(len(sorted_durations) * 0.25)] if sorted_durations else 0
    p75_duration = sorted_durations[int(len(sorted_durations) * 0.75)] if sorted_durations else 0
    p90_duration = sorted_durations[int(len(sorted_durations) * 0.90)] if sorted_durations else 0

    # Sort by duration for top/bottom 10
    prs_by_duration = sorted(analyzed_prs, key=lambda x: x["merge_duration_hours"], reverse=True)
    longest_10 = prs_by_duration[:10]
    shortest_10 = [pr for pr in prs_by_duration[-10:] if pr["merge_duration_hours"] > 0]

    # Aggregate blocker statistics
    all_blockers = defaultdict(int)
    prs_with_blockers = 0
    for pr in analyzed_prs:
        if pr["blocker_summary"]:
            prs_with_blockers += 1
        for blocker_type, count in pr["blocker_summary"].items():
            all_blockers[blocker_type] += count

    # Duration distribution
    duration_buckets = {
        "< 1 hour": 0,
        "1-6 hours": 0,
        "6-24 hours": 0,
        "1-3 days": 0,
        "3-7 days": 0,
        "1-2 weeks": 0,
        "> 2 weeks": 0,
    }
    for d in durations:
        if d < 1:
            duration_buckets["< 1 hour"] += 1
        elif d < 6:
            duration_buckets["1-6 hours"] += 1
        elif d < 24:
            duration_buckets["6-24 hours"] += 1
        elif d < 72:
            duration_buckets["1-3 days"] += 1
        elif d < 168:
            duration_buckets["3-7 days"] += 1
        elif d < 336:
            duration_buckets["1-2 weeks"] += 1
        else:
            duration_buckets["> 2 weeks"] += 1

    # Build report
    report = []
    report.append("# TensorRT-LLM PR Analysis Report")
    report.append("")
    report.append(f"**Generated**: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    report.append("")
    report.append(f"**Repository**: [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)")
    report.append("")

    # Executive Summary
    report.append("## Executive Summary")
    report.append("")
    report.append(f"| Metric | Value |")
    report.append(f"|--------|-------|")
    report.append(f"| Total Merged PRs in Repository | {total_merged:,} |")
    report.append(f"| PRs Analyzed in This Report | {len(analyzed_prs):,} |")
    report.append(f"| PRs with Review Change Requests | {prs_with_blockers} ({prs_with_blockers/len(analyzed_prs)*100:.1f}%) |")
    report.append(f"| Average Merge Duration | {format_duration(avg_duration)} |")
    report.append(f"| Median Merge Duration | {format_duration(median_duration)} |")
    report.append(f"| Average Commits per PR | {avg_commits:.1f} |")
    report.append("")

    # Merge Duration Statistics
    report.append("## Merge Duration Statistics")
    report.append("")
    report.append("| Statistic | Duration |")
    report.append("|-----------|----------|")
    report.append(f"| Minimum | {format_duration(min_duration)} |")
    report.append(f"| 25th Percentile | {format_duration(p25_duration)} |")
    report.append(f"| Median (50th) | {format_duration(median_duration)} |")
    report.append(f"| Average | {format_duration(avg_duration)} |")
    report.append(f"| 75th Percentile | {format_duration(p75_duration)} |")
    report.append(f"| 90th Percentile | {format_duration(p90_duration)} |")
    report.append(f"| Maximum | {format_duration(max_duration)} |")
    report.append("")

    # Duration distribution
    report.append("### Merge Duration Distribution")
    report.append("")
    report.append("| Time Range | Count | Percentage |")
    report.append("|------------|-------|------------|")
    for bucket, count in duration_buckets.items():
        pct = count / len(durations) * 100 if durations else 0
        bar = "█" * int(pct / 5)  # Simple visual bar
        report.append(f"| {bucket} | {count} | {pct:.1f}% {bar} |")
    report.append("")

    # Blocker distribution
    report.append("## Blocker Type Distribution")
    report.append("")
    report.append("| Blocker Type | Count | Description |")
    report.append("|-------------|-------|-------------|")

    blocker_descriptions = {
        "changes_requested": "Reviewer requested code changes",
        "ci_failure": "CI pipeline failure (from comments)",
        "ci_check_failure": "CI check failure (GitHub Actions)",
        "precommit_failure": "Pre-commit hook failure",
        "title_format_error": "PR title format validation error",
        "possible_title_format_issue": "PR title may not follow required format",
    }

    if all_blockers:
        for blocker_type, count in sorted(all_blockers.items(), key=lambda x: x[1], reverse=True):
            desc = blocker_descriptions.get(blocker_type, blocker_type)
            report.append(f"| {blocker_type} | {count} | {desc} |")
    else:
        report.append("| (none detected) | 0 | - |")
    report.append("")

    # CI/CD Configuration Analysis
    report.append("## CI/CD Configuration Analysis")
    report.append("")
    report.append("Based on the repository's GitHub Actions workflows (`.github/workflows/`), the following checks can cause PR blockers:")
    report.append("")

    report.append("### 1. PR Title Format Check")
    report.append("**File**: `.github/workflows/pr-check.yml`")
    report.append("")
    report.append("- **Trigger**: PR opened, edited, synchronize, reopened")
    report.append("- **Requirement**: PR title must match pattern:")
    report.append("  ```")
    report.append("  [Ticket][type] Summary")
    report.append("  ```")
    report.append("- **Valid ticket formats**:")
    report.append("  - JIRA ticket: `[TRTLLM-1234]`")
    report.append("  - NVBugs ID: `[https://nvbugs/1234567]`")
    report.append("  - GitHub issue: `[#1234]`")
    report.append("  - No ticket: `[None]`")
    report.append("- **Valid types**: `[fix]`, `[feat]`, `[doc]`, `[infra]`, `[chore]`, etc.")
    report.append("")

    report.append("### 2. PR Checklist Check")
    report.append("**Files**: `.github/workflows/pr-check.yml`, `.github/scripts/pr_checklist_check.py`")
    report.append("")
    report.append("- **Trigger**: PR opened, edited, synchronize, reopened")
    report.append("- **Requirement**: All checklist items in PR body must be resolved (checked)")
    report.append("- **Common issues**: Forgetting to check the final confirmation checkbox")
    report.append("")

    report.append("### 3. Pre-commit Check (Release Checks)")
    report.append("**Files**: `.github/workflows/precommit-check.yml`, `scripts/release_check.py`, `.pre-commit-config.yaml`")
    report.append("")
    report.append("- **Trigger**: Every PR")
    report.append("- **Checks performed**:")
    report.append("  - Code formatting (isort, yapf, autoflake, ruff)")
    report.append("  - Bandit security scan (no `#nosec` annotations allowed)")
    report.append("  - License header validation")
    report.append("  - YAML/JSON validation")
    report.append("  - Trailing whitespace and end-of-file fixes")
    report.append("")

    report.append("### 4. Blossom CI (Jenkins Integration)")
    report.append("**File**: `.github/workflows/blossom-ci.yml`")
    report.append("")
    report.append("- **Trigger**: `/bot run` comment from authorized users")
    report.append("- **Authorization**: ~350 authorized NVIDIA team members")
    report.append("- **Checks performed**:")
    report.append("  - Vulnerability scan")
    report.append("  - Jenkins CI job (comprehensive build and test suite)")
    report.append("- **Note**: External contributors must wait for authorized user to trigger CI")
    report.append("")

    report.append("### 5. L0 Test Results Upload")
    report.append("**File**: `.github/workflows/l0-test.yml`")
    report.append("")
    report.append("- **Trigger**: Workflow dispatch after CI completion")
    report.append("- **Function**: Updates commit status with test pass/fail counts")
    report.append("")

    # Top 10 longest
    report.append("## Top 10 Longest Merge Duration PRs")
    report.append("")
    report.append("| PR | Title | Duration | Commits | Blockers |")
    report.append("|----|-------|----------|---------|----------|")
    for pr in longest_10:
        pr_link = f"[#{pr['pr_number']}]({pr['pr_url']})"
        title = pr['title'][:50] + "..." if len(pr['title']) > 50 else pr['title']
        title = title.replace("|", "\\|")
        duration = format_duration(pr["merge_duration_hours"])
        blockers_str = ", ".join([f"{k}:{v}" for k, v in pr["blocker_summary"].items()]) or "None"
        report.append(f"| {pr_link} | {title} | {duration} | {pr['commit_count']} | {blockers_str} |")
    report.append("")

    # Top 10 shortest
    report.append("## Top 10 Shortest Merge Duration PRs")
    report.append("")
    report.append("| PR | Title | Duration | Commits | Blockers |")
    report.append("|----|-------|----------|---------|----------|")
    for pr in shortest_10:
        pr_link = f"[#{pr['pr_number']}]({pr['pr_url']})"
        title = pr['title'][:50] + "..." if len(pr['title']) > 50 else pr['title']
        title = title.replace("|", "\\|")
        duration = format_duration(pr["merge_duration_hours"])
        blockers_str = ", ".join([f"{k}:{v}" for k, v in pr["blocker_summary"].items()]) or "None"
        report.append(f"| {pr_link} | {title} | {duration} | {pr['commit_count']} | {blockers_str} |")
    report.append("")

    # All PRs table
    report.append("## All Analyzed PRs")
    report.append("")
    report.append("| PR ID & Link | Blockers (Type: Count) | Commits | Merge Duration |")
    report.append("|--------------|------------------------|---------|----------------|")

    for pr in sorted(analyzed_prs, key=lambda x: x["pr_number"], reverse=True):
        pr_link = f"[#{pr['pr_number']}]({pr['pr_url']})"
        blockers_str = ", ".join([f"{k}: {v}" for k, v in pr["blocker_summary"].items()]) or "None"
        duration = format_duration(pr["merge_duration_hours"])
        report.append(f"| {pr_link} | {blockers_str} | {pr['commit_count']} | {duration} |")

    report.append("")
    report.append("---")
    report.append("")
    report.append("*This report was automatically generated by analyzing GitHub PR data.*")

    return "\n".join(report)


def main():
    print("=" * 60)
    print("TensorRT-LLM PR Analysis (Fast Mode)")
    print("=" * 60)

    # Step 1: Get merged PR count
    print("\n[1/4] Getting merged PR count...")
    total_merged = get_merged_prs_count()
    print(f"Total merged PRs: {total_merged}")

    # Step 2: Fetch PR list
    print("\n[2/4] Fetching PR list...")
    all_prs = get_merged_prs_basic(per_page=100, max_pages=15)
    print(f"Fetched {len(all_prs)} merged PRs")

    # Target: analyze up to 500 PRs (for faster results)
    target_count = min(500, len(all_prs))
    sampled_prs = sample_prs(all_prs, target_count)
    print(f"Will analyze {len(sampled_prs)} PRs")

    # Step 3: Analyze each PR (fast mode - only get reviews)
    print("\n[3/4] Analyzing PRs...")
    analyzed_prs = []

    for i, pr in enumerate(sampled_prs):
        # Only get reviews for a subset to save API calls
        get_reviews = (i < 200)  # Get reviews for first 200 PRs

        if (i + 1) % 20 == 0 or i == 0:
            print(f"  Analyzing PR #{pr['number']} ({i+1}/{len(sampled_prs)})...")

        try:
            analysis = analyze_pr_fast(pr, get_reviews=get_reviews)
            analyzed_prs.append(analysis)
        except Exception as e:
            print(f"    Error analyzing PR #{pr['number']}: {e}")

    # Step 4: Generate report
    print("\n[4/4] Generating report...")
    report = generate_report(analyzed_prs, total_merged)

    # Save report
    output_file = "PR_ANALYSIS_REPORT.md"
    with open(output_file, "w") as f:
        f.write(report)
    print(f"Report saved to {output_file}")

    # Also save raw data as JSON
    json_file = "pr_analysis_data.json"
    with open(json_file, "w") as f:
        for pr in analyzed_prs:
            pr["blocker_summary"] = dict(pr["blocker_summary"])
        json.dump(analyzed_prs, f, indent=2, default=str)
    print(f"Raw data saved to {json_file}")

    print("\n" + "=" * 60)
    print("Analysis complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
