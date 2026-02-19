# Skill: 深度分析仓库 Pre-commit 检查规则

## 目标

分析一个仓库的 pre-commit 检查机制，产出一份包含以下内容的分析文档：
- 每条检查规则的功能描述
- 工具配置参数的含义
- 会导致检查失败的代码示例
- 排除规则的背景原因解释

---

## 第一步：定位配置文件

**寻找入口文件**：

```bash
# 主配置文件（几乎所有项目都有）
.pre-commit-config.yaml

# 工具配置（通常在这些文件中）
pyproject.toml       # Python 项目综合配置
setup.cfg            # 旧式 Python 配置
.clang-format        # C/C++ 格式化配置
.cmake-format.yaml   # CMake 格式化配置
.codespell.rc        # 拼写检查配置
```

**定位 repos 块**（`.pre-commit-config.yaml` 中 hooks 的位置通常不在文件开头，上面会有各种变量声明）：

```bash
grep -n "^repos:" .pre-commit-config.yaml
```

读取从该行号开始的内容，获取完整的 hook 列表。

---

## 第二步：提取关键信息

对每个 hook，需要记录：

| 字段 | 含义 |
|------|------|
| `repo` | 工具来源（GitHub 仓库或 `local`）|
| `rev` | 使用的版本 |
| `id` | hook 的标识符 |
| `files` | 仅处理匹配的文件 |
| `exclude` | 跳过匹配的文件（**重点分析**）|
| `args` | 传递给工具的参数 |
| `stages` | 触发阶段（`commit`、`commit-msg` 等）|
| `additional_dependencies` | 额外依赖 |

**特别关注 `exclude` 规则**：排除项背后往往有具体的技术原因（如自动生成文件、二进制数据），需要深入解释，不能只写"排除了 xxx 文件"。

---

## 第三步：分析 `exclude` 规则的原因

当看到某类文件被排除时，按以下步骤追查原因：

### 3.1 查找实际文件

```bash
# 找出被排除的文件
find . -name "*.cubin.cpp" | head -5
find . -name "*_cubin.h" | head -5
```

### 3.2 查看文件内容

```bash
# 看文件是什么格式（机器生成？二进制数据？）
head -20 <找到的文件>
```

### 3.3 判断生成来源

```bash
# 搜索生成这类文件的脚本
grep -r "cubin" scripts/ --include="*.py" -l
grep -r "gen_" . --include="*.py" -l | head -10
```

### 3.4 常见排除原因对照表

| 排除原因 | 典型特征 | 示例 |
|---------|---------|------|
| 自动生成文件 | 文件头有 "do not edit" / 内容是数值数组 | `*.cubin.cpp`（GPU 预编译二进制） |
| 二进制数据的 C++ 表示 | 大量十六进制数字 `0xABCD...` | 嵌入的字体、模型权重 |
| Git LFS 管理的大文件 | 文件内容只有3行 `oid sha256:...` | 模型文件、大型测试数据 |
| 旧式/遗留代码 | 有专门注释说明 | 第三方代码、未迁移的模块 |
| 平台差异文件 | 路径中有 `windows/` `compat/` 等 | 平台兼容层 |
| 允许注释的 JSON | `.vscode/` `.devcontainer/` | IDE 配置文件 |

---

## 第四步：读取工具配置

大多数工具的详细配置在 `pyproject.toml` 或独立配置文件中，需要单独读取：

```bash
# 在 pyproject.toml 中查找各工具配置
grep -n "^\[tool\." pyproject.toml
```

常见配置段落和含义：

```toml
[tool.ruff]
line-length = 100          # 行长限制（ruff 管辖的文件）

[tool.yapf]
column_limit = 80          # 行长限制（yapf 管辖的文件）

[tool.ruff.lint]
select = ["E", "F", ...]   # 启用的规则集

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]   # 对特定文件放宽规则

[tool.autoflake]
remove_all_unused_imports = true  # 删除所有未使用导入

[tool.codespell]
ignore-words-list = "rouge,ans"   # 忽略的误报词汇
```

---

## 第五步：为每个规则编写失败示例

这是分析文档的核心价值，每条规则都需要：

### 模板

````markdown
### N. 工具名 - 功能一句话描述

**版本**: vX.Y.Z
**适用文件**: Python / C++ / 所有文件
**配置**: （关键参数）

**失败示例**:
```python
# ❌ 这样写会失败，原因：xxx
<具体的错误代码>
```

**正确写法**:
```python
# ✅ 正确写法
<修正后的代码>
```

**常见场景**:
- 场景1（附简短说明）
- 场景2
````

### 各工具失败示例速查

**isort**：`import os` 之后不应该紧跟 `import numpy`（标准库和三方库要空一行分隔）

**yapf/ruff-format**：单行超过列宽限制，或运算符周围缺少空格

**autoflake**：`import json` 但文件中从未用到 `json`

**ruff (E/W)**：`E501` 行太长；`E225` `x=1+2` 中运算符旁缺空格

**ruff (F)**：`F401` 未使用的导入；`F821` 使用未定义的变量

**ruff (N)**：函数名用 `PascalCase`（应 `snake_case`）；类名用小写

**ruff (D)**：公共函数没有文档字符串；文档字符串不符合 Google 风格

**clang-format**：`if(x){` 缺空格；缩进混用 tab 和空格

**cmake-format**：`target_link_libraries(myapp PRIVATE libA libB)` 参数未换行对齐

**remove-crlf / mixed-line-ending**：Windows 编辑器保存导致 `\r\n` 换行符

**check-added-large-files**：误将模型文件、数据集加入 git 追踪

**detect-private-key**：文件中出现 `-----BEGIN RSA PRIVATE KEY-----`

**check-merge-conflict**：文件中残留 `<<<<<<< HEAD` 合并冲突标记

**trailing-whitespace**：行尾有空格（编辑器未配置自动清除）

**debug-statements**：提交了包含 `pdb.set_trace()` 或 `breakpoint()` 的代码

**codespell**：注释中写了 `proces` (应为 `process`)、`recieve` (应为 `receive`)

**DCO check**：提交信息中缺少 `Signed-off-by: Name <email>` 行

---

## 第六步：识别 Local Hooks

`local` 类型的 hook 是项目自己写的脚本，需要读取脚本源码才能理解规则：

```yaml
- repo: local
  hooks:
  - id: my-custom-check
    entry: ./scripts/my_check.py   # 读取这个文件
    language: script
```

重点关注脚本的：
- **输入**：处理什么文件/数据
- **检查逻辑**：判断通过/失败的条件
- **输出**：失败时打印什么错误信息

---

## 第七步：整理阶段（stages）

不同 stage 在不同时机触发，要特别说明：

| Stage | 触发时机 | 典型用途 |
|-------|---------|---------|
| `pre-commit`（默认）| `git commit` 时 | 代码格式、lint |
| `commit-msg` | 提交信息写完后 | DCO 签名、commit 格式检查 |
| `pre-push` | `git push` 前 | 运行测试 |
| `manual` | 仅手动触发 | 耗时检查 |

---

## 第八步：输出分析文档的结构

推荐的 Markdown 文档结构：

```
# 仓库名 Pre-commit 检查深度分析

## 目录
## 概述（工具数量、覆盖范围）

## Python 代码质量检查
  ### 1. isort
  ### 2. yapf / ruff
  ### 3. autoflake
  ...

## C/C++/其他语言检查
  ### clang-format
  ### cmake-format
  ...

## 通用文件检查
  ### 大文件、私钥、换行符、合并冲突...

## 项目特定检查（local hooks）
  ### 每个自定义脚本

## 配置文件（关键参数汇总）

## 最佳实践（本地安装、IDE 集成、CI 集成）

## 检查流程总结（流程图）

## 速查表（所有检查的一览表格）

## 附录：错误代码参考
```

---

## 注意事项

### 文件白名单 vs. 黑名单

- `files`（白名单）：只检查匹配的文件
- `exclude`（黑名单）：跳过匹配的文件
- 两者可以同时存在：先用 `files` 缩小范围，再用 `exclude` 排除例外

### 同一工具、不同配置文件

有些项目对不同目录使用不同的格式标准（如 `auto_deploy/` 目录单独用 ruff，其他目录用 yapf），需要分开说明，避免混淆。

### 工具之间的重叠和优先级

- `isort` + `ruff (I)` 都管 import 排序，同时启用时会有冲突，通常通过 `files` 分区管理
- `yapf` + `ruff-format` 都管代码格式，同理
- 分析时要搞清楚哪类文件用哪个工具

### 自动修复 vs. 手动修复

在速查表中区分哪些 hook 会自动修复（pre-commit 运行后会修改文件），哪些只报错需要手动修复——这对开发者很重要。

---

## 快速执行 Checklist

- [ ] 找到并读取 `.pre-commit-config.yaml`
- [ ] 定位 `repos:` 起始行，读取所有 hook
- [ ] 读取 `pyproject.toml` 或其他工具配置文件
- [ ] 对每个 `exclude` 规则，找到实际被排除的文件并解释原因
- [ ] 对 `local` hooks，读取脚本源码
- [ ] 每个 hook 至少写一个失败代码示例
- [ ] 整理速查表（工具 / 功能 / 是否自动修复）
- [ ] 说明 `commit-msg` 等非默认 stage 的 hook
- [ ] 将文档提交到指定分支并推送
