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

## 十三、结论

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
**数据来源**: requirements.txt, Dockerfile.multi, .github/workflows/blossom-ci.yml
**分析日期**: 2026-01-27
