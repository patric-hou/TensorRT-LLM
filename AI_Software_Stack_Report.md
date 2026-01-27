# TensorRT-LLM CI测试中使用的AI软件栈报告

**生成时间**: 2026-01-27
**分析范围**: Docker镜像、依赖文件、CI配置

---

## 一、核心AI框架和版本

### 1. **PyTorch**
- **版本要求**: `torch>=2.9.1,<=2.10.0a0`
- **基础镜像**: `nvcr.io/nvidia/pytorch:25.12-py3`
- **安装源**: `https://download.pytorch.org/whl/cu130`
- **相关组件**:
  - `torchvision`
  - `torchao>=0.14.1` (PyTorch量化优化)
  - `torch-c-dlpack-ext==0.1.3` (性能优化)
- **CUDA支持**: CUDA 13.0
- **说明**: PyTorch是TensorRT-LLM的主要深度学习框架

### 2. **TensorRT**
- **版本**: `tensorrt~=10.14.1`
- **CUDA支持**: 与CUDA Toolkit集成
- **作用**: 模型推理加速引擎

### 3. **Transformers (Hugging Face)**
- **版本**: `transformers==4.57.1`
- **作用**: 提供预训练模型和tokenizer

### 4. **Triton Server**
- **基础镜像**: `nvcr.io/nvidia/tritonserver:25.12-py3`
- **版本**: 25.12
- **作用**: 模型部署服务器

### 5. **Triton (OpenAI)**
- **版本**: `triton==3.5.1`
- **作用**: Python编程语言用于GPU编程

---

## 二、AI模型相关库

### 模型加载和处理
1. **Hugging Face生态**
   - `transformers==4.57.1` - 模型库
   - `accelerate>=1.7.0` - 大模型训练加速
   - `peft` - 参数高效微调
   - `optimum` - 硬件加速优化
   - `diffusers>=0.27.0` - 扩散模型

2. **量化和优化**
   - `nvidia-modelopt[torch]~=0.37.0` - NVIDIA模型优化工具包
   - `torchao>=0.14.1` - PyTorch架构优化

3. **多模态支持**
   - `opencv-python-headless` - 图像处理
   - `pillow` - 图像处理
   - `soundfile` - 音频处理

4. **注意力机制优化**
   - `flashinfer-python~=0.6.0` - Flash Attention实现

---

## 三、CUDA和GPU加速栈

### CUDA组件 (CUDA 13.0)
1. **核心库**
   - `cuda-python>=13`
   - `nvidia-cuda-nvrtc` - CUDA Runtime Compilation
   - `nvidia-nccl-cu13>=2.27.7,<=2.28.9` - 多GPU通信
   - `nvidia-ml-py>=13` - GPU管理

2. **计算库**
   - cuBLAS (通过CUDA Toolkit)
   - cuDNN (通过CUDA Toolkit)
   - NCCL (多GPU集合通信)

3. **自定义内核**
   - `nvidia-cutlass-dsl==4.3.4` - CUDA模板库
   - `apache-tvm-ffi==0.1.6` - TVM编译器接口

### GPU监控和调试
- `nvtx` - NVIDIA工具扩展
- `matplotlib` - 可视化（nvtx依赖）

---

## 四、数据处理和科学计算

### 数值计算
1. **核心库**
   - `numpy<2` - 数值计算基础
   - `pandas` - 数据分析
   - `mpmath>=1.3.0` - 多精度数学
   - `numexpr<2.14.0` - 数值表达式加速

2. **数据集处理**
   - `datasets==3.1.0` - Hugging Face数据集
   - `evaluate` - 模型评估
   - `h5py==3.12.1` - HDF5文件格式

### 可视化
- `plotly` - 交互式图表
- `matplotlib` - 科学绘图

---

## 五、模型格式和互操作

### 模型格式
1. **ONNX**
   - `onnx>=1.18.0,<1.20.0` - ONNX模型格式
   - `onnx_graphsurgeon>=0.5.2` - ONNX图优化
   - `polygraphy` - TensorRT调试工具

2. **其他工具**
   - `sentencepiece>=0.1.99` - Tokenization
   - `tiktoken` - OpenAI tokenizer
   - `einops` - 张量操作

---

## 六、分布式和并行计算

### MPI和通信
1. **MPI支持**
   - `mpi4py` - Python MPI绑定

2. **多节点支持**
   - `etcd3` (from GitHub) - 分布式协调
   - UCX (从源码安装) - 统一通信框架
   - NIXL (从源码安装) - NVIDIA内部通信库

3. **Ray支持**
   - 用于分布式推理和服务（在examples中）

---

## 七、推理服务和API

### Web服务
1. **FastAPI栈**
   - `fastapi>=0.120.1,<=0.121.3` - Web框架
   - `starlette>=0.49.1` - ASGI框架
   - `uvicorn` - ASGI服务器
   - `pydantic>=2.9.1` - 数据验证
   - `pydantic-settings[yaml]` - 配置管理

2. **OpenAI兼容**
   - `openai` - OpenAI客户端
   - `openai-harmony==0.0.4` - OpenAI协议兼容

3. **监控**
   - `prometheus_client` - Prometheus客户端
   - `prometheus_fastapi_instrumentator` - FastAPI监控

---

## 八、其他重要组件

### 约束和引导生成
- `xgrammar==0.1.25` - 语法约束生成
- `llguidance==0.7.29` - LLM引导生成
- `jsonschema` - JSON schema验证
- `partial_json_parser` - 部分JSON解析

### 语言模型工具
- `mistral-common==1.8.6` - Mistral模型工具
- `blobfile` - 大文件处理
- `backoff` - 重试逻辑

### 构建工具
- `build` - Python构建工具
- `meson` - 构建系统
- `ninja` - 构建系统
- `setuptools<80`
- `wheel<=0.45.1`
- `patchelf` - ELF二进制修改

### 系统工具
- `psutil` - 系统监控
- `colored` - 终端颜色
- `click` - 命令行接口
- `click_option_group` - CLI选项组
- `omegaconf` - 配置管理
- `pyzmq` - ZeroMQ消息队列

---

## 九、Docker基础镜像详情

### 基础镜像
```dockerfile
# 开发镜像
FROM nvcr.io/nvidia/pytorch:25.12-py3

# Triton服务镜像
FROM nvcr.io/nvidia/tritonserver:25.12-py3
```

### NVIDIA PyTorch容器 (25.12-py3) 包含
根据NVIDIA PyTorch容器发布说明：
- **PyTorch**: 2.10.0a0
- **Python**: 3.12.3
- **CUDA**: 13.0
- **cuDNN**: 最新版本
- **NCCL**: 2.28.9
- **TensorRT**: 10.x
- **预装库**: NumPy, SciPy, Pandas等科学计算库

---

## 十、测试框架 (从测试文件推断)

虽然不在requirements.txt中，但从测试文件可以看到使用：
1. **PyTest** - Python测试框架
2. **unittest** - Python内置测试框架
3. **conftest.py** - PyTest配置

---

## 十一、关键依赖版本约束总结

| 组件 | 版本约束 | 原因 |
|------|---------|------|
| PyTorch | `>=2.9.1,<=2.10.0a0` | 与NVIDIA容器25.12对齐 |
| NCCL | `>=2.27.7,<=2.28.9` | 与PyTorch 2.9.1+cu130依赖对齐 |
| TensorRT | `~=10.14.1` | 稳定版本 |
| Transformers | `==4.57.1` | 固定版本保证兼容性 |
| NumPy | `<2` | 避免NumPy 2.x破坏性变更 |
| Datasets | `==3.1.0` | 避免>3.1.0的不稳定版本 |
| ONNX | `>=1.18.0,<1.20.0` | 版本兼容性 |
| FastAPI | `>=0.120.1,<=0.121.3` | API稳定性 |

---

## 十二、CI测试中的特殊配置

### 从Jenkins文件推断的测试环境
基于`.github/workflows/blossom-ci.yml`和Jenkins脚本：

1. **Blossom CI系统**
   - NVIDIA内部CI/CD系统
   - 支持混合基础设施（GitHub + 自托管runner）

2. **测试类型**（从test-db文件推断）
   - L0测试（基础功能测试）
   - 性能测试（perf sanity）
   - 多GPU测试
   - 多节点测试

3. **硬件支持**
   - A10, A30, A100 GPU
   - H100, H200 GPU
   - B200, B300 GPU (最新)
   - GB200 (Grace-Blackwell)
   - RTX Pro 6000
   - L40S

---

## 十三、测试脚本和配置文件位置详解

本节详细列出各个AI软件组件在CI测试中的具体使用位置。

### 1. PyTorch

#### 安装位置
- **Docker安装脚本**: `docker/common/install_pytorch.sh`
  - 版本: 2.9.1
  - 支持架构: `TORCH_CUDA_ARCH_LIST="8.0;8.6;9.0;10.0;12.0"`
  - 可选从源码编译或使用预装版本

#### 测试文件
**Unit测试** (462个文件导入torch):
- `tests/unittest/_torch/` - PyTorch专用单元测试目录
  - `tests/unittest/_torch/attention/` - 注意力机制测试
  - `tests/unittest/_torch/auto_deploy/` - 自动部署测试
  - `tests/unittest/_torch/executor/test_pytorch_model_engine.py` - PyTorch模型引擎测试
  - `tests/unittest/_torch/modules/tests_lora_modules/` - LoRA模块测试
  - `tests/unittest/_torch/sampler/` - 采样器测试
  - `tests/unittest/_torch/speculative/` - 推测性解码测试
  - `tests/unittest/llmapi/test_llm_pytorch.py` - PyTorch后端LLM API测试
  - `tests/unittest/llmapi/test_llm_multi_gpu_pytorch.py` - 多GPU PyTorch测试

**集成测试**:
- `tests/integration/defs/accuracy/test_llm_api_pytorch.py` - PyTorch后端准确性测试
- `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py` - 多模态PyTorch测试
- `tests/integration/defs/accuracy/test_llm_api_pytorch_ray.py` - PyTorch+Ray分布式测试
- `tests/integration/defs/perf/pytorch_model_config.py` - PyTorch性能配置

#### 测试配置
- **Test-DB配置文件**: `tests/integration/test_lists/test-db/*.yml`
  - `l0_h100.yml` - H100 GPU的PyTorch后端测试
  - `l0_a100.yml` - A100 GPU的PyTorch后端测试
  - 等37个不同GPU配置文件

### 2. TensorRT

#### 安装位置
- **Docker安装脚本**: `docker/common/install_tensorrt.sh`
  - 版本: 10.14.1.48
  - CUDA版本: 13.1.0
  - cuDNN版本: 9.17.0.29
  - NCCL版本: 2.28.9
  - cuBLAS版本: 13.2.0.9

#### 测试文件
**Unit测试** (310个文件导入tensorrt):
- `tests/unittest/` - 所有核心功能测试
- 覆盖TensorRT引擎构建、推理、优化等

**集成测试**:
- `tests/integration/defs/accuracy/test_llm_api.py` - TensorRT后端准确性测试
- `tests/integration/defs/accuracy/test_llm_api_autodeploy.py` - 自动部署测试
- `tests/integration/defs/cpp/test_e2e.py` - C++ TensorRT端到端测试

#### 测试配置
- 所有`tests/integration/test_lists/test-db/*.yml`配置文件
- 所有性能测试配置: `tests/integration/test_lists/qa/*.yml`

### 3. Transformers (Hugging Face)

#### 依赖配置
- **requirements.txt**: `transformers==4.57.1` (第31行)
- **constraints.txt**: 版本约束

#### 测试文件
**使用Transformers的测试**:
- `tests/integration/defs/common.py` - `from transformers import AutoModelForCausalLM`
- `tests/integration/defs/deterministic/mixtral_deterministic.py` - Mixtral模型测试
- `tests/integration/defs/disaggregated/test_workers.py` - 分布式worker测试
- `tests/integration/defs/test_e2e.py` - 端到端tokenizer测试
- `tests/integration/defs/ray_orchestrator/RL/` - Ray+Transformers测试
- `tests/microbenchmarks/build_time_benchmark.py` - 构建时间基准测试

#### 模型测试
Transformers用于加载预训练模型进行对比测试:
- Llama系列
- Mixtral
- Qwen
- DeepSeek
- Nemotron

### 4. CUDA和NCCL

#### 安装位置
- **Docker安装脚本**: `docker/common/install_cuda_toolkit.sh`
  - CUDA版本: 13.1.0
  - NVRTC版本: 13.1.80

#### 依赖配置
- **requirements.txt**:
  - `cuda-python>=13` (第6行)
  - `nvidia-cuda-nvrtc` (第30行)
  - `nvidia-nccl-cu13>=2.27.7,<=2.28.9` (第29行)
  - `nvidia-ml-py>=13` (第16行)

#### 测试覆盖
- 所有多GPU测试使用NCCL进行通信
- 所有CUDA kernel测试
- `tests/integration/defs/cpp/test_multi_gpu.py` - 多GPU C++测试

### 5. MPI和分布式通信

#### 安装位置
- **Docker安装脚本**:
  - `docker/common/install_mpi4py.sh` - MPI4Py安装
  - `docker/common/install_ucx.sh` - UCX统一通信框架
  - `docker/common/install_nixl.sh` - NVIDIA NIXL通信库

#### 依赖配置
- **requirements.txt**: `mpi4py` (第9行)

#### 测试文件
- `tests/integration/defs/accuracy/test_llm_api_pytorch.py` - 使用`mpi4py.futures.MPIPoolExecutor`
- 所有多节点测试配置:
  - `tests/integration/test_lists/test-db/l0_gb200_multi_nodes.yml`
  - `tests/integration/test_lists/test-db/l0_gb200_multi_nodes_disagg_perf_sanity_*.yml`

### 6. Triton Server

#### 安装位置
- **Docker基础镜像**: `nvcr.io/nvidia/tritonserver:25.12-py3`
- **Docker安装脚本**: `docker/common/install_triton.sh`
- **Dockerfile**: `docker/Dockerfile.multi` (第94-119行)

#### 测试覆盖
- Triton backend测试
- 模型服务部署测试

### 7. Triton (OpenAI)

#### 依赖配置
- **requirements.txt**: `triton==3.5.1` (第69行)

#### 测试文件
- `tests/unittest/_torch/auto_deploy/unit/singlegpu/custom_ops/triton_kernels/` - Triton自定义kernel测试

### 8. ONNX相关

#### 依赖配置
- **requirements.txt**:
  - `onnx>=1.18.0,<1.20.0` (第11行)
  - `onnx_graphsurgeon>=0.5.2` (第12行)
  - `polygraphy` (第14行)

#### 测试覆盖
- ONNX模型转换测试
- 图优化测试

### 9. FastAPI和服务端

#### 依赖配置
- **requirements.txt**:
  - `fastapi>=0.120.1,<=0.121.3` (第48行)
  - `starlette>=0.49.1` (第49行)
  - `uvicorn` (第50行)
  - `pydantic>=2.9.1` (第34行)

#### 测试文件
- `tests/integration/defs/examples/serve/` - 服务端测试
- `tests/integration/defs/examples/serve/test_configs/` - 服务配置

### 10. 量化和优化工具

#### 依赖配置
- **requirements.txt**:
  - `nvidia-modelopt[torch]~=0.37.0` (第26行) - ModelOpt量化工具
  - `torchao>=0.14.1` (第80行) - PyTorch架构优化
  - `flashinfer-python~=0.6.0` (第56行) - Flash Attention

#### 测试覆盖
- 量化精度测试
- Flash Attention性能测试

### 11. 约束生成和结构化输出

#### 依赖配置
- **requirements.txt**:
  - `xgrammar==0.1.25` (第58行)
  - `llguidance==0.7.29` (第59行)
  - `jsonschema` (第60行)

#### 测试覆盖
- 结构化输出生成测试
- JSON schema验证测试

### 12. CI配置文件

#### BlossomCI配置
- **主配置**: `.github/workflows/blossom-ci.yml`
  - 触发条件: PR评论 `/bot run`
  - 阶段: Authorization → Vulnerability-scan → Job-trigger → Upload-Log
  - 授权用户列表: 353个NVIDIA员工

#### Pre-commit钩子
- **配置文件**: `.pre-commit-config.yaml`
  - 11个钩子: isort, yapf, ruff, clang-format, 等
  - 在每次commit前自动运行代码格式和质量检查

#### 许可证检查
- **配置文件**: `jenkins/license_cpp.json`
  - 用于扫描C++代码的许可证合规性
  - 跳过列表: 双许可证文件

### 13. Docker镜像构建

#### 主Dockerfile
- **文件**: `docker/Dockerfile.multi`
  - 基础镜像: `nvcr.io/nvidia/pytorch:25.12-py3`
  - 多阶段构建: base → devel → wheel → release
  - 安装所有依赖: PyTorch, TensorRT, CUDA, NCCL, MPI, UCX, NIXL

#### 依赖约束
- **constraints.txt**: 所有依赖的精确版本约束
- **requirements.txt**: 主要Python依赖
- **requirements-dev.txt**: 开发依赖

### 14. 测试执行入口

#### 集成测试
- **测试定义**: `tests/integration/defs/test_cases.yml`
- **GPU配置**: `tests/integration/perf_configs/gpu_configs.yml`
- **测试数据库**: `tests/integration/test_lists/test-db/*.yml` (37个配置文件)

#### 性能测试
- **核心性能**: `tests/integration/test_lists/qa/llm_perf_core.yml`
- **性能快速检查**: `tests/integration/test_lists/qa/llm_perf_sanity.yml`
- **Spark性能**: `tests/integration/test_lists/qa/llm_spark_perf.yml`

#### Unit测试
- **PyTest配置**: `tests/conftest.py`, `tests/unittest/conftest.py`
- **执行**: 使用`pytest`命令运行所有单元测试

### 15. 测试环境变量

从测试代码和配置中推断的关键环境变量:
- `PYTORCH_ALLOC_CONF="garbage_collection_threshold:0.99999"` - PyTorch内存管理
- `CCACHE_DIR=/root/.cache/ccache` - 编译缓存
- CUDA相关环境变量（CUDA_HOME, LD_LIBRARY_PATH等）

---

## 十四、结论

TensorRT-LLM的CI测试环境使用了完整的NVIDIA AI软件栈：

### 核心依赖
1. **PyTorch 2.9.1-2.10.0** - 主要深度学习框架
2. **TensorRT 10.14.1** - 推理加速引擎
3. **CUDA 13.0** - GPU计算平台
4. **Transformers 4.57.1** - 模型库

### 特点
- ✅ 完全基于NVIDIA官方容器镜像（PyTorch 25.12）
- ✅ 支持多种GPU架构（从A10到最新B300）
- ✅ 包含完整的分布式训练/推理栈（MPI, NCCL, UCX）
- ✅ 支持多种模型格式（PyTorch, ONNX, TensorRT）
- ✅ 内置OpenAI兼容API服务
- ✅ 支持约束生成和结构化输出

### 不包含的框架
- ❌ **TensorFlow** - 未使用
- ❌ **JAX** - 未使用
- ❌ **Keras** - 未使用（已被TensorFlow集成）
- ❌ **MXNet** - 未使用
- ❌ **PaddlePaddle** - 未使用

**说明**: TensorRT-LLM专注于PyTorch生态系统，不依赖其他主流深度学习框架。

---

**报告生成器**: Claude Code
**数据来源**: requirements.txt, Dockerfile.multi, .github/workflows/blossom-ci.yml, docker/common/install_*.sh, tests/**/*.py, tests/**/*.yml
**分析日期**: 2026-01-27
**更新日期**: 2026-01-27 (添加测试脚本和配置文件位置详解)
