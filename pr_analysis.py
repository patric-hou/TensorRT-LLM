#!/usr/bin/env python3
"""
PR Analysis Script for TensorRT-LLM repository.
Fetches merged PRs from GitHub API and analyzes blockers.
"""

import json
import os
import random
import time
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

import requests

# GitHub API configuration
GITHUB_API = "https://api.github.com"
REPO_OWNER = "NVIDIA"
REPO_NAME = "TensorRT-LLM"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Rate limiting
REQUEST_DELAY = 0.5  # seconds between requests without token
REQUEST_DELAY_WITH_TOKEN = 0.1

# Headers
def get_headers():
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


def api_request(url: str, params: Dict = None, retries: int = 3) -> Optional[Dict]:
    """Make API request with retry logic."""
    delay = REQUEST_DELAY_WITH_TOKEN if GITHUB_TOKEN else REQUEST_DELAY

    for attempt in range(retries):
        try:
            response = requests.get(url, headers=get_headers(), params=params, timeout=30)

            if response.status_code == 200:
                time.sleep(delay)
                return response.json()
            elif response.status_code == 403:
                # Rate limited
                reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
                wait_time = max(reset_time - time.time(), 60)
                print(f"Rate limited. Waiting {wait_time:.0f}s...")
                time.sleep(min(wait_time, 300))  # Max 5 minutes wait
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


def get_merged_prs_list(per_page: int = 100, max_pages: int = 50) -> List[Dict]:
    """Get list of merged PRs (basic info only)."""
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

        if len(prs) < per_page:
            break

    return all_prs


def get_pr_details(pr_number: int) -> Optional[Dict]:
    """Get detailed PR information."""
    url = f"{GITHUB_API}/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pr_number}"
    return api_request(url)


def get_pr_commits(pr_number: int) -> List[Dict]:
    """Get commits for a PR."""
    url = f"{GITHUB_API}/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pr_number}/commits"
    params = {"per_page": 100}
    result = api_request(url, params)
    return result if result else []


def get_pr_reviews(pr_number: int) -> List[Dict]:
    """Get reviews for a PR."""
    url = f"{GITHUB_API}/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pr_number}/reviews"
    params = {"per_page": 100}
    result = api_request(url, params)
    return result if result else []


def get_pr_comments(pr_number: int) -> List[Dict]:
    """Get review comments for a PR."""
    url = f"{GITHUB_API}/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pr_number}/comments"
    params = {"per_page": 100}
    result = api_request(url, params)
    return result if result else []


def get_pr_issue_comments(pr_number: int) -> List[Dict]:
    """Get issue comments (including bot comments) for a PR."""
    url = f"{GITHUB_API}/repos/{REPO_OWNER}/{REPO_NAME}/issues/{pr_number}/comments"
    params = {"per_page": 100}
    result = api_request(url, params)
    return result if result else []


def get_commit_check_runs(sha: str) -> List[Dict]:
    """Get check runs for a commit."""
    url = f"{GITHUB_API}/repos/{REPO_OWNER}/{REPO_NAME}/commits/{sha}/check-runs"
    params = {"per_page": 100}
    result = api_request(url, params)
    return result.get("check_runs", []) if result else []


def get_commit_statuses(sha: str) -> List[Dict]:
    """Get statuses for a commit."""
    url = f"{GITHUB_API}/repos/{REPO_OWNER}/{REPO_NAME}/commits/{sha}/statuses"
    params = {"per_page": 100}
    result = api_request(url, params)
    return result if result else []


def analyze_pr_blockers(pr_data: Dict) -> Dict[str, Any]:
    """
    Analyze blockers for a single PR.

    Returns dict with:
    - pr_number: PR number
    - pr_url: GitHub URL
    - title: PR title
    - created_at: Creation time
    - merged_at: Merge time
    - merge_duration_hours: Time to merge in hours
    - commit_count: Number of commits
    - blockers: List of blocker events with types and counts
    """
    pr_number = pr_data["number"]

    # Basic PR info
    result = {
        "pr_number": pr_number,
        "pr_url": pr_data["html_url"],
        "title": pr_data["title"],
        "author": pr_data["user"]["login"],
        "created_at": pr_data["created_at"],
        "merged_at": pr_data["merged_at"],
        "merge_duration_hours": 0,
        "commit_count": 0,
        "blockers": [],
        "blocker_summary": defaultdict(int),
    }

    # Calculate merge duration
    created = datetime.fromisoformat(pr_data["created_at"].replace("Z", "+00:00"))
    merged = datetime.fromisoformat(pr_data["merged_at"].replace("Z", "+00:00"))
    result["merge_duration_hours"] = (merged - created).total_seconds() / 3600

    # Get commits
    commits = get_pr_commits(pr_number)
    result["commit_count"] = len(commits)

    # Get reviews
    reviews = get_pr_reviews(pr_number)
    for review in reviews:
        state = review.get("state", "").upper()
        if state == "CHANGES_REQUESTED":
            result["blockers"].append({
                "type": "changes_requested",
                "reviewer": review.get("user", {}).get("login", "unknown"),
                "time": review.get("submitted_at", ""),
            })
            result["blocker_summary"]["changes_requested"] += 1

    # Get issue comments for bot messages
    issue_comments = get_pr_issue_comments(pr_number)
    for comment in issue_comments:
        body = comment.get("body", "").lower()
        user = comment.get("user", {}).get("login", "").lower()

        # CI failure indicators
        if "ci failed" in body or "test failed" in body or "check failed" in body:
            result["blockers"].append({
                "type": "ci_failure",
                "source": user,
                "time": comment.get("created_at", ""),
            })
            result["blocker_summary"]["ci_failure"] += 1

        # Pre-commit failure
        if "pre-commit" in body and ("fail" in body or "error" in body):
            result["blockers"].append({
                "type": "precommit_failure",
                "source": user,
                "time": comment.get("created_at", ""),
            })
            result["blocker_summary"]["precommit_failure"] += 1

        # PR title format issue
        if "pr title" in body and ("format" in body or "invalid" in body):
            result["blockers"].append({
                "type": "title_format_error",
                "source": user,
                "time": comment.get("created_at", ""),
            })
            result["blocker_summary"]["title_format_error"] += 1

    # Check the latest commit's check runs
    if commits:
        latest_sha = commits[-1]["sha"]
        check_runs = get_commit_check_runs(latest_sha)
        statuses = get_commit_statuses(latest_sha)

        # Count failed checks
        failed_checks = [cr for cr in check_runs if cr.get("conclusion") == "failure"]
        for fc in failed_checks:
            check_name = fc.get("name", "unknown")
            # Skip counting if it's on the final successful commit
            # We want to look at intermediate failures

        # Count failed statuses
        failed_statuses = [s for s in statuses if s.get("state") == "failure"]

    # Look at ALL commits to find CI failures (not just the last one)
    ci_failure_count = 0
    for i, commit in enumerate(commits):
        if i == len(commits) - 1:
            # Skip the final commit as it succeeded
            continue

        sha = commit["sha"]
        check_runs = get_commit_check_runs(sha)

        for cr in check_runs:
            if cr.get("conclusion") == "failure":
                check_name = cr.get("name", "unknown")
                result["blockers"].append({
                    "type": "ci_check_failure",
                    "check_name": check_name,
                    "commit": sha[:7],
                    "time": cr.get("completed_at", ""),
                })
                ci_failure_count += 1

        # Limit API calls - only check first few commits if many
        if i >= 5:
            break

    if ci_failure_count > 0:
        result["blocker_summary"]["ci_check_failure"] = ci_failure_count

    return result


def sample_prs(all_prs: List[Dict], target_count: int = 1000) -> List[Dict]:
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


def generate_report(analyzed_prs: List[Dict]) -> str:
    """Generate markdown report from analyzed PRs."""

    # Calculate statistics
    durations = [pr["merge_duration_hours"] for pr in analyzed_prs]
    commit_counts = [pr["commit_count"] for pr in analyzed_prs]

    avg_duration = sum(durations) / len(durations) if durations else 0
    sorted_durations = sorted(durations)
    median_duration = sorted_durations[len(sorted_durations) // 2] if sorted_durations else 0

    avg_commits = sum(commit_counts) / len(commit_counts) if commit_counts else 0

    # Sort by duration for top/bottom 10
    prs_by_duration = sorted(analyzed_prs, key=lambda x: x["merge_duration_hours"], reverse=True)
    longest_10 = prs_by_duration[:10]
    shortest_10 = prs_by_duration[-10:]

    # Aggregate blocker statistics
    all_blockers = defaultdict(int)
    prs_with_blockers = 0
    for pr in analyzed_prs:
        if pr["blocker_summary"]:
            prs_with_blockers += 1
        for blocker_type, count in pr["blocker_summary"].items():
            all_blockers[blocker_type] += count

    # Build report
    report = []
    report.append("# TensorRT-LLM PR Analysis Report")
    report.append("")
    report.append(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    report.append("")

    # Summary section
    report.append("## Summary Statistics")
    report.append("")
    report.append(f"- **Total PRs Analyzed**: {len(analyzed_prs)}")
    report.append(f"- **PRs with Blockers**: {prs_with_blockers} ({prs_with_blockers/len(analyzed_prs)*100:.1f}%)")
    report.append(f"- **Average Merge Duration**: {format_duration(avg_duration)} ({avg_duration:.1f} hours)")
    report.append(f"- **Median Merge Duration**: {format_duration(median_duration)} ({median_duration:.1f} hours)")
    report.append(f"- **Average Commit Count**: {avg_commits:.1f}")
    report.append("")

    # Blocker distribution
    report.append("## Blocker Type Distribution")
    report.append("")
    report.append("| Blocker Type | Count | Description |")
    report.append("|-------------|-------|-------------|")

    blocker_descriptions = {
        "changes_requested": "Reviewer requested changes",
        "ci_failure": "CI pipeline failure (from comments)",
        "ci_check_failure": "CI check failure (from GitHub checks)",
        "precommit_failure": "Pre-commit hook failure",
        "title_format_error": "PR title format validation error",
    }

    for blocker_type, count in sorted(all_blockers.items(), key=lambda x: x[1], reverse=True):
        desc = blocker_descriptions.get(blocker_type, blocker_type)
        report.append(f"| {blocker_type} | {count} | {desc} |")
    report.append("")

    # Top 10 longest
    report.append("## Top 10 Longest Merge Duration PRs")
    report.append("")
    report.append("| PR | Duration | Commits | Blockers |")
    report.append("|----|----------|---------|----------|")
    for pr in longest_10:
        pr_link = f"[#{pr['pr_number']}]({pr['pr_url']})"
        duration = format_duration(pr["merge_duration_hours"])
        blockers_str = ", ".join([f"{k}:{v}" for k, v in pr["blocker_summary"].items()]) or "None"
        report.append(f"| {pr_link} | {duration} | {pr['commit_count']} | {blockers_str} |")
    report.append("")

    # Top 10 shortest
    report.append("## Top 10 Shortest Merge Duration PRs")
    report.append("")
    report.append("| PR | Duration | Commits | Blockers |")
    report.append("|----|----------|---------|----------|")
    for pr in shortest_10:
        pr_link = f"[#{pr['pr_number']}]({pr['pr_url']})"
        duration = format_duration(pr["merge_duration_hours"])
        blockers_str = ", ".join([f"{k}:{v}" for k, v in pr["blocker_summary"].items()]) or "None"
        report.append(f"| {pr_link} | {duration} | {pr['commit_count']} | {blockers_str} |")
    report.append("")

    # CI/CD Configuration Analysis
    report.append("## CI/CD Configuration Analysis")
    report.append("")
    report.append("Based on the repository's GitHub Actions workflows, the following checks can cause PR blockers:")
    report.append("")
    report.append("### 1. PR Title Format Check (`pr-check.yml`)")
    report.append("- **Trigger**: PR opened, edited, synchronize, reopened")
    report.append("- **Requirement**: PR title must match pattern `[Ticket][type] Summary`")
    report.append("- **Valid ticket formats**: JIRA (TRTLLM-1234), NVBugs (https://nvbugs/123), GitHub issue (#123), or [None]")
    report.append("- **Valid types**: [fix], [feat], [doc], [infra], [chore], etc.")
    report.append("")
    report.append("### 2. PR Checklist Check (`pr-check.yml`)")
    report.append("- **Trigger**: PR opened, edited, synchronize, reopened")
    report.append("- **Requirement**: All checklist items in PR body must be resolved")
    report.append("")
    report.append("### 3. Pre-commit Check (`precommit-check.yml`)")
    report.append("- **Trigger**: Every PR")
    report.append("- **Checks performed**:")
    report.append("  - Code formatting (isort, yapf, autoflake, ruff)")
    report.append("  - Bandit security scan")
    report.append("  - License headers")
    report.append("  - YAML/JSON validation")
    report.append("")
    report.append("### 4. Blossom CI (`blossom-ci.yml`)")
    report.append("- **Trigger**: `/bot run` comment from authorized users")
    report.append("- **Checks performed**:")
    report.append("  - Vulnerability scan")
    report.append("  - Jenkins CI job (comprehensive testing)")
    report.append("- **Note**: Only authorized NVIDIA team members can trigger CI")
    report.append("")
    report.append("### 5. L0 Test Results (`l0-test.yml`)")
    report.append("- **Trigger**: Workflow dispatch after CI completion")
    report.append("- **Updates**: Commit status with test pass/fail counts")
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
    print("TensorRT-LLM PR Analysis")
    print("=" * 60)

    # Step 1: Get merged PR count
    print("\n[1/4] Getting merged PR count...")
    total_merged = get_merged_prs_count()
    print(f"Total merged PRs: {total_merged}")

    # Step 2: Fetch PR list
    print("\n[2/4] Fetching PR list...")
    target_count = min(1000, total_merged) if total_merged > 0 else 1000
    # Fetch more pages to get enough PRs
    max_pages = (target_count // 100) + 10
    all_prs = get_merged_prs_list(per_page=100, max_pages=max_pages)
    print(f"Fetched {len(all_prs)} merged PRs")

    # Sample if needed
    sampled_prs = sample_prs(all_prs, target_count)
    print(f"Sampled {len(sampled_prs)} PRs for analysis")

    # Step 3: Analyze each PR
    print("\n[3/4] Analyzing PRs...")
    analyzed_prs = []
    for i, pr in enumerate(sampled_prs):
        print(f"  Analyzing PR #{pr['number']} ({i+1}/{len(sampled_prs)})...")
        try:
            analysis = analyze_pr_blockers(pr)
            analyzed_prs.append(analysis)
        except Exception as e:
            print(f"    Error analyzing PR #{pr['number']}: {e}")

        # Progress update every 50 PRs
        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{len(sampled_prs)} PRs analyzed")

    # Step 4: Generate report
    print("\n[4/4] Generating report...")
    report = generate_report(analyzed_prs)

    # Save report
    output_file = "PR_ANALYSIS_REPORT.md"
    with open(output_file, "w") as f:
        f.write(report)
    print(f"Report saved to {output_file}")

    # Also save raw data as JSON for further analysis
    json_file = "pr_analysis_data.json"
    with open(json_file, "w") as f:
        # Convert defaultdict to regular dict for JSON serialization
        for pr in analyzed_prs:
            pr["blocker_summary"] = dict(pr["blocker_summary"])
        json.dump(analyzed_prs, f, indent=2, default=str)
    print(f"Raw data saved to {json_file}")

    print("\n" + "=" * 60)
    print("Analysis complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
