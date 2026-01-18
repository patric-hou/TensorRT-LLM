# TensorRT-LLM Pre-commit 检查深度分析

## 目录
- [概述](#概述)
- [Python 代码质量检查](#python-代码质量检查)
- [C/C++/CUDA 代码检查](#ccuda-代码检查)
- [通用文件检查](#通用文件检查)
- [项目特定检查](#项目特定检查)
- [配置文件](#配置文件)
- [最佳实践建议](#最佳实践建议)

## 概述

TensorRT-LLM 项目使用 pre-commit 框架在代码提交前自动执行多项质量检查。这些检查涵盖了代码格式化、语法规范、安全性验证等多个方面，确保代码库的一致性和质量。

配置文件：`.pre-commit-config.yaml`

## Python 代码质量检查

### 1. isort - Import 语句排序

**仓库**: https://github.com/pycqa/isort
**版本**: 5.12.0
**配置**:
```yaml
line_length = 80
```

**功能描述**:
- 自动排序和组织 Python import 语句
- 按照标准库、第三方库、本地库的顺序分组
- 在每组内按字母顺序排序

**失败示例**:
```python
# ❌ 错误：未排序且混乱的导入
import os
from tensorrt_llm import models
import sys
from typing import List
import numpy as np

# ✅ 正确：经过 isort 排序后
import os
import sys
from typing import List

import numpy as np

from tensorrt_llm import models
```

**常见错误**:
- Import 语句顺序不符合 PEP 8 规范
- 标准库和第三方库混在一起
- 缺少分组之间的空行

---

### 2. yapf - Python 代码格式化器

**仓库**: https://github.com/google/yapf
**版本**: v0.43.0
**配置**:
```yaml
based_on_style = "pep8"
column_limit = 80
```

**功能描述**:
- 基于 PEP 8 风格自动格式化 Python 代码
- 限制每行最多 80 个字符
- 处理缩进、空格、换行等格式问题

**失败示例**:
```python
# ❌ 错误：超过 80 字符限制，格式混乱
def very_long_function_name_that_takes_many_parameters(param1, param2, param3, param4, param5):
    result=param1+param2+param3+param4+param5
    return result

# ✅ 正确：符合 yapf 格式
def very_long_function_name_that_takes_many_parameters(
        param1, param2, param3, param4, param5):
    result = param1 + param2 + param3 + param4 + param5
    return result
```

**常见错误**:
- 行长度超过 80 字符
- 运算符周围缺少空格
- 函数参数格式不规范

---

### 3. autoflake - 移除未使用的导入和变量

**仓库**: https://github.com/PyCQA/autoflake
**版本**: v2.3.1
**配置**:
```yaml
in-place = true
remove_all_unused_imports = true
remove_unused_variables = true
```

**功能描述**:
- 自动移除未使用的 import 语句
- 删除未使用的变量
- 清理冗余代码

**失败示例**:
```python
# ❌ 错误：包含未使用的导入和变量
import os
import sys
import json  # 未使用
from typing import List, Dict, Tuple  # Dict 和 Tuple 未使用

def process_data(data: List[str]):
    unused_var = "this is not used"  # 未使用的变量
    temp = os.path.join("path", "file")  # temp 未被使用
    return [x.upper() for x in data]

# ✅ 正确：移除未使用的部分
import os
from typing import List

def process_data(data: List[str]):
    return [x.upper() for x in data]
```

**常见错误**:
- 导入了库但未使用
- 定义了变量但从未引用
- 遗留的调试代码

---

### 4. ruff - 快速 Python Linter 和 Formatter

**仓库**: https://github.com/astral-sh/ruff-pre-commit
**版本**: v0.9.4
**配置**:
```yaml
line-length = 100
fix = true
select = ["D", "E", "W", "F", "I", "N", "UP", "PL", "RUF"]
```

**功能描述**:
- 综合性的 Python 代码检查工具
- 包含 pycodestyle、pyflakes、pydocstyle 等多个检查器
- 自动修复部分问题

**启用的检查规则**:
- **D** - pydocstyle（文档字符串规范）
- **E** - pycodestyle errors（代码风格错误）
- **W** - pycodestyle warnings（代码风格警告）
- **F** - pyflakes（逻辑错误检查）
- **I** - isort（导入排序）
- **N** - pep8-naming（命名规范）
- **UP** - pyupgrade（Python 版本升级）
- **PL** - pylint（代码质量）
- **RUF** - ruff 特定规则

**失败示例 1 - 文档字符串问题 (D)**:
```python
# ❌ 错误：缺少文档字符串
def calculate_metrics(data):
    return sum(data) / len(data)

# ✅ 正确：添加 Google 风格文档字符串
def calculate_metrics(data):
    """Calculate the average of the given data.

    Args:
        data: A list of numeric values.

    Returns:
        The average value of the data.
    """
    return sum(data) / len(data)
```

**失败示例 2 - 代码风格错误 (E/W)**:
```python
# ❌ 错误：多个风格问题
class MyClass:
    def __init__(self,x,y):  # E201: 括号后有多余空格
        self.x=x  # E225: 缺少运算符周围的空格
        self.y=y

    def method(self ):  # E201: 括号前有多余空格
        return self.x+self.y  # E226: 缺少算术运算符周围的空格

# ✅ 正确：符合风格规范
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def method(self):
        return self.x + self.y
```

**失败示例 3 - 命名规范 (N)**:
```python
# ❌ 错误：命名不符合规范
def Calculate_Total(ItemList):  # 函数名应该用 snake_case
    Total = 0  # 变量名应该用 snake_case
    for ITEM in ItemList:  # 循环变量不应全大写
        Total += ITEM
    return Total

class myClass:  # 类名应该用 PascalCase
    pass

# ✅ 正确：符合命名规范
def calculate_total(item_list):
    total = 0
    for item in item_list:
        total += item
    return total

class MyClass:
    pass
```

**失败示例 4 - 未定义变量 (F)**:
```python
# ❌ 错误：使用未定义的变量
def process():
    result = undefined_variable + 10  # F821: 未定义的名称
    return result

# ❌ 错误：导入但未使用
import numpy as np  # F401: 导入但未使用
import pandas

def work():
    return [1, 2, 3]

# ✅ 正确：所有变量都已定义
import numpy as np

def process():
    result = 10 + 20
    return result

def work():
    return np.array([1, 2, 3])
```

**常见错误**:
- 缺少或不规范的文档字符串
- 违反 PEP 8 代码风格
- 命名不符合 Python 规范
- 使用未定义的变量
- 未使用的导入

---

## C/C++/CUDA 代码检查

### 5. clang-format - C/C++/CUDA 格式化

**仓库**: https://github.com/pre-commit/mirrors-clang-format
**版本**: v16.0.0
**应用范围**: C++、C、CUDA 文件

**功能描述**:
- 统一 C/C++/CUDA 代码格式
- 处理缩进、空格、大括号位置等
- 排除 cubin 相关的自动生成文件

**失败示例**:
```cpp
// ❌ 错误：格式不规范
#include <iostream>
#include<vector>  // 缺少空格
class MyClass{  // 大括号位置不对
public:
MyClass(){}  // 缩进错误
void process(int x,int y){  // 参数间缺少空格
if(x>y){return x;}  // 格式混乱
else{return y;}}
};

// ✅ 正确：符合 clang-format 规范
#include <iostream>
#include <vector>

class MyClass {
public:
    MyClass() {}

    void process(int x, int y) {
        if (x > y) {
            return x;
        } else {
            return y;
        }
    }
};
```

**常见错误**:
- 缩进不一致（混用 tab 和空格）
- 大括号位置不符合项目规范
- 运算符周围缺少空格
- include 语句格式不统一

---

### 6. cmake-format - CMake 文件格式化

**仓库**: https://github.com/cheshirekow/cmake-format-precommit
**版本**: v0.6.10

**功能描述**:
- 格式化 CMakeLists.txt 和 .cmake 文件
- 统一 CMake 命令的缩进和对齐
- 改善 CMake 脚本的可读性

**失败示例**:
```cmake
# ❌ 错误：格式混乱
cmake_minimum_required(VERSION 3.18)
project(MyProject)
set(SOURCES
main.cpp
helper.cpp
utils.cpp)  # 缩进不一致
add_executable(myapp ${SOURCES})
target_link_libraries(myapp PRIVATE libA libB libC)  # 长行未分割

# ✅ 正确：符合 cmake-format 规范
cmake_minimum_required(VERSION 3.18)
project(MyProject)

set(SOURCES
    main.cpp
    helper.cpp
    utils.cpp
)

add_executable(myapp ${SOURCES})

target_link_libraries(
    myapp
    PRIVATE
        libA
        libB
        libC
)
```

**常见错误**:
- 命令参数未正确对齐
- 长命令未进行合理换行
- 缺少适当的空行分隔

---

## 通用文件检查

### 7. remove-crlf - 移除 Windows 换行符

**仓库**: https://github.com/Lucas-C/pre-commit-hooks.git
**版本**: v1.5.5

**功能描述**:
- 移除 Windows 风格的 CRLF (`\r\n`) 换行符
- 统一使用 Unix 风格的 LF (`\n`) 换行符
- 避免跨平台开发中的换行符问题

**失败示例**:
```python
# ❌ 错误：文件包含 CRLF 换行符（\r\n）
import os\r\n
\r\n
def main():\r\n
    print("Hello")\r\n

# ✅ 正确：使用 LF 换行符（\n）
import os\n
\n
def main():\n
    print("Hello")\n
```

**问题表现**:
- 在 Linux 系统上显示 `^M` 字符
- Git diff 显示整个文件被修改
- 跨平台协作时产生冲突

---

### 8. check-added-large-files - 大文件检查

**功能描述**:
- 防止意外提交大型文件
- 保持仓库体积合理
- 排除 cubin.cpp 和 cubin.h 文件

**失败场景**:
```bash
# ❌ 错误：尝试提交大文件
$ git add large_dataset.bin  # 100MB 文件
$ git commit
# 错误：文件 'large_dataset.bin' 超过大小限制

# ✅ 正确：使用 Git LFS 或不提交大文件
$ git lfs track "*.bin"
$ git add .gitattributes
$ git add large_dataset.bin
```

---

### 9. check-merge-conflict - 合并冲突检查

**功能描述**:
- 检测文件中是否包含未解决的合并冲突标记
- 防止将冲突标记提交到代码库

**失败示例**:
```python
# ❌ 错误：包含合并冲突标记
def calculate(x, y):
<<<<<<< HEAD
    return x + y
=======
    return x * y
>>>>>>> feature-branch

# ✅ 正确：已解决冲突
def calculate(x, y):
    return x + y
```

---

### 10. check-symlinks - 符号链接检查

**功能描述**:
- 检查符号链接的有效性
- 确保符号链接指向存在的文件
- 避免破损的符号链接

**失败场景**:
```bash
# ❌ 错误：符号链接指向不存在的文件
$ ln -s /path/to/nonexistent/file.txt link.txt
$ git add link.txt
$ git commit
# 错误：符号链接 'link.txt' 指向不存在的目标

# ✅ 正确：符号链接有效
$ ln -s existing_file.txt link.txt
$ git add link.txt
$ git commit  # 通过检查
```

---

### 11. detect-private-key - 私钥检测

**功能描述**:
- 扫描文件中的私钥模式
- 防止敏感信息泄露
- 检测 SSH 密钥、SSL 证书等

**失败示例**:
```bash
# ❌ 错误：文件包含私钥
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA...
-----END RSA PRIVATE KEY-----

# ✅ 正确：不提交私钥文件
# 将私钥文件添加到 .gitignore
$ echo "*.pem" >> .gitignore
$ echo "*.key" >> .gitignore
```

**检测到的私钥类型**:
- RSA 私钥
- DSA 私钥
- EC 私钥
- OpenSSH 私钥
- PGP 私钥

---

### 12. end-of-file-fixer - 文件结尾修复

**功能描述**:
- 确保所有文本文件以单个换行符结尾
- 移除文件末尾的多余空行
- 符合 POSIX 标准
- 排除 cubin 相关文件

**失败示例**:
```python
# ❌ 错误：文件末尾没有换行符
def main():
    print("Hello")
# EOF（没有换行符）

# ❌ 错误：文件末尾有多个空行
def main():
    print("Hello")


# EOF

# ✅ 正确：文件末尾有且仅有一个换行符
def main():
    print("Hello")
# EOF（有一个换行符）
```

---

### 13. check-yaml - YAML 格式检查

**功能描述**:
- 验证 YAML 文件的语法正确性
- 支持多文档 YAML
- 排除 GitLab CI 配置文件

**配置参数**:
```yaml
args: [--allow-multiple-documents, --unsafe]
exclude: ".*/gitlab/.*.yml"
```

**失败示例**:
```yaml
# ❌ 错误：YAML 语法错误
version: 1.0
services:
  web:
    image: nginx
   port: 80  # 缩进错误
    environment:
      - KEY: value
      - INVALID  # 格式错误

# ✅ 正确：有效的 YAML
version: 1.0
services:
  web:
    image: nginx
    port: 80
    environment:
      - KEY: value
      - VALID_KEY: valid_value
```

**常见 YAML 错误**:
- 缩进不正确（必须使用空格，不能用 tab）
- 冒号后缺少空格
- 列表项格式错误
- 引号使用不当

---

### 14. trailing-whitespace - 尾随空白检查

**功能描述**:
- 移除行尾的空白字符
- 保持代码整洁
- 排除 .patch 和 .md 文件

**失败示例**:
```python
# ❌ 错误：行尾有空白字符（用·表示空格）
def process():····
    data = [1, 2, 3]··
    return sum(data)····

# ✅ 正确：行尾无空白
def process():
    data = [1, 2, 3]
    return sum(data)
```

---

### 15. check-toml - TOML 格式检查

**功能描述**:
- 验证 TOML 配置文件的语法
- 确保 pyproject.toml 等文件正确

**失败示例**:
```toml
# ❌ 错误：TOML 语法错误
[tool.ruff
line-length = 100  # 缺少右括号

[tool.pytest]
markers = [
    "slow"
    "fast"  # 缺少逗号
]

# ✅ 正确：有效的 TOML
[tool.ruff]
line-length = 100

[tool.pytest]
markers = [
    "slow",
    "fast"
]
```

---

### 16. mixed-line-ending - 混合换行符检查

**功能描述**:
- 检测并修复混合的换行符
- 统一使用 LF (`\n`)
- 仅应用于 auto_deploy 目录

**配置**:
```yaml
args: [--fix=lf]
files: ".*/auto_deploy/.*"
```

**失败示例**:
```python
# ❌ 错误：文件中混合使用 CRLF 和 LF
import os\r\n
\n
def main():\n
    print("test")\r\n

# ✅ 正确：统一使用 LF
import os\n
\n
def main():\n
    print("test")\n
```

---

### 17. debug-statements - 调试语句检查

**功能描述**:
- 检测遗留的调试代码
- 仅应用于 auto_deploy 目录
- 防止调试代码进入生产环境

**失败示例**:
```python
# ❌ 错误：包含调试语句
def process_data(data):
    import pdb; pdb.set_trace()  # 调试断点

    result = []
    for item in data:
        import ipdb; ipdb.set_trace()  # IPython 调试器
        result.append(item * 2)

    breakpoint()  # Python 3.7+ 调试
    return result

# ✅ 正确：移除调试语句
def process_data(data):
    result = []
    for item in data:
        result.append(item * 2)
    return result
```

**检测的调试语句**:
- `pdb.set_trace()`
- `ipdb.set_trace()`
- `breakpoint()`
- `import pdb`
- `import ipdb`

---

### 18. check-json - JSON 格式检查

**功能描述**:
- 验证 JSON 文件的语法正确性
- 仅应用于 auto_deploy 目录
- 排除 VSCode 和 devcontainer 配置（可包含注释）

**配置**:
```yaml
files: ".*/auto_deploy/.*"
exclude: |
  (?x)^(
    .*\.vscode/.*\.json |
    .*\.devcontainer/.*\.json
  )$
```

**失败示例**:
```json
// ❌ 错误：JSON 语法错误
{
    "name": "test",
    "version": "1.0.0",
    "dependencies": {
        "package1": "1.0.0",  // 尾随逗号
    }
    "scripts": {  // 缺少逗号
        "test": "pytest"
    }
}

// ✅ 正确：有效的 JSON
{
    "name": "test",
    "version": "1.0.0",
    "dependencies": {
        "package1": "1.0.0"
    },
    "scripts": {
        "test": "pytest"
    }
}
```

**常见 JSON 错误**:
- 尾随逗号
- 缺少逗号分隔
- 使用单引号而非双引号
- 包含注释（标准 JSON 不支持）

---

### 19. codespell - 拼写检查

**仓库**: https://github.com/codespell-project/codespell
**版本**: v2.4.1

**配置**:
```yaml
args: ["-L", "Mor,ans,thirdparty,subtiles", "--skip", "ATTRIBUTIONS-*.md,*.svg", "--skip", "security_scanning/*"]
```

**功能描述**:
- 检测代码和注释中的拼写错误
- 跳过特定的已知词汇
- 排除某些文件和目录

**忽略的词汇**:
- Mor, ans, thirdparty, subtiles

**失败示例**:
```python
# ❌ 错误：拼写错误
def proces_data(dat):  # proces -> process, dat -> data
    """Proccess the incomming data."""  # Proccess -> Process, incomming -> incoming
    resutl = []  # resutl -> result
    for itme in dat:  # itme -> item
        resutl.append(itme * 2)
    return resutl

# ✅ 正确：拼写正确
def process_data(data):
    """Process the incoming data."""
    result = []
    for item in data:
        result.append(item * 2)
    return result
```

**常见拼写错误**:
- `proces` → `process`
- `recieve` → `receive`
- `occured` → `occurred`
- `seperate` → `separate`
- `definately` → `definitely`

---

### 20. mdformat - Markdown 格式化

**仓库**: https://github.com/executablebooks/mdformat
**版本**: 0.7.17
**应用范围**: auto_deploy 目录

**功能描述**:
- 格式化 Markdown 文件
- 统一标题、列表、代码块格式
- 支持 frontmatter

**失败示例**:
````markdown
<!-- ❌ 错误：格式不规范 -->
#Title Without Space

This is a paragraph with inconsistent   spacing.

-  List item 1
-   List item 2 (不一致的缩进)
- List item 3

```python
def test():
pass  # 缩进错误
```

<!-- ✅ 正确：符合 mdformat 规范 -->
# Title Without Space

This is a paragraph with inconsistent spacing.

- List item 1
- List item 2
- List item 3

```python
def test():
    pass
```
````

---

## 项目特定检查

### 21. test lists format - 测试列表格式检查

**类型**: Local Hook
**脚本**: `./scripts/format_test_list.py`
**应用范围**: `tests/integration/test_lists/.*\.txt$`

**功能描述**:
- 检查测试列表文件中的 tab 和多个空格
- 规范化空白字符为单个空格
- 移除前导空白

**实现原理**:
```python
def normalize_whitespace(content: str) -> str:
    """Remove leading whitespace, replace tabs and multiple spaces with single spaces."""
    lines = content.splitlines(keepends=True)
    normalized_lines = []

    for line in lines:
        # Remove leading whitespace and tabs
        line = line.lstrip(' \t')
        # Replace tabs with single space
        line = line.replace('\t', ' ')
        # Replace multiple spaces with single space
        line = re.sub(r'  +', ' ', line)
        normalized_lines.append(line)

    return ''.join(normalized_lines)
```

**失败示例**:
```text
# ❌ 错误：包含 tab 和多个空格
test_module::TestClass::test_method		TIMEOUT
test_other::TestCase::test_func    SKIP

# ✅ 正确：规范化后
test_module::TestClass::test_method TIMEOUT
test_other::TestCase::test_func SKIP
```

**检查内容**:
- 移除行首的空白字符
- 将 tab 替换为单个空格
- 将多个连续空格替换为单个空格

---

### 22. waive list check - 豁免列表重复检查

**类型**: Local Hook
**脚本**: `./scripts/check_test_list.py --check-duplicate-waives`
**参数**: `pass_filenames: false`

**功能描述**:
- 检查 `waives.txt` 文件中的重复测试项
- 防止重复的测试豁免条目
- 生成重复项报告

**实现原理**:
```python
def check_waive_duplicates(llm_src):
    """Check for duplicate entries in waives.txt and write report."""
    waives_list_path = f"{llm_src}/tests/integration/test_lists/waives.txt"
    dup_cases_record = f"{llm_src}/dup_cases.txt"

    # Track all occurrences: processed_line -> [(line_no, original_line), ...]
    dedup_lines = {}

    with open(waives_list_path, "r") as f:
        lines = f.readlines()

    for line_no, line in enumerate(lines, 1):
        original_line = line.strip()
        line = line.strip()

        if not line:
            continue

        # Check for SKIP marker and split
        line = line.split(" SKIP", 1)[0].strip()

        # Track all occurrences
        if line in dedup_lines:
            dedup_lines[line].append((line_no, original_line))
        else:
            dedup_lines[line] = [(line_no, original_line)]
```

**失败示例**:
```text
# ❌ 错误：waives.txt 包含重复项
# tests/integration/test_lists/waives.txt
test_module::TestClass::test_flaky SKIP flaky test
test_other::TestOther::test_broken SKIP broken
test_module::TestClass::test_flaky SKIP duplicate entry

# 错误输出：
Duplicate waive records found for 'test_module::TestClass::test_flaky' (2 occurrences):
  Occurrence 1 at line 1: 'test_module::TestClass::test_flaky SKIP flaky test'
  Occurrence 2 at line 3: 'test_module::TestClass::test_flaky SKIP duplicate entry'

# ✅ 正确：无重复项
test_module::TestClass::test_flaky SKIP flaky test
test_other::TestOther::test_broken SKIP broken
```

**检查流程**:
1. 读取 `waives.txt` 文件
2. 移除 `SKIP` 标记后的内容
3. 识别重复的测试名称
4. 生成包含行号的重复项报告
5. 如果发现重复项，检查失败

---

### 23. DCO check - 开发者证书检查

**类型**: Local Hook
**脚本**: `./scripts/dco_check.py`
**阶段**: `commit-msg`

**功能描述**:
- 验证提交信息中是否包含 "Signed-off-by" 签名
- 确保开发者证书（Developer Certificate of Origin）合规
- 保证贡献者已同意贡献协议

**实现原理**:
```python
def commit_message_has_signoff(message):
    """
    Check if the commit message has a Signed-off-by line.

    Args:
        message (str): The commit message.

    Returns:
        bool: True if the message is valid, False otherwise.
    """
    for line in message.splitlines():
        if re.match(r'^Signed-off-by: .+ <.+>$', line):
            return True
    return False
```

**失败示例**:
```bash
# ❌ 错误：提交信息缺少签名
$ git commit -m "Fix bug in tensor processing"

# 错误输出：
The commit message does not contain a Signed-off-by line.
Please review CONTRIBUTING.md for more details.

# ✅ 正确：包含 Signed-off-by 签名
$ git commit -m "Fix bug in tensor processing

Signed-off-by: John Doe <john.doe@example.com>"

# 或使用 git commit -s 自动添加签名
$ git commit -s -m "Fix bug in tensor processing"
```

**签名格式要求**:
- 必须以 `Signed-off-by:` 开头
- 包含贡献者的全名
- 包含有效的电子邮件地址
- 格式：`Signed-off-by: Full Name <email@example.com>`

**使用 git -s 快捷方式**:
```bash
# 自动添加 Signed-off-by 行
$ git commit -s -m "Your commit message"

# 配置 git 别名简化操作
$ git config --global alias.ci "commit -s"
$ git ci -m "Your commit message"
```

---

## 配置文件

### pyproject.toml 关键配置

```toml
[tool.isort]
line_length = 80

[tool.yapf]
based_on_style = "pep8"
column_limit = 80

[tool.codespell]
skip = ".git,3rdparty,tests/integration/test_input_files**,**.jsonl,**.json"
exclude-file = "examples/models/core/whisper/tokenizer.py"
ignore-words-list = "rouge,inout,atleast,strat,nd,subtile,thrid,improbe,NotIn,te,iteract,anythin,tru,Tracin,vEw,dOut"

[tool.autoflake]
in-place = true
remove_all_unused_imports = true
remove_unused_variables = true

[tool.ruff]
line-length = 100
fix = true

[tool.ruff.format]
skip-magic-trailing-comma = false
docstring-code-format = true
docstring-code-line-length = "dynamic"

[tool.ruff.lint]
select = [
    "D",   # pydocstyle
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "N",   # pep8-naming
    "UP",  # pyupgrade
    "PL",  # pylint
    "RUF", # ruff-specific
]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]
"tests/_torch/auto_deploy/*" = ["D", "E402"]
"*/_[a-zA-Z]*" = ["D"]

[tool.ruff.lint.pycodestyle]
max-line-length = 120

[tool.ruff.lint.pydocstyle]
convention = "google"

[tool.ruff.lint.pylint]
max-args = 10
```

---

## 最佳实践建议

### 1. 开发环境设置

**安装 pre-commit**:
```bash
# 安装 pre-commit
pip install pre-commit

# 安装 git hooks
cd TensorRT-LLM
pre-commit install

# 安装 commit-msg hook（用于 DCO 检查）
pre-commit install --hook-type commit-msg
```

**手动运行检查**:
```bash
# 检查所有文件
pre-commit run --all-files

# 检查特定文件
pre-commit run --files path/to/file.py

# 运行特定的 hook
pre-commit run isort --all-files
pre-commit run ruff --all-files
```

---

### 2. 常见问题解决

**问题 1：Python 导入顺序混乱**
```bash
# 解决方案：运行 isort
$ pre-commit run isort --all-files
```

**问题 2：代码格式不符合规范**
```bash
# 解决方案：运行格式化工具
$ pre-commit run yapf --all-files
$ pre-commit run ruff-format --all-files
```

**问题 3：忘记添加 Signed-off-by**
```bash
# 解决方案：修改最后一次提交
$ git commit --amend -s --no-edit

# 或配置 git 默认使用 -s
$ git config --global format.signoff true
```

**问题 4：检查失败后的处理**
```bash
# pre-commit 会自动修复部分问题，需要重新添加
$ git add -u
$ git commit
```

---

### 3. IDE 集成

**VSCode 设置**:
```json
{
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "python.formatting.provider": "yapf",
    "editor.formatOnSave": true,
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    }
}
```

**PyCharm 设置**:
- File Watchers 配置 isort 和 yapf
- 启用 "Reformat code" on save
- 配置外部工具运行 pre-commit

---

### 4. CI/CD 集成

在 CI 流程中运行 pre-commit 检查：

```yaml
# .github/workflows/pre-commit.yml
name: Pre-commit Checks

on: [push, pull_request]

jobs:
  pre-commit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install pre-commit
        run: pip install pre-commit
      - name: Run pre-commit
        run: pre-commit run --all-files
```

---

### 5. 跳过检查（不推荐）

在特殊情况下可以跳过检查，但应谨慎使用：

```bash
# 跳过 pre-commit hooks（不推荐）
$ git commit --no-verify -m "Emergency fix"

# 跳过特定的 hook
$ SKIP=ruff git commit -m "Work in progress"

# 跳过多个 hooks
$ SKIP=ruff,isort git commit -m "WIP"
```

**警告**：跳过检查可能导致代码质量问题，应仅在紧急情况下使用。

---

## 检查流程总结

### 提交前的完整检查流程

```
1. 代码编写完成
   ↓
2. Git Add 文件
   ↓
3. Git Commit 触发 pre-commit
   ↓
4. Python 文件检查：
   - isort: 排序导入
   - yapf: 格式化代码
   - autoflake: 移除未使用代码
   - ruff: 综合检查和格式化
   ↓
5. C/C++/CUDA 文件检查：
   - clang-format: 格式化
   ↓
6. 通用文件检查：
   - remove-crlf: 移除 CRLF
   - check-added-large-files: 大文件检查
   - check-merge-conflict: 冲突检查
   - detect-private-key: 私钥检查
   - end-of-file-fixer: 文件结尾修复
   - trailing-whitespace: 尾随空白
   - check-yaml/toml/json: 格式检查
   - codespell: 拼写检查
   ↓
7. 项目特定检查：
   - test lists format: 测试列表格式
   - waive list check: 豁免列表检查
   ↓
8. Commit Message 检查：
   - DCO check: 签名验证
   ↓
9. 所有检查通过 → 提交成功
   ↓
   检查失败 → 修复问题 → 重新提交
```

---

## 检查规则速查表

| 检查工具 | 类型 | 主要功能 | 自动修复 |
|---------|------|----------|---------|
| isort | Python | Import 排序 | ✅ |
| yapf | Python | 代码格式化 | ✅ |
| autoflake | Python | 移除未使用代码 | ✅ |
| ruff | Python | 综合检查 | ✅ (部分) |
| clang-format | C/C++ | 代码格式化 | ✅ |
| cmake-format | CMake | 格式化 | ✅ |
| remove-crlf | 通用 | 移除 CRLF | ✅ |
| check-added-large-files | 通用 | 大文件检测 | ❌ |
| check-merge-conflict | 通用 | 冲突检测 | ❌ |
| check-symlinks | 通用 | 符号链接检查 | ❌ |
| detect-private-key | 安全 | 私钥检测 | ❌ |
| end-of-file-fixer | 通用 | 文件结尾 | ✅ |
| check-yaml | 配置 | YAML 语法 | ❌ |
| trailing-whitespace | 通用 | 尾随空白 | ✅ |
| check-toml | 配置 | TOML 语法 | ❌ |
| mixed-line-ending | 通用 | 换行符统一 | ✅ |
| debug-statements | Python | 调试语句 | ❌ |
| check-json | 配置 | JSON 语法 | ❌ |
| codespell | 通用 | 拼写检查 | ✅ |
| mdformat | Markdown | 格式化 | ✅ |
| test lists format | 项目 | 测试列表格式 | ✅ |
| waive list check | 项目 | 重复检查 | ❌ |
| DCO check | Git | 签名验证 | ❌ |

---

## 附录：错误代码参考

### Ruff 常见错误代码

**文档字符串 (D)**:
- `D100`: 公共模块缺少文档字符串
- `D101`: 公共类缺少文档字符串
- `D102`: 公共方法缺少文档字符串
- `D103`: 公共函数缺少文档字符串
- `D107`: `__init__` 方法缺少文档字符串
- `D417`: 参数缺少文档字符串

**代码风格 (E/W)**:
- `E201`: 括号后有多余空白
- `E202`: 括号前有多余空白
- `E225`: 运算符周围缺少空格
- `E226`: 算术运算符周围缺少空格
- `E501`: 行长度超过限制
- `W291`: 行尾有空白
- `W292`: 文件末尾缺少换行符

**pyflakes (F)**:
- `F401`: 导入但未使用
- `F403`: 使用 `from module import *`
- `F811`: 重复定义
- `F821`: 使用未定义的名称
- `F841`: 局部变量已赋值但未使用

**命名 (N)**:
- `N801`: 类名应使用 CapWords 约定
- `N802`: 函数名应使用小写
- `N803`: 参数名应使用小写
- `N806`: 变量名应使用小写

---

## 结论

TensorRT-LLM 的 pre-commit 检查体系非常完善，覆盖了：
- ✅ **Python 代码质量**：格式化、语法检查、文档规范
- ✅ **C/C++/CUDA 代码**：格式化和风格统一
- ✅ **配置文件**：YAML、TOML、JSON 语法验证
- ✅ **安全性**：私钥检测、大文件预防
- ✅ **项目规范**：测试列表、DCO 签名

遵循这些检查规则能够：
1. 保持代码库的一致性和可维护性
2. 及早发现潜在的错误和问题
3. 提高代码审查效率
4. 确保符合开源贡献规范

建议开发者：
- 在本地配置 pre-commit hooks
- 在编写代码时就遵循规范，而非依赖自动修复
- 理解每个检查的目的，而非盲目修复
- 在 IDE 中集成相关工具，实时发现问题

---

**文档版本**: v1.0
**最后更新**: 2026-01-18
**维护者**: Claude AI Assistant
