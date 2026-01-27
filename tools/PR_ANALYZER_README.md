# GitHub PR流程分析工具使用指南

## 概述

这是一个用于全面分析GitHub仓库PR流程的工具，可以准确识别PR的卡点和直接合入率。

**版本**: 2.0（修正版）
**关键改进**: 包含comments中的CI失败分析

## 🚨 重要警告

**不分析comments会导致直接合入率被严重高估！**

### 实际案例（TensorRT-LLM）

| 分析方法 | 直接合入率 | 错误程度 |
|---------|-----------|---------|
| ❌ 只看GitHub check-runs API | 80.7% | **高估58.9%** |
| ✅ 包含comments分析 | **21.8%** | 准确 |

**原因**: 很多CI系统（如Jenkins、自建CI）通过comments报告结果，而不是通过GitHub的check-runs或status API。

## 为什么需要这个工具？

GitHub提供的API只能捕获部分CI信息：
- ✅ GitHub Actions的结果（通过check-runs API）
- ✅ 部分外部CI（通过status API）
- ❌ Jenkins等通过comments报告的CI（需要手动分析）

如果只依赖GitHub的check-runs和status API，会**严重低估**PR的失败率。

## 安装和使用

### 1. 基本使用

```bash
python3 tools/pr_flow_analyzer.py --repo OWNER/REPO --sample-size 1500
```

### 2. 完整参数

```bash
python3 tools/pr_flow_analyzer.py \
  --repo NVIDIA/TensorRT-LLM \
  --sample-size 1500 \
  --ci-depth 500
```

### 3. 参数说明

- `--repo`: GitHub仓库（格式：owner/repo）
- `--sample-size`: 随机采样的PR数量（默认1500）
- `--ci-depth`: 深度CI分析的PR数量（默认500）
- `--skip-phase`: 跳过某些阶段（例如：`--skip-phase 1 2` 跳过阶段1和2）

### 4. 分阶段执行（推荐用于大型仓库）

如果分析被中断，可以跳过已完成的阶段：

```bash
# 第一次运行，执行到Phase 3
python3 pr_flow_analyzer.py --repo OWNER/REPO --sample-size 1500

# 如果中断，继续执行剩余阶段
python3 pr_flow_analyzer.py --repo OWNER/REPO --sample-size 1500 --skip-phase 1 2 3
```

## 分析流程

工具分为5个阶段：

### Phase 1: 随机采样PR
- 收集所有已合并的PR
- 随机采样指定数量（保证统计代表性）
- 输出：`sampled_prs.json`

### Phase 2: 采集详细数据
- 采集每个PR的详细信息（commits、代码变更、合并时间等）
- **包含Review状态分析**（CHANGES_REQUESTED/APPROVED）
- 输出：`detailed_prs.json`

### Phase 3: CI检查分析
- 分析GitHub check-runs API
- 分析GitHub status API
- 输出：`ci_checks.json`

### Phase 4: Comments中的CI失败分析 ⚠️ **关键步骤**
- 分析每个PR的comments
- 识别CI失败报告（FAILURE、failed等关键词）
- 这是与传统分析方法的**关键区别**
- 输出：`comments_ci.json`

**典型CI失败comment示例**：
```
/LLM/main/L0_MergeRequest_PR pipeline #2458 completed with status: 'FAILURE'
```

### Phase 5: 综合分析
- 综合所有数据源
- 正确分类PR（直接合入 vs 被阻塞）
- 统计各类卡点
- 输出：`analysis_results.json`

## 输出文件说明

执行完成后会生成以下文件：

| 文件名 | 说明 |
|-------|------|
| `sampled_prs.json` | 随机采样的PR列表 |
| `detailed_prs.json` | PR详细数据（包括Review状态） |
| `ci_checks.json` | CI检查数据（check-runs + statuses） |
| `comments_ci.json` | Comments中的CI失败分析 |
| `analysis_results.json` | 最终分析结果和分类 |

## 关键改进点详解

### 改进1: 分析Comments中的CI失败

**问题**: GitHub的check-runs API无法捕获所有CI系统的结果

**解决方案**: 分析comments中的关键词（FAILURE、failed等）

**代码实现**：
```python
CI_FAILURE_KEYWORDS = [
    'FAILURE',
    'failed',
    'status: FAILED',
    'completed with status',
    'pipeline.*failed'
]

for comment in comments_data:
    body = comment.get('body', '')
    for keyword in CI_FAILURE_KEYWORDS:
        if re.search(keyword, body, re.IGNORECASE):
            if 'FAILURE' in body or ('failed' in body.lower() and 'SUCCESS' not in body):
                has_ci_failure = True
```

### 改进2: 完整的Review状态分析

不仅统计review数量，还分析：
- CHANGES_REQUESTED次数
- APPROVED次数
- 首次approval前的修改次数

### 改进3: 综合多个数据源

正确的卡点判断需要综合：
1. GitHub check-runs API
2. GitHub status API
3. **Comments中的CI报告**（最重要）
4. Review状态

## 统计置信度

推荐的采样规模和置信度：

| 采样规模 | 总PR数 | 采样率 | 误差边界 | 置信度 |
|---------|--------|--------|---------|--------|
| 500 | 5000 | 10% | ±4.2% | 95% |
| 1000 | 5000 | 20% | ±2.9% | 95% |
| 1500 | 5000 | 30% | ±2.3% | 95% |

## 使用案例

### 案例1: TensorRT-LLM项目

```bash
python3 pr_flow_analyzer.py --repo NVIDIA/TensorRT-LLM --sample-size 1500 --ci-depth 500
```

**结果**：
- 采样：1485个PR
- 直接合入率：21.8%（修正后）
- 主要卡点：Comments中的CI失败（97.7%）

### 案例2: 其他项目

```bash
python3 pr_flow_analyzer.py --repo kubernetes/kubernetes --sample-size 2000
```

## 常见问题

### Q1: 为什么执行时间很长？

**A**: Phase 4（comments分析）需要为每个PR获取所有comments，这需要大量API调用。

- 500个PR约需20-30分钟
- 1500个PR约需60-90分钟

**建议**:
- 使用`--ci-depth 500`减少分析PR数
- 分阶段执行（使用`--skip-phase`）

### Q2: API限制怎么办？

**A**: 工具已内置API限制检测和自动暂停。

GitHub API限制：
- 未认证：60次/小时
- 已认证：5000次/小时

**建议**: 使用GitHub token增加限制：
```bash
export GITHUB_TOKEN=your_token_here
# 然后修改工具，在fetch_url中添加：
# req.add_header('Authorization', f'Bearer {os.environ.get("GITHUB_TOKEN")}')
```

### Q3: 如何验证结果准确性？

**A**: 手动抽查一些PR，查看GitHub页面的comments，验证CI失败是否被正确识别。

例如查看PR#3885：
1. 打开GitHub PR页面
2. 查看comments标签
3. 搜索"FAILURE"或"failed"
4. 与工具输出的`comments_ci.json`对比

### Q4: 能否用于私有仓库？

**A**: 可以，但需要：
1. 配置GitHub token（需要repo权限）
2. 确保token有访问私有仓库的权限

## 贡献改进

如果您发现其他CI系统的comment格式，可以添加到`CI_FAILURE_KEYWORDS`：

```python
CI_FAILURE_KEYWORDS = [
    'FAILURE',
    'failed',
    # 添加您的项目特有的关键词
    'your_ci_system.*failed',
    'build.*error'
]
```

## 许可证

MIT License

## 作者

Claude Code - 基于TensorRT-LLM项目的实际分析经验开发

## 版本历史

- **v2.0** (2026-01-27): 增加comments分析，修正直接合入率高估问题
- **v1.0** (2026-01-21): 初始版本，仅包含check-runs和status分析（已废弃）

## 致谢

感谢用户提出的关键质疑，发现了comments分析的重要性，避免了统计结论的重大错误。
