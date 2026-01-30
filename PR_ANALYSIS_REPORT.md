# TensorRT-LLM PR Analysis Report

**Generated**: 2026-01-30 11:09:17 UTC

**Repository**: [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Merged PRs in Repository | 5,546 |
| PRs Analyzed in This Report | 500 |
| PRs with Review Change Requests | 6 (1.2%) |
| Average Merge Duration | 7.7d |
| Median Merge Duration | 2.8d |
| Average Commits per PR | 1.0 |

## Merge Duration Statistics

| Statistic | Duration |
|-----------|----------|
| Minimum | 6m |
| 25th Percentile | 17.5h |
| Median (50th) | 2.8d |
| Average | 7.7d |
| 75th Percentile | 8.2d |
| 90th Percentile | 20.6d |
| Maximum | 142.9d |

### Merge Duration Distribution

| Time Range | Count | Percentage |
|------------|-------|------------|
| < 1 hour | 33 | 6.6% █ |
| 1-6 hours | 48 | 9.6% █ |
| 6-24 hours | 81 | 16.2% ███ |
| 1-3 days | 105 | 21.0% ████ |
| 3-7 days | 89 | 17.8% ███ |
| 1-2 weeks | 69 | 13.8% ██ |
| > 2 weeks | 75 | 15.0% ███ |

## Blocker Type Distribution

| Blocker Type | Count | Description |
|-------------|-------|-------------|
| changes_requested | 5 | Reviewer requested code changes |
| possible_title_format_issue | 1 | PR title may not follow required format |

## CI/CD Configuration Analysis

Based on the repository's GitHub Actions workflows (`.github/workflows/`), the following checks can cause PR blockers:

### 1. PR Title Format Check
**File**: `.github/workflows/pr-check.yml`

- **Trigger**: PR opened, edited, synchronize, reopened
- **Requirement**: PR title must match pattern:
  ```
  [Ticket][type] Summary
  ```
- **Valid ticket formats**:
  - JIRA ticket: `[TRTLLM-1234]`
  - NVBugs ID: `[https://nvbugs/1234567]`
  - GitHub issue: `[#1234]`
  - No ticket: `[None]`
- **Valid types**: `[fix]`, `[feat]`, `[doc]`, `[infra]`, `[chore]`, etc.

### 2. PR Checklist Check
**Files**: `.github/workflows/pr-check.yml`, `.github/scripts/pr_checklist_check.py`

- **Trigger**: PR opened, edited, synchronize, reopened
- **Requirement**: All checklist items in PR body must be resolved (checked)
- **Common issues**: Forgetting to check the final confirmation checkbox

### 3. Pre-commit Check (Release Checks)
**Files**: `.github/workflows/precommit-check.yml`, `scripts/release_check.py`, `.pre-commit-config.yaml`

- **Trigger**: Every PR
- **Checks performed**:
  - Code formatting (isort, yapf, autoflake, ruff)
  - Bandit security scan (no `#nosec` annotations allowed)
  - License header validation
  - YAML/JSON validation
  - Trailing whitespace and end-of-file fixes

### 4. Blossom CI (Jenkins Integration)
**File**: `.github/workflows/blossom-ci.yml`

- **Trigger**: `/bot run` comment from authorized users
- **Authorization**: ~350 authorized NVIDIA team members
- **Checks performed**:
  - Vulnerability scan
  - Jenkins CI job (comprehensive build and test suite)
- **Note**: External contributors must wait for authorized user to trigger CI

### 5. L0 Test Results Upload
**File**: `.github/workflows/l0-test.yml`

- **Trigger**: Workflow dispatch after CI completion
- **Function**: Updates commit status with test pass/fail counts

## Top 10 Longest Merge Duration PRs

| PR | Title | Duration | Commits | Blockers |
|----|-------|----------|---------|----------|
| [#7439](https://github.com/NVIDIA/TensorRT-LLM/pull/7439) | [None][feat] Add KV cache cleanup | 142.9d | 1 | None |
| [#8279](https://github.com/NVIDIA/TensorRT-LLM/pull/8279) | [https://nvbugs/5322131][feat] Multi-LoRA serving ... | 103.5d | 1 | changes_requested:1 |
| [#7846](https://github.com/NVIDIA/TensorRT-LLM/pull/7846) | [None][doc] Added line about partial reuse | 77.3d | 1 | None |
| [#7838](https://github.com/NVIDIA/TensorRT-LLM/pull/7838) | [TRTLLM-7073][feat] Support torch compile for PP f... | 76.8d | 1 | None |
| [#8368](https://github.com/NVIDIA/TensorRT-LLM/pull/8368) | [None][fix] Fix request_id for best_of/n case | 73.3d | 1 | None |
| [#8309](https://github.com/NVIDIA/TensorRT-LLM/pull/8309) | [None][feat] Support Mooncake transfer engine as a... | 66.8d | 1 | None |
| [#8956](https://github.com/NVIDIA/TensorRT-LLM/pull/8956) | [TRTLLM-7138][feat] Support nvfp4 for gptoss | 59.7d | 1 | None |
| [#6097](https://github.com/NVIDIA/TensorRT-LLM/pull/6097) | [TRTLLM-1302][feat] Topk logprobs for TRT backend ... | 57.7d | 1 | None |
| [#8383](https://github.com/NVIDIA/TensorRT-LLM/pull/8383) | [https://nvbugs/5567586][feat] Ampere xqa swa spec... | 54.5d | 1 | None |
| [#9167](https://github.com/NVIDIA/TensorRT-LLM/pull/9167) | [None][infra] add retry logic to get slurm sbatch ... | 50.9d | 1 | None |

## Top 10 Shortest Merge Duration PRs

| PR | Title | Duration | Commits | Blockers |
|----|-------|----------|---------|----------|
| [#9982](https://github.com/NVIDIA/TensorRT-LLM/pull/9982) | [None][infra] Waive failed tests for main branch o... | 28m | 1 | None |
| [#9773](https://github.com/NVIDIA/TensorRT-LLM/pull/9773) | [None][infra] Waive failed cases for main on 12/08 | 27m | 1 | None |
| [#10994](https://github.com/NVIDIA/TensorRT-LLM/pull/10994) | [None][infra] Waive failed case for main branch on... | 25m | 1 | None |
| [#10298](https://github.com/NVIDIA/TensorRT-LLM/pull/10298) | [None][infra] Waive failed tests for main on 12/25 | 25m | 1 | None |
| [#10356](https://github.com/NVIDIA/TensorRT-LLM/pull/10356) | [https://nvbugs/5774869][chore] waive tests. | 24m | 1 | None |
| [#9553](https://github.com/NVIDIA/TensorRT-LLM/pull/9553) | [None][infra] Waive failed tests for release branc... | 23m | 1 | None |
| [#11027](https://github.com/NVIDIA/TensorRT-LLM/pull/11027) | [None][chore] Upgrade starlette and FastAPI (#9319... | 17m | 1 | None |
| [#10869](https://github.com/NVIDIA/TensorRT-LLM/pull/10869) | [None][chore] Revert NVIDIA/TensorRT-LLM#10847 | 17m | 1 | None |
| [#10970](https://github.com/NVIDIA/TensorRT-LLM/pull/10970) | [None][fix] Fix Piecewise Cuda Graph for GPTOSS (#... | 12m | 1 | None |
| [#10967](https://github.com/NVIDIA/TensorRT-LLM/pull/10967) | [None] Add visual gen for Wan | 6m | 1 | None |

## All Analyzed PRs

| PR ID & Link | Blockers (Type: Count) | Commits | Merge Duration |
|--------------|------------------------|---------|----------------|
| [#11101](https://github.com/NVIDIA/TensorRT-LLM/pull/11101) | None | 1 | 21.0h |
| [#11096](https://github.com/NVIDIA/TensorRT-LLM/pull/11096) | None | 1 | 20.1h |
| [#11091](https://github.com/NVIDIA/TensorRT-LLM/pull/11091) | None | 1 | 33m |
| [#11090](https://github.com/NVIDIA/TensorRT-LLM/pull/11090) | None | 1 | 1.1d |
| [#11074](https://github.com/NVIDIA/TensorRT-LLM/pull/11074) | None | 1 | 1.4d |
| [#11065](https://github.com/NVIDIA/TensorRT-LLM/pull/11065) | None | 1 | 1.5d |
| [#11058](https://github.com/NVIDIA/TensorRT-LLM/pull/11058) | None | 1 | 22.6h |
| [#11056](https://github.com/NVIDIA/TensorRT-LLM/pull/11056) | None | 1 | 1.0d |
| [#11054](https://github.com/NVIDIA/TensorRT-LLM/pull/11054) | None | 1 | 5.0h |
| [#11040](https://github.com/NVIDIA/TensorRT-LLM/pull/11040) | None | 1 | 12.0h |
| [#11030](https://github.com/NVIDIA/TensorRT-LLM/pull/11030) | None | 1 | 2.3d |
| [#11027](https://github.com/NVIDIA/TensorRT-LLM/pull/11027) | None | 1 | 17m |
| [#11026](https://github.com/NVIDIA/TensorRT-LLM/pull/11026) | None | 1 | 23.2h |
| [#11024](https://github.com/NVIDIA/TensorRT-LLM/pull/11024) | None | 1 | 1.0d |
| [#11023](https://github.com/NVIDIA/TensorRT-LLM/pull/11023) | None | 1 | 2.7d |
| [#11019](https://github.com/NVIDIA/TensorRT-LLM/pull/11019) | None | 1 | 3.4h |
| [#11018](https://github.com/NVIDIA/TensorRT-LLM/pull/11018) | None | 1 | 2.1d |
| [#11012](https://github.com/NVIDIA/TensorRT-LLM/pull/11012) | None | 1 | 1.1h |
| [#11010](https://github.com/NVIDIA/TensorRT-LLM/pull/11010) | None | 1 | 2.0d |
| [#11007](https://github.com/NVIDIA/TensorRT-LLM/pull/11007) | None | 1 | 2.2d |
| [#11006](https://github.com/NVIDIA/TensorRT-LLM/pull/11006) | None | 1 | 1.1d |
| [#11003](https://github.com/NVIDIA/TensorRT-LLM/pull/11003) | None | 1 | 4.0d |
| [#10999](https://github.com/NVIDIA/TensorRT-LLM/pull/10999) | None | 1 | 45m |
| [#10994](https://github.com/NVIDIA/TensorRT-LLM/pull/10994) | None | 1 | 25m |
| [#10993](https://github.com/NVIDIA/TensorRT-LLM/pull/10993) | None | 1 | 1.1d |
| [#10983](https://github.com/NVIDIA/TensorRT-LLM/pull/10983) | None | 1 | 10.9h |
| [#10976](https://github.com/NVIDIA/TensorRT-LLM/pull/10976) | None | 1 | 23.8h |
| [#10974](https://github.com/NVIDIA/TensorRT-LLM/pull/10974) | None | 1 | 1.2d |
| [#10971](https://github.com/NVIDIA/TensorRT-LLM/pull/10971) | None | 1 | 1.9d |
| [#10970](https://github.com/NVIDIA/TensorRT-LLM/pull/10970) | None | 1 | 12m |
| [#10967](https://github.com/NVIDIA/TensorRT-LLM/pull/10967) | None | 1 | 6m |
| [#10962](https://github.com/NVIDIA/TensorRT-LLM/pull/10962) | None | 1 | 4.1d |
| [#10957](https://github.com/NVIDIA/TensorRT-LLM/pull/10957) | None | 1 | 4.2d |
| [#10954](https://github.com/NVIDIA/TensorRT-LLM/pull/10954) | None | 1 | 2.8d |
| [#10953](https://github.com/NVIDIA/TensorRT-LLM/pull/10953) | None | 1 | 1.5h |
| [#10945](https://github.com/NVIDIA/TensorRT-LLM/pull/10945) | None | 1 | 22.9h |
| [#10935](https://github.com/NVIDIA/TensorRT-LLM/pull/10935) | None | 1 | 6.9d |
| [#10929](https://github.com/NVIDIA/TensorRT-LLM/pull/10929) | None | 1 | 5.2d |
| [#10925](https://github.com/NVIDIA/TensorRT-LLM/pull/10925) | None | 1 | 1.9d |
| [#10923](https://github.com/NVIDIA/TensorRT-LLM/pull/10923) | None | 1 | 1.0h |
| [#10922](https://github.com/NVIDIA/TensorRT-LLM/pull/10922) | None | 1 | 6.9d |
| [#10918](https://github.com/NVIDIA/TensorRT-LLM/pull/10918) | None | 1 | 1.9d |
| [#10916](https://github.com/NVIDIA/TensorRT-LLM/pull/10916) | None | 1 | 18.9h |
| [#10914](https://github.com/NVIDIA/TensorRT-LLM/pull/10914) | None | 1 | 3.9d |
| [#10911](https://github.com/NVIDIA/TensorRT-LLM/pull/10911) | None | 1 | 4.0d |
| [#10896](https://github.com/NVIDIA/TensorRT-LLM/pull/10896) | None | 1 | 1.5d |
| [#10890](https://github.com/NVIDIA/TensorRT-LLM/pull/10890) | None | 1 | 17.6h |
| [#10883](https://github.com/NVIDIA/TensorRT-LLM/pull/10883) | None | 1 | 2.0d |
| [#10882](https://github.com/NVIDIA/TensorRT-LLM/pull/10882) | None | 1 | 42m |
| [#10881](https://github.com/NVIDIA/TensorRT-LLM/pull/10881) | None | 1 | 5.9d |
| [#10878](https://github.com/NVIDIA/TensorRT-LLM/pull/10878) | None | 1 | 14.5h |
| [#10871](https://github.com/NVIDIA/TensorRT-LLM/pull/10871) | None | 1 | 2.5d |
| [#10869](https://github.com/NVIDIA/TensorRT-LLM/pull/10869) | None | 1 | 17m |
| [#10868](https://github.com/NVIDIA/TensorRT-LLM/pull/10868) | None | 1 | 1.0d |
| [#10867](https://github.com/NVIDIA/TensorRT-LLM/pull/10867) | None | 1 | 8.9d |
| [#10866](https://github.com/NVIDIA/TensorRT-LLM/pull/10866) | None | 1 | 1.1d |
| [#10865](https://github.com/NVIDIA/TensorRT-LLM/pull/10865) | None | 1 | 1.3d |
| [#10854](https://github.com/NVIDIA/TensorRT-LLM/pull/10854) | None | 1 | 5.9d |
| [#10844](https://github.com/NVIDIA/TensorRT-LLM/pull/10844) | None | 1 | 17.4h |
| [#10841](https://github.com/NVIDIA/TensorRT-LLM/pull/10841) | None | 1 | 21.1h |
| [#10833](https://github.com/NVIDIA/TensorRT-LLM/pull/10833) | None | 1 | 2.2d |
| [#10831](https://github.com/NVIDIA/TensorRT-LLM/pull/10831) | None | 1 | 18.0h |
| [#10830](https://github.com/NVIDIA/TensorRT-LLM/pull/10830) | None | 1 | 1.5d |
| [#10829](https://github.com/NVIDIA/TensorRT-LLM/pull/10829) | None | 1 | 2.5h |
| [#10825](https://github.com/NVIDIA/TensorRT-LLM/pull/10825) | None | 1 | 1.8h |
| [#10822](https://github.com/NVIDIA/TensorRT-LLM/pull/10822) | None | 1 | 23.5h |
| [#10819](https://github.com/NVIDIA/TensorRT-LLM/pull/10819) | None | 1 | 9.4h |
| [#10808](https://github.com/NVIDIA/TensorRT-LLM/pull/10808) | None | 1 | 7.1d |
| [#10806](https://github.com/NVIDIA/TensorRT-LLM/pull/10806) | None | 1 | 22.5h |
| [#10797](https://github.com/NVIDIA/TensorRT-LLM/pull/10797) | None | 1 | 11.2d |
| [#10786](https://github.com/NVIDIA/TensorRT-LLM/pull/10786) | None | 1 | 1.5d |
| [#10783](https://github.com/NVIDIA/TensorRT-LLM/pull/10783) | None | 1 | 7.7d |
| [#10781](https://github.com/NVIDIA/TensorRT-LLM/pull/10781) | None | 1 | 1.3h |
| [#10779](https://github.com/NVIDIA/TensorRT-LLM/pull/10779) | None | 1 | 18.9h |
| [#10777](https://github.com/NVIDIA/TensorRT-LLM/pull/10777) | None | 1 | 1.7h |
| [#10771](https://github.com/NVIDIA/TensorRT-LLM/pull/10771) | None | 1 | 2.0d |
| [#10768](https://github.com/NVIDIA/TensorRT-LLM/pull/10768) | None | 1 | 4.9d |
| [#10766](https://github.com/NVIDIA/TensorRT-LLM/pull/10766) | None | 1 | 6.3h |
| [#10760](https://github.com/NVIDIA/TensorRT-LLM/pull/10760) | None | 1 | 1.2d |
| [#10758](https://github.com/NVIDIA/TensorRT-LLM/pull/10758) | None | 1 | 5.9d |
| [#10757](https://github.com/NVIDIA/TensorRT-LLM/pull/10757) | None | 1 | 10.8d |
| [#10756](https://github.com/NVIDIA/TensorRT-LLM/pull/10756) | None | 1 | 4.8d |
| [#10755](https://github.com/NVIDIA/TensorRT-LLM/pull/10755) | None | 1 | 7.8d |
| [#10749](https://github.com/NVIDIA/TensorRT-LLM/pull/10749) | None | 1 | 2.8d |
| [#10746](https://github.com/NVIDIA/TensorRT-LLM/pull/10746) | None | 1 | 55m |
| [#10743](https://github.com/NVIDIA/TensorRT-LLM/pull/10743) | None | 1 | 7.7h |
| [#10741](https://github.com/NVIDIA/TensorRT-LLM/pull/10741) | None | 1 | 2.9d |
| [#10738](https://github.com/NVIDIA/TensorRT-LLM/pull/10738) | None | 1 | 1.2h |
| [#10737](https://github.com/NVIDIA/TensorRT-LLM/pull/10737) | None | 1 | 43m |
| [#10734](https://github.com/NVIDIA/TensorRT-LLM/pull/10734) | None | 1 | 11.2h |
| [#10731](https://github.com/NVIDIA/TensorRT-LLM/pull/10731) | None | 1 | 3.4d |
| [#10730](https://github.com/NVIDIA/TensorRT-LLM/pull/10730) | None | 1 | 7.3d |
| [#10727](https://github.com/NVIDIA/TensorRT-LLM/pull/10727) | None | 1 | 22.8h |
| [#10726](https://github.com/NVIDIA/TensorRT-LLM/pull/10726) | None | 1 | 4.7h |
| [#10722](https://github.com/NVIDIA/TensorRT-LLM/pull/10722) | None | 1 | 19.5h |
| [#10716](https://github.com/NVIDIA/TensorRT-LLM/pull/10716) | None | 1 | 3.4d |
| [#10711](https://github.com/NVIDIA/TensorRT-LLM/pull/10711) | None | 1 | 35m |
| [#10703](https://github.com/NVIDIA/TensorRT-LLM/pull/10703) | None | 1 | 16.6h |
| [#10699](https://github.com/NVIDIA/TensorRT-LLM/pull/10699) | None | 1 | 7.7d |
| [#10698](https://github.com/NVIDIA/TensorRT-LLM/pull/10698) | None | 1 | 18.3h |
| [#10686](https://github.com/NVIDIA/TensorRT-LLM/pull/10686) | None | 1 | 50m |
| [#10681](https://github.com/NVIDIA/TensorRT-LLM/pull/10681) | None | 1 | 3.2h |
| [#10675](https://github.com/NVIDIA/TensorRT-LLM/pull/10675) | None | 1 | 4.0d |
| [#10669](https://github.com/NVIDIA/TensorRT-LLM/pull/10669) | None | 1 | 6.7d |
| [#10665](https://github.com/NVIDIA/TensorRT-LLM/pull/10665) | None | 1 | 23.4h |
| [#10664](https://github.com/NVIDIA/TensorRT-LLM/pull/10664) | None | 1 | 1.8d |
| [#10660](https://github.com/NVIDIA/TensorRT-LLM/pull/10660) | None | 1 | 2.9d |
| [#10655](https://github.com/NVIDIA/TensorRT-LLM/pull/10655) | None | 1 | 50m |
| [#10654](https://github.com/NVIDIA/TensorRT-LLM/pull/10654) | None | 1 | 6.1d |
| [#10638](https://github.com/NVIDIA/TensorRT-LLM/pull/10638) | None | 1 | 1.4d |
| [#10635](https://github.com/NVIDIA/TensorRT-LLM/pull/10635) | None | 1 | 14.0d |
| [#10630](https://github.com/NVIDIA/TensorRT-LLM/pull/10630) | None | 1 | 1.0d |
| [#10627](https://github.com/NVIDIA/TensorRT-LLM/pull/10627) | None | 1 | 18.8h |
| [#10626](https://github.com/NVIDIA/TensorRT-LLM/pull/10626) | None | 1 | 19.6h |
| [#10625](https://github.com/NVIDIA/TensorRT-LLM/pull/10625) | None | 1 | 1.7d |
| [#10619](https://github.com/NVIDIA/TensorRT-LLM/pull/10619) | None | 1 | 12.4h |
| [#10616](https://github.com/NVIDIA/TensorRT-LLM/pull/10616) | None | 1 | 6.1d |
| [#10613](https://github.com/NVIDIA/TensorRT-LLM/pull/10613) | None | 1 | 9.8d |
| [#10610](https://github.com/NVIDIA/TensorRT-LLM/pull/10610) | None | 1 | 7.9d |
| [#10606](https://github.com/NVIDIA/TensorRT-LLM/pull/10606) | None | 1 | 19.8h |
| [#10604](https://github.com/NVIDIA/TensorRT-LLM/pull/10604) | None | 1 | 30m |
| [#10593](https://github.com/NVIDIA/TensorRT-LLM/pull/10593) | None | 1 | 2.3h |
| [#10586](https://github.com/NVIDIA/TensorRT-LLM/pull/10586) | None | 1 | 4.8d |
| [#10584](https://github.com/NVIDIA/TensorRT-LLM/pull/10584) | None | 1 | 5.0d |
| [#10577](https://github.com/NVIDIA/TensorRT-LLM/pull/10577) | None | 1 | 2.7d |
| [#10570](https://github.com/NVIDIA/TensorRT-LLM/pull/10570) | None | 1 | 14.5d |
| [#10569](https://github.com/NVIDIA/TensorRT-LLM/pull/10569) | None | 1 | 5.3d |
| [#10561](https://github.com/NVIDIA/TensorRT-LLM/pull/10561) | None | 1 | 13.1h |
| [#10560](https://github.com/NVIDIA/TensorRT-LLM/pull/10560) | None | 1 | 6.0h |
| [#10559](https://github.com/NVIDIA/TensorRT-LLM/pull/10559) | None | 1 | 7.0d |
| [#10555](https://github.com/NVIDIA/TensorRT-LLM/pull/10555) | None | 1 | 51m |
| [#10551](https://github.com/NVIDIA/TensorRT-LLM/pull/10551) | None | 1 | 11.7d |
| [#10550](https://github.com/NVIDIA/TensorRT-LLM/pull/10550) | None | 1 | 18.0d |
| [#10539](https://github.com/NVIDIA/TensorRT-LLM/pull/10539) | None | 1 | 11.8d |
| [#10536](https://github.com/NVIDIA/TensorRT-LLM/pull/10536) | None | 1 | 1.2h |
| [#10529](https://github.com/NVIDIA/TensorRT-LLM/pull/10529) | None | 1 | 3.4h |
| [#10525](https://github.com/NVIDIA/TensorRT-LLM/pull/10525) | None | 1 | 20.9d |
| [#10524](https://github.com/NVIDIA/TensorRT-LLM/pull/10524) | None | 1 | 5.4d |
| [#10522](https://github.com/NVIDIA/TensorRT-LLM/pull/10522) | None | 1 | 9.0d |
| [#10516](https://github.com/NVIDIA/TensorRT-LLM/pull/10516) | None | 1 | 2.0d |
| [#10512](https://github.com/NVIDIA/TensorRT-LLM/pull/10512) | None | 1 | 1.2d |
| [#10499](https://github.com/NVIDIA/TensorRT-LLM/pull/10499) | None | 1 | 6.0d |
| [#10492](https://github.com/NVIDIA/TensorRT-LLM/pull/10492) | None | 1 | 18.3h |
| [#10488](https://github.com/NVIDIA/TensorRT-LLM/pull/10488) | None | 1 | 6.8d |
| [#10466](https://github.com/NVIDIA/TensorRT-LLM/pull/10466) | None | 1 | 3.7h |
| [#10460](https://github.com/NVIDIA/TensorRT-LLM/pull/10460) | None | 1 | 8.5d |
| [#10457](https://github.com/NVIDIA/TensorRT-LLM/pull/10457) | None | 1 | 15.3h |
| [#10452](https://github.com/NVIDIA/TensorRT-LLM/pull/10452) | None | 1 | 5.8h |
| [#10451](https://github.com/NVIDIA/TensorRT-LLM/pull/10451) | None | 1 | 7.7d |
| [#10449](https://github.com/NVIDIA/TensorRT-LLM/pull/10449) | None | 1 | 19.0h |
| [#10444](https://github.com/NVIDIA/TensorRT-LLM/pull/10444) | None | 1 | 9.7d |
| [#10441](https://github.com/NVIDIA/TensorRT-LLM/pull/10441) | None | 1 | 56m |
| [#10440](https://github.com/NVIDIA/TensorRT-LLM/pull/10440) | None | 1 | 1.6h |
| [#10439](https://github.com/NVIDIA/TensorRT-LLM/pull/10439) | None | 1 | 9.8d |
| [#10438](https://github.com/NVIDIA/TensorRT-LLM/pull/10438) | None | 1 | 60m |
| [#10430](https://github.com/NVIDIA/TensorRT-LLM/pull/10430) | None | 1 | 17.8h |
| [#10421](https://github.com/NVIDIA/TensorRT-LLM/pull/10421) | None | 1 | 7.5h |
| [#10420](https://github.com/NVIDIA/TensorRT-LLM/pull/10420) | None | 1 | 8.8d |
| [#10419](https://github.com/NVIDIA/TensorRT-LLM/pull/10419) | None | 1 | 7.5h |
| [#10406](https://github.com/NVIDIA/TensorRT-LLM/pull/10406) | None | 1 | 10.1d |
| [#10403](https://github.com/NVIDIA/TensorRT-LLM/pull/10403) | None | 1 | 38m |
| [#10402](https://github.com/NVIDIA/TensorRT-LLM/pull/10402) | None | 1 | 8.4d |
| [#10401](https://github.com/NVIDIA/TensorRT-LLM/pull/10401) | None | 1 | 7.1d |
| [#10400](https://github.com/NVIDIA/TensorRT-LLM/pull/10400) | None | 1 | 15.6h |
| [#10393](https://github.com/NVIDIA/TensorRT-LLM/pull/10393) | None | 1 | 19.1h |
| [#10389](https://github.com/NVIDIA/TensorRT-LLM/pull/10389) | None | 1 | 2.9d |
| [#10387](https://github.com/NVIDIA/TensorRT-LLM/pull/10387) | None | 1 | 3.9d |
| [#10386](https://github.com/NVIDIA/TensorRT-LLM/pull/10386) | None | 1 | 2.9d |
| [#10385](https://github.com/NVIDIA/TensorRT-LLM/pull/10385) | None | 1 | 2.9d |
| [#10384](https://github.com/NVIDIA/TensorRT-LLM/pull/10384) | None | 1 | 3.7d |
| [#10383](https://github.com/NVIDIA/TensorRT-LLM/pull/10383) | None | 1 | 2.9d |
| [#10382](https://github.com/NVIDIA/TensorRT-LLM/pull/10382) | None | 1 | 5.0d |
| [#10380](https://github.com/NVIDIA/TensorRT-LLM/pull/10380) | None | 1 | 12.6d |
| [#10378](https://github.com/NVIDIA/TensorRT-LLM/pull/10378) | None | 1 | 2.3d |
| [#10376](https://github.com/NVIDIA/TensorRT-LLM/pull/10376) | None | 1 | 4.8h |
| [#10375](https://github.com/NVIDIA/TensorRT-LLM/pull/10375) | None | 1 | 1.0d |
| [#10369](https://github.com/NVIDIA/TensorRT-LLM/pull/10369) | None | 1 | 22.8d |
| [#10368](https://github.com/NVIDIA/TensorRT-LLM/pull/10368) | None | 1 | 13.5h |
| [#10357](https://github.com/NVIDIA/TensorRT-LLM/pull/10357) | None | 1 | 5.1d |
| [#10356](https://github.com/NVIDIA/TensorRT-LLM/pull/10356) | None | 1 | 24m |
| [#10355](https://github.com/NVIDIA/TensorRT-LLM/pull/10355) | None | 1 | 11.3d |
| [#10354](https://github.com/NVIDIA/TensorRT-LLM/pull/10354) | None | 1 | 9.6h |
| [#10351](https://github.com/NVIDIA/TensorRT-LLM/pull/10351) | None | 1 | 22.2d |
| [#10350](https://github.com/NVIDIA/TensorRT-LLM/pull/10350) | None | 1 | 5.6d |
| [#10344](https://github.com/NVIDIA/TensorRT-LLM/pull/10344) | None | 1 | 15.7h |
| [#10338](https://github.com/NVIDIA/TensorRT-LLM/pull/10338) | None | 1 | 1.4h |
| [#10336](https://github.com/NVIDIA/TensorRT-LLM/pull/10336) | None | 1 | 5.9d |
| [#10335](https://github.com/NVIDIA/TensorRT-LLM/pull/10335) | None | 1 | 16.1d |
| [#10334](https://github.com/NVIDIA/TensorRT-LLM/pull/10334) | None | 1 | 21.4h |
| [#10333](https://github.com/NVIDIA/TensorRT-LLM/pull/10333) | None | 1 | 48m |
| [#10332](https://github.com/NVIDIA/TensorRT-LLM/pull/10332) | None | 1 | 3.0d |
| [#10327](https://github.com/NVIDIA/TensorRT-LLM/pull/10327) | None | 1 | 17.8d |
| [#10324](https://github.com/NVIDIA/TensorRT-LLM/pull/10324) | None | 1 | 1.1h |
| [#10321](https://github.com/NVIDIA/TensorRT-LLM/pull/10321) | None | 1 | 1.3d |
| [#10320](https://github.com/NVIDIA/TensorRT-LLM/pull/10320) | None | 1 | 21.5d |
| [#10314](https://github.com/NVIDIA/TensorRT-LLM/pull/10314) | None | 1 | 8.0d |
| [#10311](https://github.com/NVIDIA/TensorRT-LLM/pull/10311) | None | 1 | 2.3d |
| [#10303](https://github.com/NVIDIA/TensorRT-LLM/pull/10303) | None | 1 | 10.9h |
| [#10302](https://github.com/NVIDIA/TensorRT-LLM/pull/10302) | None | 1 | 4.6d |
| [#10299](https://github.com/NVIDIA/TensorRT-LLM/pull/10299) | None | 1 | 6.9d |
| [#10298](https://github.com/NVIDIA/TensorRT-LLM/pull/10298) | None | 1 | 25m |
| [#10288](https://github.com/NVIDIA/TensorRT-LLM/pull/10288) | None | 1 | 11.0d |
| [#10286](https://github.com/NVIDIA/TensorRT-LLM/pull/10286) | None | 1 | 39m |
| [#10285](https://github.com/NVIDIA/TensorRT-LLM/pull/10285) | None | 1 | 9.2d |
| [#10283](https://github.com/NVIDIA/TensorRT-LLM/pull/10283) | None | 1 | 14.7h |
| [#10279](https://github.com/NVIDIA/TensorRT-LLM/pull/10279) | None | 1 | 32.0d |
| [#10275](https://github.com/NVIDIA/TensorRT-LLM/pull/10275) | None | 1 | 6.0d |
| [#10272](https://github.com/NVIDIA/TensorRT-LLM/pull/10272) | None | 1 | 21.1d |
| [#10267](https://github.com/NVIDIA/TensorRT-LLM/pull/10267) | None | 1 | 1.0h |
| [#10266](https://github.com/NVIDIA/TensorRT-LLM/pull/10266) | None | 1 | 27.8d |
| [#10262](https://github.com/NVIDIA/TensorRT-LLM/pull/10262) | None | 1 | 6.9h |
| [#10253](https://github.com/NVIDIA/TensorRT-LLM/pull/10253) | None | 1 | 6.8h |
| [#10252](https://github.com/NVIDIA/TensorRT-LLM/pull/10252) | None | 1 | 7.8d |
| [#10249](https://github.com/NVIDIA/TensorRT-LLM/pull/10249) | None | 1 | 1.2d |
| [#10248](https://github.com/NVIDIA/TensorRT-LLM/pull/10248) | None | 1 | 6.2h |
| [#10236](https://github.com/NVIDIA/TensorRT-LLM/pull/10236) | None | 1 | 2.9h |
| [#10235](https://github.com/NVIDIA/TensorRT-LLM/pull/10235) | None | 1 | 31.1d |
| [#10234](https://github.com/NVIDIA/TensorRT-LLM/pull/10234) | None | 1 | 12.6d |
| [#10232](https://github.com/NVIDIA/TensorRT-LLM/pull/10232) | changes_requested: 1 | 1 | 2.0d |
| [#10227](https://github.com/NVIDIA/TensorRT-LLM/pull/10227) | None | 1 | 12.9d |
| [#10225](https://github.com/NVIDIA/TensorRT-LLM/pull/10225) | changes_requested: 1 | 1 | 7.0d |
| [#10224](https://github.com/NVIDIA/TensorRT-LLM/pull/10224) | None | 1 | 32m |
| [#10219](https://github.com/NVIDIA/TensorRT-LLM/pull/10219) | None | 1 | 3.2d |
| [#10212](https://github.com/NVIDIA/TensorRT-LLM/pull/10212) | None | 1 | 8.3d |
| [#10210](https://github.com/NVIDIA/TensorRT-LLM/pull/10210) | None | 1 | 1.4h |
| [#10209](https://github.com/NVIDIA/TensorRT-LLM/pull/10209) | None | 1 | 10.6h |
| [#10206](https://github.com/NVIDIA/TensorRT-LLM/pull/10206) | None | 1 | 13.2d |
| [#10192](https://github.com/NVIDIA/TensorRT-LLM/pull/10192) | None | 1 | 21.5d |
| [#10190](https://github.com/NVIDIA/TensorRT-LLM/pull/10190) | None | 1 | 13.8d |
| [#10189](https://github.com/NVIDIA/TensorRT-LLM/pull/10189) | None | 1 | 1.1d |
| [#10187](https://github.com/NVIDIA/TensorRT-LLM/pull/10187) | None | 1 | 31.1d |
| [#10184](https://github.com/NVIDIA/TensorRT-LLM/pull/10184) | None | 1 | 44m |
| [#10177](https://github.com/NVIDIA/TensorRT-LLM/pull/10177) | None | 1 | 2.5d |
| [#10175](https://github.com/NVIDIA/TensorRT-LLM/pull/10175) | None | 1 | 1.6d |
| [#10173](https://github.com/NVIDIA/TensorRT-LLM/pull/10173) | None | 1 | 1.2d |
| [#10169](https://github.com/NVIDIA/TensorRT-LLM/pull/10169) | None | 1 | 16.9d |
| [#10166](https://github.com/NVIDIA/TensorRT-LLM/pull/10166) | None | 1 | 14.7d |
| [#10155](https://github.com/NVIDIA/TensorRT-LLM/pull/10155) | None | 1 | 2.7d |
| [#10154](https://github.com/NVIDIA/TensorRT-LLM/pull/10154) | None | 1 | 8.6d |
| [#10152](https://github.com/NVIDIA/TensorRT-LLM/pull/10152) | None | 1 | 6.3d |
| [#10150](https://github.com/NVIDIA/TensorRT-LLM/pull/10150) | None | 1 | 17.9d |
| [#10149](https://github.com/NVIDIA/TensorRT-LLM/pull/10149) | None | 1 | 2.9d |
| [#10146](https://github.com/NVIDIA/TensorRT-LLM/pull/10146) | None | 1 | 18.2d |
| [#10136](https://github.com/NVIDIA/TensorRT-LLM/pull/10136) | None | 1 | 4.3d |
| [#10135](https://github.com/NVIDIA/TensorRT-LLM/pull/10135) | None | 1 | 3.8h |
| [#10132](https://github.com/NVIDIA/TensorRT-LLM/pull/10132) | None | 1 | 13.9h |
| [#10131](https://github.com/NVIDIA/TensorRT-LLM/pull/10131) | None | 1 | 1.1d |
| [#10120](https://github.com/NVIDIA/TensorRT-LLM/pull/10120) | None | 1 | 4.6d |
| [#10114](https://github.com/NVIDIA/TensorRT-LLM/pull/10114) | None | 1 | 1.0d |
| [#10113](https://github.com/NVIDIA/TensorRT-LLM/pull/10113) | None | 1 | 18.7d |
| [#10112](https://github.com/NVIDIA/TensorRT-LLM/pull/10112) | None | 1 | 3.3d |
| [#10111](https://github.com/NVIDIA/TensorRT-LLM/pull/10111) | None | 1 | 25.6d |
| [#10090](https://github.com/NVIDIA/TensorRT-LLM/pull/10090) | None | 1 | 3.7d |
| [#10082](https://github.com/NVIDIA/TensorRT-LLM/pull/10082) | None | 1 | 12.9d |
| [#10077](https://github.com/NVIDIA/TensorRT-LLM/pull/10077) | None | 1 | 1.0h |
| [#10075](https://github.com/NVIDIA/TensorRT-LLM/pull/10075) | None | 1 | 29.3d |
| [#10068](https://github.com/NVIDIA/TensorRT-LLM/pull/10068) | None | 1 | 53m |
| [#10067](https://github.com/NVIDIA/TensorRT-LLM/pull/10067) | None | 1 | 4.5d |
| [#10060](https://github.com/NVIDIA/TensorRT-LLM/pull/10060) | None | 1 | 14.9d |
| [#10055](https://github.com/NVIDIA/TensorRT-LLM/pull/10055) | None | 1 | 8.8d |
| [#10049](https://github.com/NVIDIA/TensorRT-LLM/pull/10049) | None | 1 | 23.4d |
| [#10045](https://github.com/NVIDIA/TensorRT-LLM/pull/10045) | None | 1 | 1.2d |
| [#10042](https://github.com/NVIDIA/TensorRT-LLM/pull/10042) | None | 1 | 2.2d |
| [#10035](https://github.com/NVIDIA/TensorRT-LLM/pull/10035) | None | 1 | 3.0d |
| [#10028](https://github.com/NVIDIA/TensorRT-LLM/pull/10028) | None | 1 | 4.4d |
| [#10027](https://github.com/NVIDIA/TensorRT-LLM/pull/10027) | None | 1 | 3.7d |
| [#10026](https://github.com/NVIDIA/TensorRT-LLM/pull/10026) | None | 1 | 1.0d |
| [#10025](https://github.com/NVIDIA/TensorRT-LLM/pull/10025) | None | 1 | 2.0d |
| [#10023](https://github.com/NVIDIA/TensorRT-LLM/pull/10023) | None | 1 | 9.1h |
| [#10021](https://github.com/NVIDIA/TensorRT-LLM/pull/10021) | None | 1 | 3.0d |
| [#10020](https://github.com/NVIDIA/TensorRT-LLM/pull/10020) | None | 1 | 10.1h |
| [#10012](https://github.com/NVIDIA/TensorRT-LLM/pull/10012) | None | 1 | 20.6d |
| [#10011](https://github.com/NVIDIA/TensorRT-LLM/pull/10011) | None | 1 | 8.7d |
| [#10008](https://github.com/NVIDIA/TensorRT-LLM/pull/10008) | None | 1 | 1.1d |
| [#10005](https://github.com/NVIDIA/TensorRT-LLM/pull/10005) | None | 1 | 4.4d |
| [#10000](https://github.com/NVIDIA/TensorRT-LLM/pull/10000) | None | 1 | 3.8d |
| [#9998](https://github.com/NVIDIA/TensorRT-LLM/pull/9998) | None | 1 | 21.4d |
| [#9993](https://github.com/NVIDIA/TensorRT-LLM/pull/9993) | None | 1 | 3.0d |
| [#9992](https://github.com/NVIDIA/TensorRT-LLM/pull/9992) | None | 1 | 1.0d |
| [#9989](https://github.com/NVIDIA/TensorRT-LLM/pull/9989) | None | 1 | 1.9d |
| [#9982](https://github.com/NVIDIA/TensorRT-LLM/pull/9982) | None | 1 | 28m |
| [#9978](https://github.com/NVIDIA/TensorRT-LLM/pull/9978) | None | 1 | 17.4h |
| [#9977](https://github.com/NVIDIA/TensorRT-LLM/pull/9977) | None | 1 | 1.4d |
| [#9972](https://github.com/NVIDIA/TensorRT-LLM/pull/9972) | None | 1 | 1.5d |
| [#9971](https://github.com/NVIDIA/TensorRT-LLM/pull/9971) | None | 1 | 8.1d |
| [#9963](https://github.com/NVIDIA/TensorRT-LLM/pull/9963) | None | 1 | 30.7d |
| [#9958](https://github.com/NVIDIA/TensorRT-LLM/pull/9958) | None | 1 | 9.4d |
| [#9957](https://github.com/NVIDIA/TensorRT-LLM/pull/9957) | None | 1 | 3.0d |
| [#9952](https://github.com/NVIDIA/TensorRT-LLM/pull/9952) | None | 1 | 5.6h |
| [#9949](https://github.com/NVIDIA/TensorRT-LLM/pull/9949) | None | 1 | 9.8d |
| [#9946](https://github.com/NVIDIA/TensorRT-LLM/pull/9946) | None | 1 | 2.9d |
| [#9945](https://github.com/NVIDIA/TensorRT-LLM/pull/9945) | None | 1 | 9.9h |
| [#9944](https://github.com/NVIDIA/TensorRT-LLM/pull/9944) | None | 1 | 3.3d |
| [#9939](https://github.com/NVIDIA/TensorRT-LLM/pull/9939) | None | 1 | 12.1d |
| [#9936](https://github.com/NVIDIA/TensorRT-LLM/pull/9936) | None | 1 | 58m |
| [#9935](https://github.com/NVIDIA/TensorRT-LLM/pull/9935) | None | 1 | 3.1d |
| [#9914](https://github.com/NVIDIA/TensorRT-LLM/pull/9914) | None | 1 | 3.4d |
| [#9911](https://github.com/NVIDIA/TensorRT-LLM/pull/9911) | None | 1 | 11.1d |
| [#9910](https://github.com/NVIDIA/TensorRT-LLM/pull/9910) | None | 1 | 11.4d |
| [#9908](https://github.com/NVIDIA/TensorRT-LLM/pull/9908) | None | 1 | 11.3d |
| [#9906](https://github.com/NVIDIA/TensorRT-LLM/pull/9906) | None | 1 | 6.7d |
| [#9905](https://github.com/NVIDIA/TensorRT-LLM/pull/9905) | None | 1 | 34.6d |
| [#9904](https://github.com/NVIDIA/TensorRT-LLM/pull/9904) | None | 1 | 6.2h |
| [#9897](https://github.com/NVIDIA/TensorRT-LLM/pull/9897) | None | 1 | 13.8d |
| [#9896](https://github.com/NVIDIA/TensorRT-LLM/pull/9896) | None | 1 | 1.1d |
| [#9895](https://github.com/NVIDIA/TensorRT-LLM/pull/9895) | None | 1 | 1.1d |
| [#9894](https://github.com/NVIDIA/TensorRT-LLM/pull/9894) | None | 1 | 1.0d |
| [#9892](https://github.com/NVIDIA/TensorRT-LLM/pull/9892) | None | 1 | 20.9h |
| [#9888](https://github.com/NVIDIA/TensorRT-LLM/pull/9888) | None | 1 | 42.6d |
| [#9886](https://github.com/NVIDIA/TensorRT-LLM/pull/9886) | None | 1 | 20.5h |
| [#9881](https://github.com/NVIDIA/TensorRT-LLM/pull/9881) | None | 1 | 2.2d |
| [#9879](https://github.com/NVIDIA/TensorRT-LLM/pull/9879) | None | 1 | 36.0d |
| [#9873](https://github.com/NVIDIA/TensorRT-LLM/pull/9873) | None | 1 | 29.8d |
| [#9870](https://github.com/NVIDIA/TensorRT-LLM/pull/9870) | None | 1 | 35.0d |
| [#9863](https://github.com/NVIDIA/TensorRT-LLM/pull/9863) | None | 1 | 5.5h |
| [#9860](https://github.com/NVIDIA/TensorRT-LLM/pull/9860) | None | 1 | 1.0d |
| [#9843](https://github.com/NVIDIA/TensorRT-LLM/pull/9843) | None | 1 | 1.7d |
| [#9838](https://github.com/NVIDIA/TensorRT-LLM/pull/9838) | None | 1 | 27.8d |
| [#9837](https://github.com/NVIDIA/TensorRT-LLM/pull/9837) | None | 1 | 20.1h |
| [#9834](https://github.com/NVIDIA/TensorRT-LLM/pull/9834) | None | 1 | 3.4d |
| [#9833](https://github.com/NVIDIA/TensorRT-LLM/pull/9833) | None | 1 | 2.9d |
| [#9823](https://github.com/NVIDIA/TensorRT-LLM/pull/9823) | None | 1 | 1.1d |
| [#9817](https://github.com/NVIDIA/TensorRT-LLM/pull/9817) | None | 1 | 3.0h |
| [#9816](https://github.com/NVIDIA/TensorRT-LLM/pull/9816) | None | 1 | 1.0d |
| [#9815](https://github.com/NVIDIA/TensorRT-LLM/pull/9815) | None | 1 | 1.2h |
| [#9814](https://github.com/NVIDIA/TensorRT-LLM/pull/9814) | None | 1 | 10.3d |
| [#9808](https://github.com/NVIDIA/TensorRT-LLM/pull/9808) | None | 1 | 44.4d |
| [#9801](https://github.com/NVIDIA/TensorRT-LLM/pull/9801) | None | 1 | 1.2d |
| [#9797](https://github.com/NVIDIA/TensorRT-LLM/pull/9797) | None | 1 | 1.2d |
| [#9788](https://github.com/NVIDIA/TensorRT-LLM/pull/9788) | None | 1 | 1.0d |
| [#9783](https://github.com/NVIDIA/TensorRT-LLM/pull/9783) | None | 1 | 18.6h |
| [#9780](https://github.com/NVIDIA/TensorRT-LLM/pull/9780) | None | 1 | 4.9d |
| [#9775](https://github.com/NVIDIA/TensorRT-LLM/pull/9775) | None | 1 | 6.0h |
| [#9773](https://github.com/NVIDIA/TensorRT-LLM/pull/9773) | None | 1 | 27m |
| [#9771](https://github.com/NVIDIA/TensorRT-LLM/pull/9771) | None | 1 | 1.1d |
| [#9770](https://github.com/NVIDIA/TensorRT-LLM/pull/9770) | None | 1 | 18.5h |
| [#9769](https://github.com/NVIDIA/TensorRT-LLM/pull/9769) | None | 1 | 2.3h |
| [#9765](https://github.com/NVIDIA/TensorRT-LLM/pull/9765) | None | 1 | 11.7h |
| [#9764](https://github.com/NVIDIA/TensorRT-LLM/pull/9764) | None | 1 | 5.4d |
| [#9761](https://github.com/NVIDIA/TensorRT-LLM/pull/9761) | None | 1 | 39.4d |
| [#9758](https://github.com/NVIDIA/TensorRT-LLM/pull/9758) | None | 1 | 16.5d |
| [#9757](https://github.com/NVIDIA/TensorRT-LLM/pull/9757) | None | 1 | 6.7d |
| [#9755](https://github.com/NVIDIA/TensorRT-LLM/pull/9755) | None | 1 | 14.2h |
| [#9746](https://github.com/NVIDIA/TensorRT-LLM/pull/9746) | None | 1 | 5.5d |
| [#9745](https://github.com/NVIDIA/TensorRT-LLM/pull/9745) | None | 1 | 1.5d |
| [#9743](https://github.com/NVIDIA/TensorRT-LLM/pull/9743) | None | 1 | 2.7d |
| [#9741](https://github.com/NVIDIA/TensorRT-LLM/pull/9741) | None | 1 | 2.6d |
| [#9736](https://github.com/NVIDIA/TensorRT-LLM/pull/9736) | None | 1 | 6.7d |
| [#9735](https://github.com/NVIDIA/TensorRT-LLM/pull/9735) | None | 1 | 16.7d |
| [#9731](https://github.com/NVIDIA/TensorRT-LLM/pull/9731) | changes_requested: 1 | 1 | 5.7d |
| [#9724](https://github.com/NVIDIA/TensorRT-LLM/pull/9724) | None | 1 | 3.0d |
| [#9720](https://github.com/NVIDIA/TensorRT-LLM/pull/9720) | None | 1 | 8.2d |
| [#9710](https://github.com/NVIDIA/TensorRT-LLM/pull/9710) | changes_requested: 1 | 1 | 11.3d |
| [#9700](https://github.com/NVIDIA/TensorRT-LLM/pull/9700) | None | 1 | 4.9d |
| [#9690](https://github.com/NVIDIA/TensorRT-LLM/pull/9690) | None | 1 | 4.0d |
| [#9689](https://github.com/NVIDIA/TensorRT-LLM/pull/9689) | None | 1 | 12.0d |
| [#9686](https://github.com/NVIDIA/TensorRT-LLM/pull/9686) | None | 1 | 4.3d |
| [#9672](https://github.com/NVIDIA/TensorRT-LLM/pull/9672) | None | 1 | 41.7d |
| [#9667](https://github.com/NVIDIA/TensorRT-LLM/pull/9667) | None | 1 | 16.1h |
| [#9665](https://github.com/NVIDIA/TensorRT-LLM/pull/9665) | None | 1 | 4.2h |
| [#9663](https://github.com/NVIDIA/TensorRT-LLM/pull/9663) | None | 1 | 58m |
| [#9662](https://github.com/NVIDIA/TensorRT-LLM/pull/9662) | None | 1 | 1.2d |
| [#9661](https://github.com/NVIDIA/TensorRT-LLM/pull/9661) | None | 1 | 5.2d |
| [#9660](https://github.com/NVIDIA/TensorRT-LLM/pull/9660) | None | 1 | 6.0d |
| [#9659](https://github.com/NVIDIA/TensorRT-LLM/pull/9659) | None | 1 | 5.7d |
| [#9650](https://github.com/NVIDIA/TensorRT-LLM/pull/9650) | None | 1 | 7.9d |
| [#9638](https://github.com/NVIDIA/TensorRT-LLM/pull/9638) | None | 1 | 1.4h |
| [#9633](https://github.com/NVIDIA/TensorRT-LLM/pull/9633) | None | 1 | 4.0h |
| [#9627](https://github.com/NVIDIA/TensorRT-LLM/pull/9627) | None | 1 | 8.2d |
| [#9622](https://github.com/NVIDIA/TensorRT-LLM/pull/9622) | None | 1 | 22.3h |
| [#9621](https://github.com/NVIDIA/TensorRT-LLM/pull/9621) | None | 1 | 13.2d |
| [#9614](https://github.com/NVIDIA/TensorRT-LLM/pull/9614) | None | 1 | 6.9d |
| [#9613](https://github.com/NVIDIA/TensorRT-LLM/pull/9613) | None | 1 | 1.3d |
| [#9610](https://github.com/NVIDIA/TensorRT-LLM/pull/9610) | None | 1 | 14.8d |
| [#9605](https://github.com/NVIDIA/TensorRT-LLM/pull/9605) | None | 1 | 49m |
| [#9604](https://github.com/NVIDIA/TensorRT-LLM/pull/9604) | None | 1 | 13.1d |
| [#9599](https://github.com/NVIDIA/TensorRT-LLM/pull/9599) | None | 1 | 17.5h |
| [#9597](https://github.com/NVIDIA/TensorRT-LLM/pull/9597) | None | 1 | 17.4h |
| [#9594](https://github.com/NVIDIA/TensorRT-LLM/pull/9594) | None | 1 | 4.3d |
| [#9592](https://github.com/NVIDIA/TensorRT-LLM/pull/9592) | None | 1 | 4.7d |
| [#9585](https://github.com/NVIDIA/TensorRT-LLM/pull/9585) | None | 1 | 1.0d |
| [#9581](https://github.com/NVIDIA/TensorRT-LLM/pull/9581) | None | 1 | 1.6h |
| [#9580](https://github.com/NVIDIA/TensorRT-LLM/pull/9580) | None | 1 | 21.0h |
| [#9579](https://github.com/NVIDIA/TensorRT-LLM/pull/9579) | None | 1 | 9.2h |
| [#9578](https://github.com/NVIDIA/TensorRT-LLM/pull/9578) | None | 1 | 23.6h |
| [#9575](https://github.com/NVIDIA/TensorRT-LLM/pull/9575) | None | 1 | 1.9d |
| [#9571](https://github.com/NVIDIA/TensorRT-LLM/pull/9571) | None | 1 | 43m |
| [#9569](https://github.com/NVIDIA/TensorRT-LLM/pull/9569) | None | 1 | 7.4h |
| [#9568](https://github.com/NVIDIA/TensorRT-LLM/pull/9568) | None | 1 | 1.1h |
| [#9566](https://github.com/NVIDIA/TensorRT-LLM/pull/9566) | None | 1 | 12.9h |
| [#9561](https://github.com/NVIDIA/TensorRT-LLM/pull/9561) | None | 1 | 23.4h |
| [#9553](https://github.com/NVIDIA/TensorRT-LLM/pull/9553) | None | 1 | 23m |
| [#9552](https://github.com/NVIDIA/TensorRT-LLM/pull/9552) | None | 1 | 1.6d |
| [#9544](https://github.com/NVIDIA/TensorRT-LLM/pull/9544) | None | 1 | 2.9d |
| [#9543](https://github.com/NVIDIA/TensorRT-LLM/pull/9543) | None | 1 | 2.7d |
| [#9541](https://github.com/NVIDIA/TensorRT-LLM/pull/9541) | None | 1 | 14.3d |
| [#9540](https://github.com/NVIDIA/TensorRT-LLM/pull/9540) | None | 1 | 5.6d |
| [#9539](https://github.com/NVIDIA/TensorRT-LLM/pull/9539) | None | 1 | 40m |
| [#9537](https://github.com/NVIDIA/TensorRT-LLM/pull/9537) | None | 1 | 4.8h |
| [#9535](https://github.com/NVIDIA/TensorRT-LLM/pull/9535) | None | 1 | 4.9d |
| [#9534](https://github.com/NVIDIA/TensorRT-LLM/pull/9534) | None | 1 | 2.9d |
| [#9533](https://github.com/NVIDIA/TensorRT-LLM/pull/9533) | None | 1 | 3.1h |
| [#9522](https://github.com/NVIDIA/TensorRT-LLM/pull/9522) | None | 1 | 2.2d |
| [#9520](https://github.com/NVIDIA/TensorRT-LLM/pull/9520) | None | 1 | 5.8d |
| [#9518](https://github.com/NVIDIA/TensorRT-LLM/pull/9518) | None | 1 | 5.5h |
| [#9512](https://github.com/NVIDIA/TensorRT-LLM/pull/9512) | None | 1 | 10.9d |
| [#9510](https://github.com/NVIDIA/TensorRT-LLM/pull/9510) | None | 1 | 6.3d |
| [#9508](https://github.com/NVIDIA/TensorRT-LLM/pull/9508) | None | 1 | 3.0h |
| [#9505](https://github.com/NVIDIA/TensorRT-LLM/pull/9505) | None | 1 | 2.9h |
| [#9502](https://github.com/NVIDIA/TensorRT-LLM/pull/9502) | None | 1 | 1.3h |
| [#9500](https://github.com/NVIDIA/TensorRT-LLM/pull/9500) | None | 1 | 4.9d |
| [#9497](https://github.com/NVIDIA/TensorRT-LLM/pull/9497) | None | 1 | 4.6d |
| [#9475](https://github.com/NVIDIA/TensorRT-LLM/pull/9475) | None | 1 | 14.4d |
| [#9472](https://github.com/NVIDIA/TensorRT-LLM/pull/9472) | None | 1 | 23.6h |
| [#9459](https://github.com/NVIDIA/TensorRT-LLM/pull/9459) | None | 1 | 19.7d |
| [#9457](https://github.com/NVIDIA/TensorRT-LLM/pull/9457) | None | 1 | 3.3h |
| [#9455](https://github.com/NVIDIA/TensorRT-LLM/pull/9455) | None | 1 | 11.0h |
| [#9443](https://github.com/NVIDIA/TensorRT-LLM/pull/9443) | None | 1 | 1.8d |
| [#9441](https://github.com/NVIDIA/TensorRT-LLM/pull/9441) | None | 1 | 2.8d |
| [#9429](https://github.com/NVIDIA/TensorRT-LLM/pull/9429) | None | 1 | 1.5h |
| [#9428](https://github.com/NVIDIA/TensorRT-LLM/pull/9428) | None | 1 | 6.2d |
| [#9427](https://github.com/NVIDIA/TensorRT-LLM/pull/9427) | None | 1 | 7.8h |
| [#9422](https://github.com/NVIDIA/TensorRT-LLM/pull/9422) | None | 1 | 1.8d |
| [#9416](https://github.com/NVIDIA/TensorRT-LLM/pull/9416) | None | 1 | 7.1h |
| [#9411](https://github.com/NVIDIA/TensorRT-LLM/pull/9411) | None | 1 | 1.1d |
| [#9410](https://github.com/NVIDIA/TensorRT-LLM/pull/9410) | None | 1 | 2.6d |
| [#9405](https://github.com/NVIDIA/TensorRT-LLM/pull/9405) | None | 1 | 2.9d |
| [#9404](https://github.com/NVIDIA/TensorRT-LLM/pull/9404) | None | 1 | 7.2h |
| [#9400](https://github.com/NVIDIA/TensorRT-LLM/pull/9400) | None | 1 | 1.2h |
| [#9396](https://github.com/NVIDIA/TensorRT-LLM/pull/9396) | None | 1 | 9.8d |
| [#9395](https://github.com/NVIDIA/TensorRT-LLM/pull/9395) | None | 1 | 1.0d |
| [#9392](https://github.com/NVIDIA/TensorRT-LLM/pull/9392) | None | 1 | 9.1d |
| [#9389](https://github.com/NVIDIA/TensorRT-LLM/pull/9389) | None | 1 | 21.5h |
| [#9386](https://github.com/NVIDIA/TensorRT-LLM/pull/9386) | None | 1 | 4.0d |
| [#9381](https://github.com/NVIDIA/TensorRT-LLM/pull/9381) | None | 1 | 1.6d |
| [#9371](https://github.com/NVIDIA/TensorRT-LLM/pull/9371) | None | 1 | 4.6d |
| [#9369](https://github.com/NVIDIA/TensorRT-LLM/pull/9369) | None | 1 | 2.3d |
| [#9367](https://github.com/NVIDIA/TensorRT-LLM/pull/9367) | None | 1 | 18.8d |
| [#9353](https://github.com/NVIDIA/TensorRT-LLM/pull/9353) | None | 1 | 20.6d |
| [#9347](https://github.com/NVIDIA/TensorRT-LLM/pull/9347) | None | 1 | 4.0d |
| [#9336](https://github.com/NVIDIA/TensorRT-LLM/pull/9336) | None | 1 | 3.8d |
| [#9333](https://github.com/NVIDIA/TensorRT-LLM/pull/9333) | None | 1 | 10.7d |
| [#9331](https://github.com/NVIDIA/TensorRT-LLM/pull/9331) | None | 1 | 3.3d |
| [#9330](https://github.com/NVIDIA/TensorRT-LLM/pull/9330) | None | 1 | 7.1d |
| [#9329](https://github.com/NVIDIA/TensorRT-LLM/pull/9329) | None | 1 | 3.6d |
| [#9325](https://github.com/NVIDIA/TensorRT-LLM/pull/9325) | None | 1 | 4.5d |
| [#9322](https://github.com/NVIDIA/TensorRT-LLM/pull/9322) | None | 1 | 5.0d |
| [#9320](https://github.com/NVIDIA/TensorRT-LLM/pull/9320) | None | 1 | 5.2h |
| [#9307](https://github.com/NVIDIA/TensorRT-LLM/pull/9307) | None | 1 | 11.6d |
| [#9297](https://github.com/NVIDIA/TensorRT-LLM/pull/9297) | None | 1 | 6.3d |
| [#9292](https://github.com/NVIDIA/TensorRT-LLM/pull/9292) | None | 1 | 8.1d |
| [#9262](https://github.com/NVIDIA/TensorRT-LLM/pull/9262) | None | 1 | 13.7d |
| [#9261](https://github.com/NVIDIA/TensorRT-LLM/pull/9261) | None | 1 | 13.8d |
| [#9224](https://github.com/NVIDIA/TensorRT-LLM/pull/9224) | None | 1 | 8.5d |
| [#9211](https://github.com/NVIDIA/TensorRT-LLM/pull/9211) | None | 1 | 10.9d |
| [#9185](https://github.com/NVIDIA/TensorRT-LLM/pull/9185) | None | 1 | 19.7d |
| [#9167](https://github.com/NVIDIA/TensorRT-LLM/pull/9167) | None | 1 | 50.9d |
| [#9157](https://github.com/NVIDIA/TensorRT-LLM/pull/9157) | None | 1 | 12.9d |
| [#9140](https://github.com/NVIDIA/TensorRT-LLM/pull/9140) | None | 1 | 18.1d |
| [#9138](https://github.com/NVIDIA/TensorRT-LLM/pull/9138) | None | 1 | 43.2d |
| [#9128](https://github.com/NVIDIA/TensorRT-LLM/pull/9128) | None | 1 | 22.1d |
| [#9093](https://github.com/NVIDIA/TensorRT-LLM/pull/9093) | None | 1 | 13.0d |
| [#9089](https://github.com/NVIDIA/TensorRT-LLM/pull/9089) | None | 1 | 7.7d |
| [#9077](https://github.com/NVIDIA/TensorRT-LLM/pull/9077) | None | 1 | 19.8d |
| [#9060](https://github.com/NVIDIA/TensorRT-LLM/pull/9060) | None | 1 | 50.1d |
| [#8999](https://github.com/NVIDIA/TensorRT-LLM/pull/8999) | None | 1 | 20.3d |
| [#8963](https://github.com/NVIDIA/TensorRT-LLM/pull/8963) | None | 1 | 25.9d |
| [#8956](https://github.com/NVIDIA/TensorRT-LLM/pull/8956) | None | 1 | 59.7d |
| [#8919](https://github.com/NVIDIA/TensorRT-LLM/pull/8919) | None | 1 | 34.1d |
| [#8902](https://github.com/NVIDIA/TensorRT-LLM/pull/8902) | None | 1 | 27.9d |
| [#8889](https://github.com/NVIDIA/TensorRT-LLM/pull/8889) | None | 1 | 28.8d |
| [#8861](https://github.com/NVIDIA/TensorRT-LLM/pull/8861) | None | 1 | 25.9d |
| [#8800](https://github.com/NVIDIA/TensorRT-LLM/pull/8800) | None | 1 | 38.4d |
| [#8795](https://github.com/NVIDIA/TensorRT-LLM/pull/8795) | None | 1 | 16.6h |
| [#8794](https://github.com/NVIDIA/TensorRT-LLM/pull/8794) | None | 1 | 7.8d |
| [#8714](https://github.com/NVIDIA/TensorRT-LLM/pull/8714) | None | 1 | 37.8d |
| [#8691](https://github.com/NVIDIA/TensorRT-LLM/pull/8691) | None | 1 | 7.6d |
| [#8609](https://github.com/NVIDIA/TensorRT-LLM/pull/8609) | None | 1 | 8.5h |
| [#8576](https://github.com/NVIDIA/TensorRT-LLM/pull/8576) | None | 1 | 2.8h |
| [#8538](https://github.com/NVIDIA/TensorRT-LLM/pull/8538) | None | 1 | 6.9d |
| [#8509](https://github.com/NVIDIA/TensorRT-LLM/pull/8509) | None | 1 | 42.1d |
| [#8383](https://github.com/NVIDIA/TensorRT-LLM/pull/8383) | None | 1 | 54.5d |
| [#8368](https://github.com/NVIDIA/TensorRT-LLM/pull/8368) | None | 1 | 73.3d |
| [#8309](https://github.com/NVIDIA/TensorRT-LLM/pull/8309) | None | 1 | 66.8d |
| [#8279](https://github.com/NVIDIA/TensorRT-LLM/pull/8279) | changes_requested: 1 | 1 | 103.5d |
| [#8216](https://github.com/NVIDIA/TensorRT-LLM/pull/8216) | None | 1 | 20.1d |
| [#8194](https://github.com/NVIDIA/TensorRT-LLM/pull/8194) | None | 1 | 41.4d |
| [#8018](https://github.com/NVIDIA/TensorRT-LLM/pull/8018) | None | 1 | 39.7d |
| [#8000](https://github.com/NVIDIA/TensorRT-LLM/pull/8000) | None | 1 | 25.7d |
| [#7846](https://github.com/NVIDIA/TensorRT-LLM/pull/7846) | None | 1 | 77.3d |
| [#7838](https://github.com/NVIDIA/TensorRT-LLM/pull/7838) | None | 1 | 76.8d |
| [#7808](https://github.com/NVIDIA/TensorRT-LLM/pull/7808) | None | 1 | 4.7d |
| [#7539](https://github.com/NVIDIA/TensorRT-LLM/pull/7539) | None | 1 | 42.0d |
| [#7439](https://github.com/NVIDIA/TensorRT-LLM/pull/7439) | None | 1 | 142.9d |
| [#7387](https://github.com/NVIDIA/TensorRT-LLM/pull/7387) | None | 1 | 17.8d |
| [#6973](https://github.com/NVIDIA/TensorRT-LLM/pull/6973) | None | 1 | 6.4d |
| [#6393](https://github.com/NVIDIA/TensorRT-LLM/pull/6393) | possible_title_format_issue: 1 | 1 | 1.8d |
| [#6146](https://github.com/NVIDIA/TensorRT-LLM/pull/6146) | None | 1 | 2.0d |
| [#6097](https://github.com/NVIDIA/TensorRT-LLM/pull/6097) | None | 1 | 57.7d |
| [#4265](https://github.com/NVIDIA/TensorRT-LLM/pull/4265) | None | 1 | 5.2d |

---

*This report was automatically generated by analyzing GitHub PR data.*