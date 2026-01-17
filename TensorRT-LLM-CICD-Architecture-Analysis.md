# TensorRT-LLM CI/CD 架构详细分析报告

**生成日期**: 2026-01-17
**项目**: NVIDIA TensorRT-LLM
**分析范围**: GitHub Workflows、Jenkins 配置、测试框架和完整 PR 流程

---

## 目录

1. [GitHub Workflows 文件清单](#1-github-workflows-文件清单)
2. [各 Workflow 详细分析](#2-各-workflow-详细分析)
3. [Jenkins 配置识别](#3-jenkins-配置识别)
4. [代码合入前的检查项分析](#4-代码合入前的检查项分析)
5. [完整的 PR 合入流程](#5-完整的-pr-合入流程)
6. [测试框架和测试策略](#6-测试框架和测试策略)
7. [架构总结](#7-架构总结)
8. [最佳实践建议](#8-最佳实践建议)

---

## 1. GitHub Workflows 文件清单

`.github/workflows` 目录包含以下 10 个 workflow 文件和 1 个配置文件：

### Workflow 文件

1. **auto-assign.yml** - 自动分配 issue
2. **auto-close-inactive-issues.yml** - 自动关闭不活跃的 issue
3. **blossom-ci.yml** - Blossom CI 触发器（核心 CI/CD 流程）
4. **bot-command.yml** - Bot 命令帮助信息
5. **l0-test.yml** - L0 测试结果上传
6. **label_community_pr.yml** - 社区 PR 自动标签
7. **label_issue.yml** - 新 issue 自动标签
8. **pr-check.yml** - PR 检查
9. **precommit-check.yml** - Pre-commit 检查
10. **waiting_for_feedback.yml** - 反馈等待标签管理

### 配置文件

- **module-owners.json** - 模块负责人配置

---

## 2. 各 Workflow 详细分析

### 2.1 核心 CI/CD Workflows

#### blossom-ci.yml (核心 CI 触发器)

**触发条件**:
- PR 评论创建时（`issue_comment.created`）
- 手动触发（`workflow_dispatch`）

**作用**:
这是项目的核心 CI/CD 触发器，实现混合基础设施（GitHub + 自托管 Jenkins）

**关键功能**:
- **授权检查**: 只有 350+ 授权用户（主要是 NVIDIA 员工）可以触发 CI
- **Bot 命令支持**:
  - `/bot run` - 启动构建/测试流程
  - `/bot skip --comment` - 跳过测试（需要理由）
  - `/bot reuse-pipeline` - 重用之前的流程
  - `/bot kill` - 终止运行中的构建

**流程步骤**:
1. **Authorization** - 验证用户权限
2. **Vulnerability-scan** - 漏洞扫描（使用 NVIDIA Blossom Action）
3. **Job-trigger** - 触发 Jenkins 任务
4. **Upload-Log** - 上传日志

---

#### pr-check.yml (PR 检查)

**触发条件**:
PR 打开、编辑、同步、重新打开时

**检查项**:

1. **PR 标题格式检查**:
   - 格式：`[票据ID][类型] 摘要`
   - 票据格式：
     - JIRA: `[TRTLLM-1234]`
     - NVBugs: `[https://nvbugs/1234567]`
     - GitHub Issue: `[#1234]`
     - 无票据: `[None]`
   - 类型（小写）：`[fix]`, `[feat]`, `[doc]`, `[infra]`, `[chore]` 等
   - 示例：`[TRTLLM-1234][feat] Add new feature`

2. **PR Checklist 检查**:
   - 验证 PR body 中是否包含 "## PR Checklist" 部分
   - 检查是否有未解决的 checklist 项
   - 当前 `ENFORCE_PR_HAS_CHECKLIST: false`（未强制执行）

---

#### precommit-check.yml (Release 检查)

**触发条件**:
- Pull request 事件
- 手动触发（可指定 commit SHA）

**作用**:
运行发布前检查脚本 `scripts/release_check.py`

**并发控制**:
同一分支/run 的检查会自动取消之前的运行

---

#### l0-test.yml (L0 测试结果处理)

**触发条件**:
仅通过 `workflow_dispatch` 手动触发

**作用**:
- 收集 Jenkins CI 的测试结果
- 创建测试摘要
- 更新 commit 状态为 `blossom-ci`
- 显示通过/失败/跳过的测试数量

---

### 2.2 Issue/PR 管理 Workflows

#### auto-assign.yml

**触发条件**: issue 被标记时

**作用**:
- 根据 `module-owners.json` 配置自动分配 issue 给相应模块负责人
- 只处理特定颜色标签（`#00611d` - 模块标签）
- 自动添加 "triaged" 和 "investigating" 标签

**模块负责人示例**:
- `Inference runtime`: funatiq, pcastonguay, Shixiaowei02, MartinMarciniszyn, schetlur-nv, dcampora
- `Low Precision`: Tracin, nv-guomingz, Naveassaf
- `Customized kernels`: lowsfer, PerkzZheng, jdemouth-nvidia
- [完整列表见 module-owners.json]

---

#### label_issue.yml

**触发条件**: 新 issue 创建时

**作用**:
- 使用 AI（NVIDIA Goggles Action）自动标记 issue
- 基于 issue 标题和内容自动分配合适的标签
- 排除的标签：bug, Community want to contribute, duplicate 等

---

#### label_community_pr.yml

**触发条件**:
- 每小时运行一次（cron: `0 * * * *`）
- 手动触发

**作用**:
为社区贡献者的 PR 添加 "Community want to contribute" 标签

---

#### auto-close-inactive-issues.yml

**触发条件**:
- 每天 UTC 3:00 运行（cron: `0 3 * * *`）
- 手动触发

**作用**:
- 对带有 "waiting for feedback" 标签且 14 天无更新的 issue/PR 标记为 stale
- 标记为 stale 后再 14 天无更新则自动关闭
- 运行配额：每次最多处理 1000 个 issues

---

#### waiting_for_feedback.yml

**触发条件**: issue/PR 评论创建时

**逻辑**:
- 作者回复 → 移除 "waiting for feedback" 标签
- NVIDIA 成员（非作者）评论 → 添加 "waiting for feedback" 标签
- 外部用户（非作者）评论 → 移除 "waiting for feedback" 标签
- 忽略 Bot 账户（如 tensorrt-cicd）

---

#### bot-command.yml

**触发条件**: 以 `/bot` 开头但不是标准命令的评论

**作用**: 显示 Bot 命令帮助信息

---

## 3. Jenkins 配置识别

### Jenkins Groovy 文件清单

位于 `jenkins/` 目录：

1. **L0_MergeRequest.groovy** (1362 行) - PR 合并请求的 L0 测试流程
2. **L0_Test.groovy** (177KB) - L0 测试执行配置
3. **Build.groovy** - 构建配置
4. **BuildDockerImage.groovy** - Docker 镜像构建
5. **GenerateLock.groovy** - 依赖锁文件生成
6. **controlCCache.groovy** - CCache 控制
7. **runPerfSanityTriage.groovy** - 性能回归测试

### Jenkins 与 GitHub Actions 的集成方式

**混合 CI/CD 架构（Blossom-CI）**:
- GitHub Actions 作为前端接口（授权、漏洞扫描）
- Jenkins 作为后端执行引擎（重型测试任务）
- 通过 Blossom-CI 框架连接两者

### 关键配置参数

来自 L0_MergeRequest.groovy：

```groovy
// 阶段选择
STAGE_CHOICE_NORMAL = "normal"
STAGE_CHOICE_SKIP = "skip"
STAGE_CHOICE_IGNORE = "ignore"

// Fail Fast 功能
- 默认启用（pre-merge）
- post-merge 始终禁用
- 可通过 --disable-fail-fast 禁用

// 测试过滤选项
- reuse_test: 重用之前的构建/测试结果
- skip_test: 跳过所有测试阶段
- stage_list: 只运行指定测试阶段
- gpu_type: 只在指定 GPU 类型上运行
- test_backend: 过滤测试后端 (pytorch, cpp, tensorrt, triton)
- post_merge: 运行 post-merge 流程
- debug: 调试模式（实验性）
```

---

## 4. 代码合入前的检查项分析

### 4.1 强制性检查项（必须通过才能合并）

#### GitHub Actions 层面

1. **PR 标题格式检查** (`pr-check.yml`)
   - 状态：**强制性**
   - 失败会导致 workflow 失败（`exit 1`）
   - 格式必须符合：`[票据ID][类型] 摘要`

2. **Pre-commit 检查** (`precommit-check.yml`)
   - 状态：**强制性**
   - 运行 `scripts/release_check.py`
   - 包括代码格式化和静态检查

3. **Blossom-CI 授权检查** (`blossom-ci.yml`)
   - 状态：**强制性**
   - 只有授权用户可以触发 CI
   - 未授权用户无法运行测试

4. **漏洞扫描** (`blossom-ci.yml`)
   - 状态：**强制性**
   - 在触发 Jenkins 任务前必须通过
   - 使用 NVIDIA Blossom Action 执行

#### Jenkins 层面（通过 Blossom-CI 触发）

5. **构建检查**
   - 多架构构建（x86_64, SBSA/ARM）
   - 多 OS 支持（Ubuntu, Rocky Linux 8）
   - 多 Python 版本（3.10, 3.12）

6. **L0 测试套件**
   - 单元测试（unittest 目录）
   - 集成测试（integration 目录）
   - C++ 运行时测试
   - 根据 GPU 类型分配：A10, A30, L40s, A100, H100, B200

7. **代码质量检查**（通过 pre-commit hooks）
   - `isort` - import 排序
   - `yapf` - Python 代码格式化
   - `clang-format` - C++ 代码格式化
   - `cmake-format` - CMake 文件格式化
   - `codespell` - 拼写检查
   - `ruff` - Python linting
   - `autoflake` - 未使用导入移除
   - `mdformat` - Markdown 格式化

8. **API 稳定性测试**
   - 位于 `tests/api_stability`
   - 检测受保护 API 的破坏性更改
   - 需要代码所有者审查批准

---

### 4.2 可以由 Maintainer 豁免的检查项

根据配置分析，以下检查可以被豁免：

1. **PR Checklist 检查**
   - 当前 `ENFORCE_PR_HAS_CHECKLIST: false`
   - 即使有未完成的 checklist，也不会阻止合并
   - 仅显示警告

2. **特定测试阶段** (通过 Bot 命令)
   - `/bot skip --comment "理由"` - 完全跳过测试
     - ⚠️ 标注为危险操作：可能导致主分支破坏
     - 需要提供跳过理由
     - **不会更新 GitHub check 状态**

   - `/bot run --skip-test` - 跳过测试但运行构建
     - 不更新 GitHub check 状态

   - `/bot run --stage-list "指定阶段"` - 只运行特定阶段
     - 不更新 GitHub check 状态

   - `/bot reuse-pipeline` - 重用之前的流程验证当前提交
     - ⚠️ 危险操作
     - 杀死所有当前运行的构建

3. **Fail Fast 功能**
   - `/bot run --disable-fail-fast` - 禁用快速失败
   - 即使有失败也继续运行所有测试

4. **Multi-GPU 测试**
   - 默认不在 pre-merge 运行
   - 可通过 `--add-multi-gpu-test` 强制运行
   - 可通过 `--disable-multi-gpu-test` 禁用

5. **特定 GPU 类型测试**
   - 可通过 `--gpu-type "A30, H100_PCIe"` 只在特定 GPU 上运行

---

### 4.3 检查状态更新规则

**只有在以下情况下才会更新 GitHub commit status**：

```groovy
enableUpdateGitlabStatus =
    !testFilter[ENABLE_SKIP_TEST] &&
    !testFilter[ONLY_MULTI_GPU_TEST] &&
    !testFilter[DISABLE_MULTI_GPU_TEST] &&
    !testFilter[DEBUG_MODE] &&
    testFilter[GPU_TYPE_LIST] == null &&
    testFilter[TEST_STAGE_LIST] == null &&
    testFilter[TEST_BACKEND] == null
```

即：运行完整的 L0 pre-merge 流程时才更新状态。部分运行不会反映在 GitHub 状态中。

---

## 5. 完整的 PR 合入流程

### 阶段 0：准备阶段（开发者本地）

1. **Fork 和克隆仓库**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_FORK.git TensorRT-LLM
   ```

2. **安装 pre-commit hooks**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

3. **开发和提交**
   - 本地开发修改
   - Pre-commit hooks 在每次 commit 时自动运行
   - 必须使用 `git commit -s` 签署 DCO（Developer Certificate of Origin）

---

### 阶段 1：创建 Pull Request

1. **推送到 fork 仓库**
   ```bash
   git push -u origin <local-branch>:<remote-branch>
   ```

2. **创建 PR**
   - 目标分支：通常为 `main`（除非 NVBug 指定特定版本分支）
   - PR 标题必须符合格式：`[票据ID][类型] 摘要`
   - PR 描述应包含：
     - 背景和动机
     - 变更摘要
     - 潜在影响
     - 相关 PR 链接

3. **自动触发的检查**：
   - ✅ `pr-check.yml` - PR 标题格式验证
   - ✅ `precommit-check.yml` - Release 检查
   - ✅ `label_issue.yml` - 自动标签（对 issue）
   - ✅ `label_community_pr.yml` - 社区 PR 标签
   - ✅ `auto-assign.yml` - 自动分配审查者（基于模块）

---

### 阶段 2：Code Review

1. **PR 状态变更**：
   - 创建时：无标签
   - 审查中：添加 "Pending Review" 标签
   - 需要修改：添加 "Changes Requested" 标签
   - 等待作者反馈：添加 "waiting for feedback" 标签

2. **审查者角色**：
   - 至少一位 TensorRT-LLM 工程师被分配审查
   - 对于 API 破坏性更改，需要 API 代码所有者审查
   - NVIDIA 开发者需要包含 JIRA/NVBug ID

---

### 阶段 3：CI 测试流程

#### 触发 CI（两种方式）

**方式 1：自动触发**
- 某些情况下自动触发（基于文件变更等）

**方式 2：手动触发（通过 Bot 命令）**

授权用户在 PR 评论中使用：

```bash
# 标准流程
/bot run

# 带选项的流程
/bot run --reuse-test                    # 重用之前的构建和测试结果
/bot run --disable-fail-fast             # 禁用快速失败
/bot run --add-multi-gpu-test            # 添加 multi-GPU 测试
/bot run --post-merge                    # 运行 post-merge 流程
/bot run --stage-list "A10-PyTorch-1"    # 只运行特定阶段
/bot run --gpu-type "A30, H100_PCIe"     # 只在特定 GPU 上运行
/bot run --detailed-log                  # 启用详细日志
```

---

#### CI 执行流程（Blossom-CI）

```
GitHub Actions (blossom-ci.yml)
    ↓
1. Authorization Check
   - 验证评论者在授权列表中（350+ 用户）
   - 非授权用户：停止
    ↓
2. Vulnerability Scan
   - 使用 NVIDIA Blossom Action
   - 扫描代码漏洞
   - 失败：停止
    ↓
3. Trigger Jenkins Job
   - 传递参数到 Jenkins
   - 启动对应的 Jenkins pipeline
    ↓
Jenkins (L0_MergeRequest.groovy)
    ↓
4. Build Stage
   - x86_64 构建 (Ubuntu, Rocky Linux 8)
   - SBSA/ARM 构建
   - 多 Python 版本 (3.10, 3.12)
   - 多容器镜像
    ↓
5. Test Stages (按 GPU 类型并行)

   L0 Pre-merge Tests:
   ├─ A10 Tests
   │  ├─ PyTorch tests
   │  ├─ CPP tests
   │  └─ TensorRT tests
   ├─ A30 Tests
   ├─ L40s Tests
   ├─ A100 Tests
   ├─ H100 Tests
   └─ B200 Tests (可选)

   Test Types:
   ├─ Unit Tests (tests/unittest/)
   │  - Python unittest/pytest
   │  - 小型、快速、功能特定
   ├─ Integration Tests (tests/integration/)
   │  - 完整工作流测试
   │  - 包括 checkpoint 转换、engine 构建、评估
   └─ C++ Runtime Tests
      - 使用 Google Test 框架
      - 通过 pytest 运行
    ↓
6. Collect Results
   - 收集所有测试结果 (XML 格式)
   - 上传到 Artifactory
    ↓
GitHub Actions (l0-test.yml)
    ↓
7. Process Test Results
   - 下载测试结果
   - 生成测试摘要
   - 更新 commit status 为 "blossom-ci"
   - 显示: X passed, Y failed, Z skipped
```

---

#### Test Stage 管理

测试用例分布在 `tests/integration/test_lists/test-db/` 下的 YAML 文件：
- `l0_a10.yml` - A10 GPU 测试列表
- `l0_a30.yml` - A30 GPU 测试列表
- `l0_h100.yml` - H100 GPU 测试列表
- 等等

每个文件定义：
- GPU 数量要求
- GPU 类型通配符
- 测试用例列表
- 可选的 TIMEOUT 和 ISOLATION 标记

---

### 阶段 4：处理 CI 失败

1. **如果 CI 失败**：
   - 开发者负责修复所有 CI 失败
   - 修复后推送新的 commit
   - 自动触发新的 CI 运行（或手动触发）

2. **调试选项**：
   ```bash
   /bot run --debug --stage-list "特定阶段"
   # 启用容器访问进行调试（实验性功能）
   ```

3. **重新运行选项**：
   ```bash
   /bot kill                    # 终止当前运行
   /bot run                     # 重新运行
   /bot run --reuse-test        # 重用成功的测试
   ```

---

### 阶段 5：批准和合并

1. **批准条件**：
   - ✅ 所有代码审查批准
   - ✅ 完整 CI 通过（blossom-ci status = success）
   - ✅ 没有合并冲突
   - ✅ DCO 签署检查通过
   - ✅ API 稳定性测试通过（如有 API 更改）

2. **特殊情况豁免**：
   - Maintainer 可以使用 `/bot skip --comment "理由"` 跳过测试
   - 但这被标记为**危险操作**，可能导致主分支问题

3. **合并**：
   - 审查者在 CI 通过后执行合并
   - 自动关闭相关 issue（如果有）

---

### 阶段 6：Post-merge 验证

- Post-merge pipeline 自动运行
- 更全面的测试套件
- Fail Fast 始终禁用
- 发现问题需要立即修复或回滚

---

## 6. 测试框架和测试策略

### 6.1 测试框架技术栈

#### Python 测试

- **主框架**: pytest
- **兼容**: Python unittest
- **插件**: requirements-dev.txt 中定义
- **运行方式**:
  ```bash
  pip install -e ./              # 可编辑安装
  pip install -r requirements-dev.txt
  cd tests/
  pytest <目标>
  ```

#### C++ 测试

- **框架**: Google Test (gtest)
- **运行方式**: 通过 pytest 调用 C++ 可执行文件
- **资源生成**: `cpp/tests/resources/` 脚本生成测试引擎

#### 性能测试

- **位置**: `tests/integration/`
- **目的**: QA 和 CI 中的性能回归检测
- **文档**: `tests/integration/README.md`

---

### 6.2 测试分层策略

#### L0 测试 (Level 0 - 基础测试)

**定义**: 快速、基础的功能验证

**分类**:

1. **Unit Tests** (`tests/unittest/`)
   - **特点**:
     - 小型、快速
     - 测试特定函数或类
     - 无需完整工作流
   - **示例**:
     - `unittest/trt/functional/test_*.py` - 功能测试
     - `unittest/trt/model_api/test_*.py` - 模型 API 测试

   - **CI 集成**:
     - 通过桥接机制 (`test_unittests.py`) 集成
     - 映射为 integration test 用例
     - 示例: `unittest/trt/attention/test_gpt_attention.py -k "partition0"`

2. **Integration Tests** (`tests/integration/defs/`)
   - **特点**:
     - 完整工作流测试
     - 包括 checkpoint 转换、engine 构建、评估
     - 验证功能和准确性

   - **子类别**:
     - `accuracy/` - 准确性测试
     - `disaggregated/` - 分离式服务测试
     - `cpp/` - C++ 端到端测试

   - **依赖**:
     - 需要 `LLM_MODELS_ROOT` 环境变量
     - 指向真实模型数据目录

3. **C++ Runtime Tests** (`cpp/tests/`)
   - **特点**:
     - 测试 C++ 运行时组件
     - 依赖 Python 前端生成引擎
   - **资源**: `cpp/tests/resources/scripts/`

**运行策略**:
- **Pre-merge**: 选择性运行（基于 GPU 类型）
- **Post-merge**: 更全面的覆盖
- **GPU 优先级**: A10 > A30 > L40s > A100 > H100 > B200

---

#### L1 测试 (Level 1 - 高级测试)

**定义**: 更长时间运行、更全面的测试

**运行时机**:
- Nightly 构建
- Stable 版本验证
- 自定义触发

**Jenkins 文件**:
- `L1_Custom`
- `L1_Nightly`
- `L1_Stable`

---

### 6.3 测试用例管理

#### Test Database

位置：`tests/integration/test_lists/test-db/`

结构示例：

```yaml
version: 0.0.1
l0_a10:
- condition:
    ranges:
      system_gpu_count:
        gte: 1
        lte: 1
    wildcards:
      gpu:
      - '*a10*'
      linux_distribution_name: ubuntu*
  tests:
  - test_path.py::test_function[param]
  - test_path.py::test_function[param] TIMEOUT (90)
  - test_path.py::test_function[param] ISOLATION
  - test_path.py::test_function[param] ISOLATION, TIMEOUT (120)
```

**标记说明**:
- `TIMEOUT (N)`: 超时限制（分钟）
- `ISOLATION`: 在独立 pytest 进程中运行
- 可组合使用（用逗号分隔）

---

#### 平台配置

jenkins/L0_Test.groovy 中的变量映射：

- `x86TestConfigs` - x86 平台测试配置
- `SBSATestConfigs` - SBSA/ARM 平台测试配置
- `x86SlurmTestConfigs` - x86 Slurm 集群配置
- `SBSASlurmTestConfigs` - SBSA Slurm 集群配置

---

### 6.4 测试执行策略

#### 并行策略

```
Build Stage (并行)
├─ x86_64 Ubuntu
├─ x86_64 Rocky Linux 8
└─ SBSA ARM

Test Stage (按 GPU 类型并行)
├─ A10 Tests
├─ A30 Tests
├─ L40s Tests
├─ A100 Tests
├─ H100 Tests
└─ B200 Tests
```

---

#### Fail Fast

- **Pre-merge**: 默认启用
  - 任何阶段失败立即停止
  - 可通过 `--disable-fail-fast` 禁用
- **Post-merge**: 始终禁用
  - 运行所有测试以获得完整视图

---

#### Test Reuse (优化策略)

- **默认行为**: 重用上次流程的构建和成功测试
- **条件**: Git commit ID 未更改
- **显式控制**:
  - `--reuse-test [pipeline-id]` - 重用指定流程
  - `--disable-reuse-test` - 禁用重用

---

#### Multi-GPU 测试策略

- **Pre-merge**: 默认不运行（资源考虑）
- **触发条件**:
  - 特定文件变更检测
  - 显式请求: `--add-multi-gpu-test`
- **Post-merge**: 包含在标准流程中

---

### 6.5 测试数据管理

#### 模型数据

- **环境变量**: `LLM_MODELS_ROOT`
- **结构**: 层次化子目录
  - 定义在 `integration/defs/conftest.py`
  - 示例: `bert_example_root`, `gpt2_root`
- **CI 环境**: NVIDIA 内部路径
- **本地测试**: 用户需自行准备和挂载

---

#### 测试结果

- **格式**: JUnit XML (`results*.xml`)
- **上传**: Jenkins → Artifactory
- **处理**: GitHub Actions (`l0-test.yml`)
  - 使用 `test-summary/action` 生成摘要
  - 更新 commit status

---

### 6.6 测试覆盖率策略

#### 按后端分类

```bash
--test-backend "pytorch, cpp"    # 只运行 pytorch 和 cpp 后端测试
```

支持的后端:
- `pytorch` - PyTorch 后端
- `cpp` - C++ 后端
- `tensorrt` - TensorRT 后端
- `triton` - Triton 后端

---

#### 按 GPU 类型

- **选择原则**: 选择满足需求的最便宜 GPU
- **优先级**: A10 > A30 > L40s > A100 > H100 > B200
- **重要测试**: 仅在一种 GPU 上运行（除非行为因 GPU 而异）

---

#### 隔离测试 (ISOLATION)

适用场景:
- 修改全局状态或环境变量
- 内存密集型操作
- 间歇性失败（仅在与其他测试一起运行时）
- 需要独占资源（GPU 内存、文件等）

---

### 6.7 本地测试指南

#### 运行 CI 阶段本地复现

```bash
# 1. 准备测试列表
cat > a10_list.txt <<EOF
disaggregated/test_disaggregated.py::test_basic[model]
accuracy/test_llm_api.py::test_accuracy[gpt2]
EOF

# 2. 运行测试
cd tests/integration/defs
pytest . --test-list="a10_list.txt" --output-dir=/tmp/llm_integration_test
```

---

#### 调试特定测试

```bash
# 运行单个测试
pytest "accuracy/test_llm_api_pytorch.py::TestLlama3_1_8B::test_auto_dtype"

# 运行匹配关键词的测试
pytest -k test_llm_gpt2_medium_bad_words_1gpu

# 运行匹配正则的测试
pytest -R ".*test_llm_gpt2_medium_bad_words_1gpu.*non.*py.*"

# 列出所有测试用例
pytest --co -q
pytest -k llmapi --co -q
```

---

### 6.8 代码质量保障

#### Pre-commit Hooks (自动执行)

```bash
# 安装
pip install pre-commit
pre-commit install

# 每次 commit 时自动运行:
- isort           # Import 排序
- yapf            # Python 格式化
- ruff            # Python linting + 格式化
- autoflake       # 移除未使用的导入
- clang-format    # C++ 格式化
- cmake-format    # CMake 格式化
- codespell       # 拼写检查
- mdformat        # Markdown 格式化
- 其他检查...
```

---

#### API 稳定性保护

- **位置**: `tests/api_stability`
- **目标**: 受保护的 API（LLM API 核心组件）
- **检测**: 签名更改、破坏性变更
- **流程**: 失败时需要 API 代码所有者审查

---

## 7. 架构总结

### 7.1 混合 CI/CD 模型

TensorRT-LLM 采用独特的**混合基础设施**架构：

```
External Interface (GitHub)
    ↓
GitHub Actions (轻量级任务)
├─ PR 验证
├─ 授权检查
├─ 漏洞扫描
└─ 结果处理
    ↓
Blossom-CI (桥接层)
    ↓
Jenkins (重型任务)
├─ 多平台构建
├─ GPU 测试
├─ 性能测试
└─ 集成测试
```

**优势**:
- ✅ 利用 GitHub Actions 的易用性和透明度
- ✅ 利用 Jenkins 对复杂工作流和自托管 runner 的控制
- ✅ 保护内部资源（GPU 集群）
- ✅ 灵活的测试策略（通过 Bot 命令）

---

### 7.2 质量门控机制

**多层防护**:

1. **本地开发**:
   - Pre-commit hooks
   - 本地测试

2. **PR 创建**:
   - 标题格式验证
   - Checklist 验证
   - 自动标签和分配

3. **代码审查**:
   - 人工审查
   - API 所有者审查（破坏性更改）

4. **CI 验证**:
   - 授权检查
   - 漏洞扫描
   - 构建验证
   - 多层次测试（L0 单元/集成/C++）
   - API 稳定性测试

5. **Post-merge 监控**:
   - 更全面的测试套件
   - 性能回归检测

---

### 7.3 关键特性

1. **灵活性**:
   - Bot 命令系统提供细粒度控制
   - 可选的测试过滤（GPU、后端、阶段）
   - 测试重用优化

2. **安全性**:
   - 授权用户列表（350+ NVIDIA 员工）
   - 漏洞扫描
   - DCO 签署要求

3. **效率**:
   - 并行构建和测试
   - Fail Fast 机制
   - 测试结果重用
   - 按 GPU 类型优先级分配

4. **可追溯性**:
   - 严格的 PR 标题格式（包含票据 ID）
   - 完整的测试结果上传
   - Commit status 更新

---

### 7.4 注意事项

⚠️ **危险操作**（需谨慎使用）:
- `/bot skip --comment` - 可能导致主分支破坏
- `/bot reuse-pipeline` - 未验证新代码

⚠️ **状态更新限制**:
- 部分运行（特定阶段/GPU）不更新 GitHub status
- 可能导致绿色 checkmark 但实际未完全测试

⚠️ **资源限制**:
- GPU 资源有限，优先级策略很重要
- 测试用例需手动维护在 YAML 文件中

---

## 8. 最佳实践建议

### 对于贡献者

1. **始终使用 pre-commit hooks** 避免格式问题
2. **遵循 PR 标题格式** 避免自动检查失败
3. **本地运行相关测试** 在推送前验证
4. **清晰的 commit 消息** 和 PR 描述
5. **及时响应审查意见** 避免 stale 标签

---

### 对于维护者

1. **谨慎使用豁免命令** (`/bot skip`)
2. **优先使用 `--reuse-test`** 优化 CI 时间
3. **根据变更范围选择测试策略**:
   - 小改动: 部分测试 + post-merge 验证
   - API 更改: 完整测试 + API 所有者审查
   - 性能优化: 包含性能测试
4. **更新测试数据库** 当添加新测试时
5. **监控 post-merge 结果** 及时发现问题

---

## 附录：常用命令速查

### Bot 命令

```bash
# 基本命令
/bot run                              # 标准 CI 流程
/bot kill                             # 终止当前运行
/bot skip --comment "理由"            # 跳过测试（危险）

# 测试优化
/bot run --reuse-test                 # 重用之前的结果
/bot run --disable-fail-fast          # 禁用快速失败

# 测试过滤
/bot run --gpu-type "A30, H100"       # 指定 GPU 类型
/bot run --stage-list "A10-PyTorch"   # 指定测试阶段
/bot run --test-backend "pytorch"     # 指定测试后端

# 特殊测试
/bot run --add-multi-gpu-test         # 添加 multi-GPU 测试
/bot run --post-merge                 # 运行 post-merge 流程
/bot run --debug                      # 调试模式
```

---

### 本地测试命令

```bash
# 安装依赖
pip install -e ./
pip install -r requirements-dev.txt

# 运行测试
pytest tests/                         # 运行所有测试
pytest -k test_name                   # 运行匹配的测试
pytest --co -q                        # 列出所有测试

# Pre-commit
pre-commit install                    # 安装 hooks
pre-commit run --all-files            # 手动运行所有 hooks
```

---

## 结论

TensorRT-LLM 项目采用了企业级的混合 CI/CD 方案，平衡了开源协作的透明度和内部资源管理的需求。通过多层次的质量门控、灵活的测试策略和完善的自动化流程，确保了代码质量和项目稳定性。

这个架构的核心优势在于：
- **混合基础设施**：结合 GitHub Actions 的易用性和 Jenkins 的强大能力
- **细粒度控制**：通过 Bot 命令系统提供灵活的测试选项
- **资源优化**：智能的 GPU 分配和测试重用机制
- **质量保障**：从本地开发到 post-merge 的全流程质量控制

---

**文档版本**: 1.0
**最后更新**: 2026-01-17
**分析工具**: Claude Code
