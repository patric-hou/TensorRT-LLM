#!/usr/bin/env python3
"""
GitHub PR流程完整分析工具

这个工具提供了对GitHub仓库PR流程的全面分析，包括：
1. 随机采样PR
2. 采集详细数据（包括Review状态）
3. CI检查分析（check-runs + statuses）
4. **关键改进：分析comments中的CI失败信息**
5. 生成综合分析报告

关键教训：
- GitHub的check-runs和status API只能捕获部分CI结果
- Jenkins等外部CI系统通常通过comments报告结果
- 必须分析comments才能获得完整的CI失败信息

使用方法：
    python3 pr_flow_analyzer.py --repo OWNER/REPO --sample-size 1500 --ci-depth 500

作者: Claude Code
版本: 2.0 (修正版 - 包含comment分析)
日期: 2026-01-27
"""

import json
import urllib.request
import time
import re
import argparse
import sys
from datetime import datetime
from collections import defaultdict, Counter
import random

# ============================================================================
# 配置和常量
# ============================================================================

CI_FAILURE_KEYWORDS = [
    'FAILURE',
    'failed',
    'status: FAILED',
    'completed with status',
    'pipeline.*failed',
    'job.*failed',
    'FAIL',
    'ERROR'
]

# ============================================================================
# 工具函数
# ============================================================================

def fetch_url(url, timeout=15):
    """获取URL内容，带重试"""
    max_retries = 3
    for i in range(max_retries):
        try:
            req = urllib.request.Request(url)
            req.add_header('Accept', 'application/vnd.github.v3+json')
            req.add_header('User-Agent', 'PR-Flow-Analyzer/2.0')
            with urllib.request.urlopen(req, timeout=timeout) as response:
                data = json.loads(response.read().decode())
                headers = dict(response.headers)
                return data, headers
        except Exception as e:
            if i == max_retries - 1:
                print(f"❌ 请求失败: {url[:60]}... - {str(e)}")
                return None, None
            time.sleep(2)
    return None, None

def check_rate_limit(headers):
    """检查API限制并在需要时暂停"""
    if headers and 'X-RateLimit-Remaining' in headers:
        remaining = int(headers['X-RateLimit-Remaining'])
        if remaining < 200:
            print(f"\n⚠️  API限制剩余 {remaining} 次，暂停60秒...")
            time.sleep(60)

# ============================================================================
# Phase 1: 采样PR
# ============================================================================

def sample_prs(repo, sample_size, output_file):
    """随机采样指定数量的已合并PR"""
    print("=" * 80)
    print(f"Phase 1: 随机采样 {sample_size} 个已合并的PR")
    print("=" * 80)
    print()

    owner, repo_name = repo.split('/')

    # 收集所有已合并的PR
    all_prs = []
    page = 1

    while len(all_prs) < 5000:  # 最多收集5000个
        url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls?state=closed&per_page=100&page={page}"
        data, headers = fetch_url(url)

        if not data:
            break

        merged_prs = [pr for pr in data if pr.get('merged_at')]
        all_prs.extend(merged_prs)

        print(f"  已收集: {len(all_prs)} 个merged PR (页码: {page})")

        if len(merged_prs) < 100:
            break

        page += 1
        time.sleep(0.5)

    print()
    print(f"✓ 共收集到 {len(all_prs)} 个已合并的PR")
    print()

    # 随机采样
    random.seed(42)
    sample_size = min(sample_size, len(all_prs))
    sampled = random.sample(all_prs, sample_size)

    # 保存基础信息
    basic_info = [
        {
            'number': pr['number'],
            'title': pr['title'],
            'created_at': pr['created_at'],
            'merged_at': pr['merged_at'],
            'user': pr['user']['login'],
            'html_url': pr['html_url']
        }
        for pr in sampled
    ]

    with open(output_file, 'w') as f:
        json.dump(basic_info, f, indent=2)

    print(f"✓ 已保存 {len(basic_info)} 个PR到 {output_file}")
    return basic_info

# ============================================================================
# Phase 2: 采集详细数据（包括Review）
# ============================================================================

def collect_detailed_data(repo, sampled_prs, output_file):
    """采集PR的详细数据，包括Review状态"""
    print("=" * 80)
    print(f"Phase 2: 采集 {len(sampled_prs)} 个PR的详细数据")
    print("=" * 80)
    print()

    owner, repo_name = repo.split('/')
    detailed_prs = []

    for i, pr_basic in enumerate(sampled_prs, 1):
        pr_num = pr_basic['number']

        if i % 50 == 0:
            print(f"  进度: {i}/{len(sampled_prs)} ({i/len(sampled_prs)*100:.1f}%)")

        # 获取PR详情
        pr_url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls/{pr_num}"
        pr_data, headers = fetch_url(pr_url)

        if not pr_data:
            continue

        detailed_pr = {
            'number': pr_num,
            'title': pr_data['title'],
            'user': pr_data['user']['login'],
            'created_at': pr_data['created_at'],
            'merged_at': pr_data['merged_at'],
            'commits': pr_data.get('commits', 0),
            'additions': pr_data.get('additions', 0),
            'deletions': pr_data.get('deletions', 0),
            'changed_files': pr_data.get('changed_files', 0),
            'comments': pr_data.get('comments', 0),
            'review_comments': pr_data.get('review_comments', 0),
        }

        # 采集Review状态
        time.sleep(0.3)
        review_url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls/{pr_num}/reviews"
        reviews_data, _ = fetch_url(review_url)

        if reviews_data:
            changes_requested = sum(1 for r in reviews_data if r.get('state') == 'CHANGES_REQUESTED')
            approved = sum(1 for r in reviews_data if r.get('state') == 'APPROVED')

            detailed_pr['review_changes_requested_count'] = changes_requested
            detailed_pr['review_approved_count'] = approved
            detailed_pr['review_has_changes_requested'] = changes_requested > 0
            detailed_pr['review_total_count'] = len(reviews_data)
        else:
            detailed_pr['review_changes_requested_count'] = 0
            detailed_pr['review_approved_count'] = 0
            detailed_pr['review_has_changes_requested'] = False
            detailed_pr['review_total_count'] = 0

        # 计算合并时间
        if detailed_pr['created_at'] and detailed_pr['merged_at']:
            created = datetime.fromisoformat(detailed_pr['created_at'].replace('Z', '+00:00'))
            merged = datetime.fromisoformat(detailed_pr['merged_at'].replace('Z', '+00:00'))
            detailed_pr['time_to_merge_hours'] = (merged - created).total_seconds() / 3600
        else:
            detailed_pr['time_to_merge_hours'] = None

        detailed_prs.append(detailed_pr)

        check_rate_limit(headers)
        time.sleep(0.3)

    with open(output_file, 'w') as f:
        json.dump(detailed_prs, f, indent=2)

    print()
    print(f"✓ 已保存 {len(detailed_prs)} 个PR的详细数据到 {output_file}")
    return detailed_prs

# ============================================================================
# Phase 3: CI检查分析（check-runs + statuses）
# ============================================================================

def analyze_ci_checks(repo, sampled_prs, output_file):
    """分析PR的CI检查（check-runs和statuses）"""
    print("=" * 80)
    print(f"Phase 3: 分析 {len(sampled_prs)} 个PR的CI检查")
    print("=" * 80)
    print()

    owner, repo_name = repo.split('/')
    ci_data = []

    for i, pr_basic in enumerate(sampled_prs, 1):
        pr_num = pr_basic['number']

        if i % 25 == 0:
            print(f"  进度: {i}/{len(sampled_prs)} ({i/len(sampled_prs)*100:.1f}%)")

        # 获取PR的head SHA
        pr_url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls/{pr_num}"
        pr_data, _ = fetch_url(pr_url)

        if not pr_data:
            continue

        head_sha = pr_data.get('head', {}).get('sha')
        if not head_sha:
            continue

        time.sleep(0.3)

        # 获取check runs
        checks_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits/{head_sha}/check-runs"
        checks_data, headers = fetch_url(checks_url)

        check_runs = []
        if checks_data and 'check_runs' in checks_data:
            for check in checks_data['check_runs']:
                check_runs.append({
                    'name': check.get('name', ''),
                    'status': check.get('status', ''),
                    'conclusion': check.get('conclusion', '')
                })

        time.sleep(0.3)

        # 获取statuses
        status_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits/{head_sha}/status"
        status_data, _ = fetch_url(status_url)

        statuses = []
        if status_data and 'statuses' in status_data:
            for status in status_data['statuses']:
                statuses.append({
                    'context': status.get('context', ''),
                    'state': status.get('state', '')
                })

        ci_data.append({
            'pr_number': pr_num,
            'head_sha': head_sha,
            'check_runs': check_runs,
            'statuses': statuses
        })

        check_rate_limit(headers)
        time.sleep(0.3)

    with open(output_file, 'w') as f:
        json.dump(ci_data, f, indent=2)

    print()
    print(f"✓ 已保存 {len(ci_data)} 个PR的CI检查数据到 {output_file}")
    return ci_data

# ============================================================================
# Phase 4: 分析Comments中的CI失败（关键改进！）
# ============================================================================

def analyze_comments_ci_failures(repo, sampled_prs, output_file):
    """
    分析comments中的CI失败信息

    这是关键改进！很多CI系统（如Jenkins）通过comments报告结果，
    而不是通过GitHub的check-runs或status API。
    """
    print("=" * 80)
    print(f"Phase 4: 分析 {len(sampled_prs)} 个PR的Comments中的CI失败")
    print("=" * 80)
    print()
    print("⚠️  这是关键步骤！遗漏这一步会导致直接合入率被严重高估！")
    print()

    owner, repo_name = repo.split('/')
    comment_analysis = []

    for i, pr_basic in enumerate(sampled_prs, 1):
        pr_num = pr_basic['number']

        if i % 25 == 0:
            print(f"  进度: {i}/{len(sampled_prs)} ({i/len(sampled_prs)*100:.1f}%)")

        # 获取comments
        comments_url = f"https://api.github.com/repos/{owner}/{repo_name}/issues/{pr_num}/comments"
        comments_data, headers = fetch_url(comments_url)

        if not comments_data:
            continue

        # 分析comments中的CI状态
        has_ci_failure = False
        ci_failure_messages = []

        for comment in comments_data:
            body = comment.get('body', '')

            # 检查是否包含CI失败信息
            for keyword in CI_FAILURE_KEYWORDS:
                if re.search(keyword, body, re.IGNORECASE):
                    # 进一步检查是否真的是失败（排除SUCCESS）
                    if 'FAILURE' in body or ('failed' in body.lower() and 'SUCCESS' not in body):
                        has_ci_failure = True
                        # 提取失败信息
                        lines = body.split('\n')
                        for line in lines:
                            if 'FAILURE' in line or 'failed' in line.lower():
                                ci_failure_messages.append(line.strip()[:200])
                                break
                        break

        comment_analysis.append({
            'pr_number': pr_num,
            'total_comments': len(comments_data),
            'has_ci_failure_in_comments': has_ci_failure,
            'ci_failure_count': len(ci_failure_messages),
            'sample_messages': ci_failure_messages[:3]
        })

        check_rate_limit(headers)
        time.sleep(0.4)

    with open(output_file, 'w') as f:
        json.dump(comment_analysis, f, indent=2)

    has_failure_count = sum(1 for item in comment_analysis if item['has_ci_failure_in_comments'])

    print()
    print(f"✓ 已保存 {len(comment_analysis)} 个PR的comment分析到 {output_file}")
    print(f"✓ 发现 {has_failure_count} 个PR在comments中有CI失败 ({has_failure_count/len(comment_analysis)*100:.1f}%)")
    print()

    return comment_analysis

# ============================================================================
# Phase 5: 综合分析和分类
# ============================================================================

def comprehensive_analysis(detailed_prs, ci_data, comment_analysis):
    """综合分析，正确分类PR"""
    print("=" * 80)
    print("Phase 5: 综合分析和PR分类")
    print("=" * 80)
    print()

    # 创建字典
    pr_dict = {pr['number']: pr for pr in detailed_prs}
    ci_dict = {item['pr_number']: item for item in ci_data}
    comment_dict = {item['pr_number']: item for item in comment_analysis}

    direct_merge = []
    blocked = []

    for pr_num in comment_dict.keys():
        if pr_num not in pr_dict or pr_num not in ci_dict:
            continue

        pr = pr_dict[pr_num]
        ci = ci_dict[pr_num]
        comment = comment_dict[pr_num]

        # 检查所有卡点
        bottlenecks = []

        # 1. Check-runs中的failure
        for check in ci['check_runs']:
            if check['conclusion'] == 'failure':
                bottlenecks.append(f"check:{check['name']}")

        # 2. Status中的failure
        if 'statuses' in ci:
            for status in ci['statuses']:
                if status['state'] in ['failure', 'error']:
                    bottlenecks.append(f"status:{status['context']}")

        # 3. Review Changes Requested
        if pr.get('review_has_changes_requested', False):
            bottlenecks.append(f"review")

        # 4. Comments中的CI failure（关键！）
        if comment['has_ci_failure_in_comments']:
            bottlenecks.append(f"comment_ci")

        pr_info = {
            'number': pr_num,
            'title': pr['title'],
            'user': pr['user'],
            'bottlenecks': bottlenecks,
            'merge_time_hours': pr.get('time_to_merge_hours', 0),
            'commits': pr.get('commits', 0)
        }

        if len(bottlenecks) == 0:
            direct_merge.append(pr_info)
        else:
            blocked.append(pr_info)

    total = len(direct_merge) + len(blocked)

    print(f"分析完成:")
    print(f"  - 直接合入: {len(direct_merge)} 个 ({len(direct_merge)/total*100:.1f}%)")
    print(f"  - 被阻塞: {len(blocked)} 个 ({len(blocked)/total*100:.1f}%)")
    print()

    # 卡点统计
    bottleneck_stats = {
        'check': 0,
        'status': 0,
        'review': 0,
        'comment_ci': 0
    }

    for pr in blocked:
        for b in pr['bottlenecks']:
            if b.startswith('check:'):
                bottleneck_stats['check'] += 1
            elif b.startswith('status:'):
                bottleneck_stats['status'] += 1
            elif b == 'review':
                bottleneck_stats['review'] += 1
            elif b == 'comment_ci':
                bottleneck_stats['comment_ci'] += 1

    print("卡点分布:")
    print(f"  - Check-runs失败: {bottleneck_stats['check']} ({bottleneck_stats['check']/len(blocked)*100:.1f}%)")
    print(f"  - Status失败: {bottleneck_stats['status']} ({bottleneck_stats['status']/len(blocked)*100:.1f}%)")
    print(f"  - Review Changes: {bottleneck_stats['review']} ({bottleneck_stats['review']/len(blocked)*100:.1f}%)")
    print(f"  - Comments中CI失败: {bottleneck_stats['comment_ci']} ({bottleneck_stats['comment_ci']/len(blocked)*100:.1f}%)")
    print()

    return {
        'direct_merge': direct_merge,
        'blocked': blocked,
        'direct_merge_rate': len(direct_merge)/total*100,
        'blocked_rate': len(blocked)/total*100,
        'bottleneck_stats': bottleneck_stats
    }

# ============================================================================
# 主函数
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description='GitHub PR流程完整分析工具 v2.0')
    parser.add_argument('--repo', required=True, help='仓库名称 (格式: owner/repo)')
    parser.add_argument('--sample-size', type=int, default=1500, help='采样PR数量 (默认: 1500)')
    parser.add_argument('--ci-depth', type=int, default=500, help='深度CI分析数量 (默认: 500)')
    parser.add_argument('--skip-phase', type=int, nargs='+', help='跳过的阶段 (1-5)')

    args = parser.parse_args()

    skip_phases = set(args.skip_phase) if args.skip_phase else set()

    print()
    print("=" * 80)
    print("GitHub PR流程完整分析工具 v2.0")
    print("=" * 80)
    print()
    print(f"仓库: {args.repo}")
    print(f"采样规模: {args.sample_size} 个PR")
    print(f"CI深度分析: {args.ci_depth} 个PR")
    print()
    print("关键改进: 包含comments中的CI失败分析")
    print("警告: 不分析comments会导致直接合入率被严重高估（可能高估50%+）")
    print()
    print("=" * 80)
    print()

    # 执行各阶段
    if 1 not in skip_phases:
        sampled_prs = sample_prs(args.repo, args.sample_size, 'sampled_prs.json')
    else:
        with open('sampled_prs.json', 'r') as f:
            sampled_prs = json.load(f)

    if 2 not in skip_phases:
        detailed_prs = collect_detailed_data(args.repo, sampled_prs, 'detailed_prs.json')
    else:
        with open('detailed_prs.json', 'r') as f:
            detailed_prs = json.load(f)

    ci_sample = random.sample(sampled_prs, min(args.ci_depth, len(sampled_prs)))

    if 3 not in skip_phases:
        ci_data = analyze_ci_checks(args.repo, ci_sample, 'ci_checks.json')
    else:
        with open('ci_checks.json', 'r') as f:
            ci_data = json.load(f)

    if 4 not in skip_phases:
        comment_analysis = analyze_comments_ci_failures(args.repo, ci_sample, 'comments_ci.json')
    else:
        with open('comments_ci.json', 'r') as f:
            comment_analysis = json.load(f)

    if 5 not in skip_phases:
        results = comprehensive_analysis(detailed_prs, ci_data, comment_analysis)

        with open('analysis_results.json', 'w') as f:
            json.dump(results, f, indent=2)

        print("=" * 80)
        print("✓ 分析完成！")
        print("=" * 80)
        print()
        print(f"📊 关键指标:")
        print(f"  - 直接合入率: {results['direct_merge_rate']:.1f}%")
        print(f"  - 被阻塞率: {results['blocked_rate']:.1f}%")
        print()
        print("生成的文件:")
        print("  - sampled_prs.json: 采样的PR列表")
        print("  - detailed_prs.json: PR详细数据")
        print("  - ci_checks.json: CI检查数据")
        print("  - comments_ci.json: Comments中的CI失败")
        print("  - analysis_results.json: 最终分析结果")
        print()

if __name__ == '__main__':
    main()
