# GitHub Pull Request 完全指南 - 以PR #10795为例

本指南将详细讲解GitHub Pull Request（拉取请求）的每个组成部分，帮助你完全理解PR页面上的所有信息。

**示例PR**: https://github.com/NVIDIA/TensorRT-LLM/pull/10795

---

## 一、GitHub PR页面结构概览

```
┌─────────────────────────────────────────────────────────────────┐
│ 🔹 页面顶部导航                                                  │
│  - Code / Issues / Pull requests / Actions / ...                │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 📌 PR标题栏 (Header)                                             │
│  [None][infra] Waive failed case for release branch on 01/19   │
│  #10795 ⚫ Merged  👤 EmmaQiaoCh  🕒 merged 1 day ago           │
└─────────────────────────────────────────────────────────────────┘

┌──────────────────────┬──────────────────────────────────────────┐
│  🏷️ 左侧信息栏        │  📝 主内容区域                            │
│                      │                                          │
│  Reviewers           │  ▼ Description (PR描述)                  │
│  Assignees           │  ▼ Conversation (对话/Comments)          │
│  Labels              │  ▼ Commits (提交记录)                    │
│  Projects            │  ▼ Checks (CI/CD检查)                    │
│  Milestones          │  ▼ Files changed (文件变更)              │
│  Development         │                                          │
│                      │                                          │
└──────────────────────┴──────────────────────────────────────────┘
```

---

## 二、PR #10795的完整信息解析

### 📌 Part 1: PR标题栏（Header）

#### 【标题】
```
[None][infra] Waive failed case for release branch on 01/19
```

**解读**:
- `[None]` - JIRA ticket标记（这个PR没有关联JIRA ticket）
- `[infra]` - PR类型标记：基础设施/CI相关
- `Waive failed case...` - PR的简短描述：豁免某个失败的测试用例

**其他常见类型标记**:
- `[feat]` - 新功能
- `[fix]` - Bug修复
- `[doc]` - 文档更新
- `[chore]` - 杂项/维护任务
- `[test]` - 测试相关

---

#### 【PR编号和状态】
```
#10795  ⚫ Merged
```

**符号含义**:
- `#10795` - PR的唯一编号
- `⚫ Merged` - PR状态为"已合并"（紫色圆点图标）

**PR状态图标**:
| 图标 | 颜色 | 状态 | 含义 |
|-----|-----|-----|------|
| 🟢 `Open` | 绿色 | 打开 | PR正在审查中，尚未合并 |
| ⚫ `Merged` | 紫色 | 已合并 | PR已被合并到目标分支 |
| 🔴 `Closed` | 红色 | 已关闭 | PR被关闭但未合并（被拒绝或作废） |
| 🔄 `Draft` | 灰色 | 草稿 | PR仍在开发中，不准备审查 |

---

#### 【作者和时间信息】
```
👤 EmmaQiaoCh  merged 1 commit into main from release-branch  1 day ago
```

**解读**:
- **👤 EmmaQiaoCh** - PR的创建者和合并者
- **merged 1 commit** - 合并了1个commit
- **into main** - 目标分支是`main`
- **from release-branch** - 源分支是`release-branch`
- **1 day ago** - 合并时间（相对时间）

---

### 📝 Part 2: PR描述区域（Description）

这是PR创建者填写的描述内容。对于PR #10795:

```markdown
## Summary by CodeRabbit

* **Tests**
  * Updated test configuration to skip a specific test case pending resolution.
```

**包含内容**:
1. **Summary** - 总结这个PR做了什么
2. **Why** - 为什么需要这个改动
3. **How** - 如何实现的
4. **Test Coverage** - 如何测试
5. **Checklist** - PR提交检查清单

**特殊标记**:
- `<!-- -->` - HTML注释，不显示在页面上
- **CodeRabbit标记** - 这是由CodeRabbitAI机器人自动生成的摘要

---

### 💬 Part 3: Conversation区域（对话/评论）

这是PR的核心交流区域。让我逐条解析PR #10795的所有评论：

---

#### 【Comment 1】EmmaQiaoCh - PR作者的指令

```
📅 2026-01-19 05:02:15 (UTC)
👤 EmmaQiaoCh (PR作者)

/bot skip --comment "Waive failed cases for release branch"
```

**解读**:
- **发起人**: EmmaQiaoCh（PR作者本人）
- **内容类型**: Bot命令
- **作用**: 告诉CI机器人跳过测试（因为这个PR本身就是在添加测试豁免）
- **`/bot skip`**: 这是一个CI bot命令，类似于Slack的slash命令

**常见Bot命令**:
- `/bot run` - 触发CI运行
- `/bot skip` - 跳过CI测试
- `/bot retest` - 重新运行测试
- `/rebase` - 执行rebase操作

**关键词误判**:
- ❌ 我的脚本检测到"failed"就认为是CI失败
- ✅ 实际上这里的"failed cases"是指"要豁免的失败测试用例"，不是CI运行失败

---

#### 【Comment 2】coderabbitai[bot] - AI代码审查机器人

```
📅 2026-01-19 05:03:56 (UTC)
🤖 coderabbitai[bot] (自动化机器人)

📝 Walkthrough
📊 Changes
🎯 Estimated code review effort: 1 (Trivial) | ⏱️ ~2 minutes

🚥 Pre-merge checks | ✅ 2 | ❌ 1

❌ Failed checks (1 warning)
┌────────────────────┬──────────┬─────────────────────┐
│ Check name         │ Status   │ Explanation         │
├────────────────────┼──────────┼─────────────────────┤
│ Description check  │ ⚠️ Warning│ PR description is   │
│                    │          │ essentially empty   │
└────────────────────┴──────────┴─────────────────────┘

✅ Passed checks (2 passed)
- Title check ✅
- Docstring Coverage ✅
```

**解读**:
- **发起人**: coderabbitai[bot] - CodeRabbit AI自动审查机器人
- **作用**: 自动分析PR的代码变更并提供审查建议

**图标含义**:
- 📝 **Walkthrough** - 代码变更概览
- 🎯 **Effort** - 预估审查工作量（1-5分，1最简单）
- ⏱️ **Time** - 预估审查时间
- 🚥 **Pre-merge checks** - 合并前检查

**检查结果**:
1. ❌ **Description check - Warning**
   - 状态: ⚠️ 警告（不是错误）
   - 原因: PR描述太简单，几乎是空的
   - 影响: 不会阻止合并，只是提醒

2. ✅ **Title check - Passed**
   - PR标题格式正确：`[None][infra] ...`

3. ✅ **Docstring Coverage - Passed**
   - 没有需要添加文档字符串的函数

**关键词误判**:
- ❌ 我的脚本看到"Failed checks"就认为是CI失败
- ✅ 实际上这是CodeRabbit的**静态检查**，不是CI/CD流水线
- ✅ 而且只是"Warning"警告，不是真正的失败

---

#### 【Comment 3】tensorrt-cicd - CI机器人触发通知

```
📅 2026-01-19 05:10:04 (UTC)
🤖 tensorrt-cicd (CI/CD机器人)

[PR_Github #32517](内部链接) [ skip ] triggered by Bot. Commit: `477b78c`
```

**解读**:
- **发起人**: tensorrt-cicd - NVIDIA内部的CI/CD机器人
- **作用**: 通知CI流水线已触发

**详细信息**:
- **PR_Github #32517** - Jenkins内部构建编号
- **[ skip ]** - 执行模式：跳过测试
- **triggered by Bot** - 由Bot命令触发（响应Comment 1的`/bot skip`）
- **Commit: `477b78c`** - 对哪个commit执行CI

**链接**: `https://nv/trt-llm-cicd/job/helpers/job/PR_Github/32517/`
- 这是NVIDIA内部Jenkins链接（外部无法访问）

---

#### 【Comment 4】tensorrt-cicd - CI机器人完成通知

```
📅 2026-01-19 05:43:09 (UTC)
🤖 tensorrt-cicd (CI/CD机器人)

[PR_Github #32517](内部链接) [ skip ] completed with state `SUCCESS`. Commit: `477b78c`
Skipping testing for commit `477b78c`
```

**解读**:
- **发起人**: tensorrt-cicd
- **作用**: 报告CI执行结果

**关键信息**:
- **completed with state `SUCCESS`** - ✅ CI成功完成
- **[ skip ]** - 跳过模式（没有真正运行测试）
- **Skipping testing** - 说明跳过了测试

**这才是真正的CI状态报告！**
- ✅ 正确的CI失败格式应该是: `completed with state 'FAILURE'`
- ✅ 这里是`SUCCESS`，说明没有CI失败

---

### 🔍 Part 4: Checks标签页（CI/CD检查）

在PR页面顶部有几个标签：
```
[Conversation] [Commits] [Checks] ✓ [Files changed]
```

点击**Checks**标签可以看到所有CI/CD检查的详细信息。

**Checks页面包含**:
1. **GitHub Actions** - GitHub自带的CI/CD
2. **External Checks** - 第三方CI系统（如Jenkins、CircleCI）
3. **Required Checks** - 必须通过的检查
4. **Optional Checks** - 可选检查

**PR #10795的Checks**:
```
✅ All checks have passed (或 Some checks were skipped)
  ✓ Blossom-CI - skipped
  ✓ CodeRabbit - completed
```

**图标含义**:
- ✅ **绿色对勾** - 检查通过
- ❌ **红色叉号** - 检查失败
- 🟡 **黄色圆点** - 检查进行中
- ⚪ **灰色** - 检查被跳过或未运行
- ⏸️ **暂停图标** - 等待批准

---

### 📊 Part 5: Files changed标签页（文件变更）

```
[Files changed]  1 file  +1  -0
```

**解读**:
- **1 file** - 修改了1个文件
- **+1** - 新增1行
- **-0** - 删除0行

**文件变更详情**:
```diff
tests/integration/test_lists/waives.txt

@@ -123,3 +123,4 @@
 accuracy/test_llm_api.py::TestQwen2_72B_Instruct::test_auto_quantize_ammo[tp4] nvbugs#5818963 SKIP
 accuracy/test_llm_api.py::TestQwen2_72B_Instruct::test_fp8[tp4] nvbugs#5820155 SKIP
 accuracy/test_llm_api.py::TestLlama3_2_90B_Vision_Instruct::test_auto_dtype[tp4-1-cuda_graph=True] nvbugs#5820153 SKIP
+accuracy/test_llm_api_pytorch.py::TestLlama4ScoutInstruct::test_fp4[tp4-cuda_graph=True] nvbugs#5820734 SKIP
```

**Diff格式说明**:
- `@@` - 代码块位置标记
- `+` 绿色行 - 新增的内容
- `-` 红色行 - 删除的内容
- 白色行 - 未变更的上下文

**这个PR做了什么**:
在`waives.txt`文件末尾添加了1行，将一个测试用例标记为SKIP（跳过）。

---

### 🏷️ Part 6: 左侧信息栏

#### Reviewers（审查者）
```
🔍 No reviewers
```
- 这个PR没有指定审查者
- 通常会有"Request review"按钮

#### Assignees（分配者）
```
👤 EmmaQiaoCh (自我分配)
```
- PR被分配给谁处理

#### Labels（标签）
```
🏷️ 暂无标签
```
- 可以添加如：bug, enhancement, documentation等

#### Projects（项目）
```
📋 暂无关联项目
```
- 可以关联GitHub Projects看板

#### Milestones（里程碑）
```
🎯 暂无里程碑
```
- 可以关联发布版本，如：v1.0, v2.0

#### Development（开发）
```
🔗 暂无关联Issue
```
- 可以关联相关的Issue

---

### ⏱️ Part 7: Timeline（时间线）

GitHub会显示PR的完整时间线：

```
🕐 2026-01-19 05:01:48  👤 EmmaQiaoCh opened this pull request
🕐 2026-01-19 05:02:19  🔄 EmmaQiaoCh enabled auto-merge (squash)
🕐 2026-01-19 05:43:26  ⚫ EmmaQiaoCh merged commit 477b78c into main
🕐 2026-01-19 05:43:26  🔴 Closed
```

**事件类型**:
- **opened** - PR创建
- **committed** - 新增commit
- **review_requested** - 请求审查
- **reviewed** - 完成审查
- **approved** - 审查批准
- **changes_requested** - 要求修改
- **merged** - 合并
- **closed** - 关闭

---

## 三、CI/CD状态识别完整指南

### ✅ 如何判断CI是否失败

#### 正确的CI失败标记

**必须满足所有条件**:
1. ✅ 评论者是CI机器人：`tensorrt-cicd`, `blossomci`, `github-actions[bot]`
2. ✅ 包含明确的失败状态：`status: 'FAILURE'` 或 `state 'FAILURE'`
3. ✅ 通常包含流水线/作业编号

**示例** - 真正的CI失败：
```
tensorrt-cicd commented:

[PR_Github #12345](link) completed with status: 'FAILURE'. Commit: `abc1234`

Pipeline failed at stage: Integration Tests
Error: TestLlama3_8B::test_accuracy failed with exit code 1
```

**关键词**:
- `status: 'FAILURE'` ✅
- `state 'FAILURE'` ✅
- `completed with status: 'FAILED'` ✅
- `pipeline #XXXX failed` ✅

---

#### ❌ 常见误判案例

**Case 1: 修复失败测试的PR**
```
/bot skip --comment "Waive failed cases for release branch"
```
- 包含"failed"但不是CI失败
- 上下文是"waive failed cases"（豁免失败用例）

**Case 2: CodeRabbit的检查警告**
```
❌ Failed checks (1 warning)
Description check - ⚠️ Warning
```
- 包含"Failed checks"但不是CI失败
- 这是静态代码检查，不是CI/CD流水线
- 而且是"Warning"不是真正的failure

**Case 3: 讨论中提到失败**
```
This PR fixes the failed test in #10790
```
- 包含"failed"但只是在讨论中提及

---

### 📋 CI状态总结表

| 检查来源 | 真正的CI? | 示例 | 判断标准 |
|---------|----------|------|---------|
| **tensorrt-cicd** | ✅ 是 | `completed with status: 'FAILURE'` | 看status字段 |
| **blossomci** | ✅ 是 | `pipeline #123 failed` | 看pipeline状态 |
| **github-actions[bot]** | ✅ 是 | CI检查失败图标 | 看Checks标签页 |
| **CodeRabbitAI** | ❌ 否 | `Failed checks (1 warning)` | 静态分析，不是CI |
| **普通用户评论** | ❌ 否 | "Fix failed test" | 只是讨论 |
| **Bot命令** | ❌ 否 | `/bot skip --comment "waive failed"` | 命令，不是状态报告 |

---

## 四、PR #10795总结

### 完整流程

```
1. 👤 EmmaQiaoCh 创建PR
   ├─ 目的: 将1个失败的测试加入豁免列表
   └─ 修改: waives.txt +1行

2. 👤 EmmaQiaoCh 发送Bot命令
   └─ /bot skip (跳过CI测试)

3. 🤖 CodeRabbitAI 自动审查
   ├─ ✅ 标题格式正确
   ├─ ⚠️ 描述太简单（警告）
   └─ ✅ 无需docstring

4. 🤖 tensorrt-cicd 执行CI
   ├─ 触发: skip模式
   ├─ 结果: SUCCESS
   └─ 说明: 跳过了测试

5. 👤 EmmaQiaoCh 合并PR
   └─ 自动合并到main分支
```

### 真实CI状态

| 项目 | 值 |
|------|---|
| **CI运行次数** | 1次 (skip模式) |
| **CI失败次数** | 0次 |
| **CI状态** | ✅ SUCCESS |
| **真实阻塞** | 0次 |

### 我们检测的"2次阻塞"都是误判

1. **误判1**: EmmaQiaoCh的"failed cases" → 实际是命令参数
2. **误判2**: CodeRabbit的"Failed checks" → 实际是静态检查警告

---

## 五、GitHub PR关键概念总结

### 1. PR状态生命周期

```
Draft → Open → Reviewed → Approved → Merged → Closed
  ↓       ↓        ↓         ↓          ↓
 草稿    打开    已审查    已批准     已合并
```

### 2. 重要图标速查表

| 图标 | 含义 | 位置 |
|-----|------|------|
| 🟢 Open | PR打开中 | 标题旁 |
| ⚫ Merged | PR已合并 | 标题旁 |
| 🔴 Closed | PR已关闭未合并 | 标题旁 |
| ✅ | 检查通过 | Checks |
| ❌ | 检查失败 | Checks |
| 🟡 | 检查进行中 | Checks |
| ⚠️ | 警告 | Comments |
| 👤 | 用户 | 各处 |
| 🤖 | 机器人 | Comments |
| 💬 | 评论数 | 顶部 |
| 📝 | 文件变更 | Files |
| ➕ | 新增行数 | Files |
| ➖ | 删除行数 | Files |

### 3. 机器人类型

| 机器人名称 | 作用 | 可信度 |
|-----------|------|--------|
| **tensorrt-cicd** | NVIDIA CI/CD | ⭐⭐⭐⭐⭐ 完全可信 |
| **blossomci** | NVIDIA Blossom CI | ⭐⭐⭐⭐⭐ 完全可信 |
| **github-actions[bot]** | GitHub Actions | ⭐⭐⭐⭐⭐ 完全可信 |
| **coderabbitai[bot]** | AI代码审查 | ⭐⭐⭐ 参考 |
| **dependabot[bot]** | 依赖更新 | ⭐⭐⭐⭐ 可信 |

### 4. 评论命令（Bot Commands）

| 命令 | 作用 | 示例 |
|-----|------|------|
| `/bot run` | 触发CI | `/bot run` |
| `/bot skip` | 跳过CI | `/bot skip --comment "reason"` |
| `/bot retest` | 重新测试 | `/bot retest` |
| `/rebase` | Rebase PR | `/rebase` |
| `@coderabbitai` | 调用AI审查 | `@coderabbitai review` |

---

## 六、如何在GitHub上查看这些信息

### 访问PR #10795

1. **直接URL**: https://github.com/NVIDIA/TensorRT-LLM/pull/10795

2. **导航路径**:
   ```
   GitHub主页
   → NVIDIA/TensorRT-LLM仓库
   → Pull requests标签
   → 搜索#10795
   ```

### 查看不同部分

#### Conversation（对话）
- 默认视图
- 显示所有评论和事件

#### Commits（提交）
- 点击顶部"Commits"标签
- 查看: `477b78c` 这个commit的详情

#### Checks（检查）
- 点击顶部"Checks"标签
- 查看: CI/CD运行详情

#### Files changed（文件变更）
- 点击顶部"Files changed"标签
- 查看: diff（代码对比）

---

## 七、实战练习建议

### 如何准确识别CI失败

**检查清单**:
- [ ] 评论者是CI机器人？（tensorrt-cicd、blossomci）
- [ ] 包含明确的状态字段？（`status: 'FAILURE'`）
- [ ] 不是Bot命令？（不包含`/bot`前缀）
- [ ] 不是静态检查？（不是CodeRabbit等）
- [ ] 上下文合理？（不是"fix failed"、"waive failed"等讨论）

**如果5个都满足 → ✅ 这是真正的CI失败！**

---

## 八、改进建议

### 改进CI失败检测算法

**当前问题**:
```python
# ❌ 太宽泛
if 'failed' in comment.body.lower():
    ci_failures += 1
```

**改进后**:
```python
# ✅ 更精确
CI_BOT_USERS = ['tensorrt-cicd', 'blossomci', 'github-actions[bot]']
CI_FAILURE_PATTERNS = [
    r"completed with (?:status|state):\s*['\"]FAILURE['\"]",
    r"completed with (?:status|state):\s*['\"]FAILED['\"]",
    r"pipeline #\d+ (?:failed|FAILED)",
]

if comment.user in CI_BOT_USERS:
    for pattern in CI_FAILURE_PATTERNS:
        if re.search(pattern, comment.body):
            ci_failures += 1
            break
```

---

**报告生成时间**: 2026-01-27

**适用范围**: GitHub Pull Request通用知识

**参考PR**: NVIDIA/TensorRT-LLM#10795
