# AI 知识大全与学习导航工作环境

> 基于《AI人工智能知识大全 - 全方向深度指南》（洞察AI-Onlyone, 2026）封装的可复用技能。
> 本技能是覆盖 30+ 核心方向的 AI 知识体系总索引，帮助用户快速定位 AI 技术领域、理解技术全貌、规划学习路径、选择工具框架，并做出技术选型决策。

---

## 1. 任务边界

**做**
- 提供 AI 全技术栈的知识地图：从数学基础到前沿大模型、从理论到工程落地
- 帮助用户定位自己处于 AI 学习的哪个阶段，并给出下一阶段路径
- 提供各领域技术选型对比表（框架、模型、工具、数据库等）
- 指导模型训练全流程：预训练 → SFT → RLHF/DPO → 部署 → 监控
- 提供 Prompt Engineering 核心技巧和最佳实践
- 帮助用户理解 LLM、RAG、Agent、AIGC 等前沿技术的架构原理
- 提供 AI 面试高频考点和关键问题
- 指导 MLOps 工程化落地：模型部署、推理优化、监控迭代
- 提供 AI 安全、合规、法规方面的知识框架
- 帮助用户理解 AI 商业化模式和创业趋势

**不做**
- 不提供具体模型的完整训练代码实现（提供关键代码片段和工具推荐）
- 不做 AI 模型的性能基准测试和对比报告
- 不提供数学公式的严格推导证明（提供直觉理解和应用场景）
- 不涉及具体企业内部 AI 系统的架构审计
- 不做投资建议或商业预测

---

## 2. AI 知识体系全景

### 2.1 知识体系框架（2025-2026 热点）

```
📂 AI人工智能知识体系
├── 📐 数学基础 → 线性代数 / 概率统计 / 微积分 / 优化理论
├── 🤖 机器学习 → 监督学习 / 无监督学习 / 集成学习
├── 🧬 深度学习 → CNN / RNN / Transformer / 注意力机制
├── 💬 NLP自然语言处理 → BERT / GPT / 文本分类 / 情感分析
├── 👁️ 计算机视觉 → 图像分类 / 目标检测 / 图像分割
├── 🗣️ 大语言模型LLM → GPT / Claude / LLaMA / Qwen
├── 🔗 RAG与AI Agent → 向量数据库 / LangChain / 智能体
├── 🎨 AIGC生成模型 → GAN / Diffusion / AI绘画 / 视频生成
├── 🌍 多模态AI → GPT-4V / Gemini / 视觉语言模型
├── 🎮 强化学习 → Q-Learning / PPO / RLHF
├── 🏗️ 深度学习框架 → PyTorch / TensorFlow / JAX
├── 🚀 MLOps → 模型部署 / TensorRT / ONNX / 监控
├── 🔒 AI安全 → 对齐技术 / 隐私保护 / 偏见公平
├── 🏭 应用场景 → 智能客服 / 推荐系统 / 自动驾驶 / 医疗AI
├── ✍️ 提示词工程 → Prompt Engineering / CoT / Few-shot / ReAct
├── 🕸️ 知识图谱 → 构建流程 / 图神经网络 / 嵌入方法
├── 🔐 联邦学习 → 横向/纵向联邦 / 隐私计算
├── 💻 AI编程助手 → Copilot / Cursor / Claude Code
├── 🤖 具身智能 → 人形机器人 / 多模态感知 / 运动控制
├── 📱 端侧AI → 边缘计算 / 模型压缩 / 端侧部署
├── 🤖 Agent进阶 → CrewAI / LangGraph / MCP协议
├── 🧩 混合专家MoE → DeepSeek V3 / Mixtral
├── 🏗️ AI基础设施 → GPU集群 / 分布式训练
├── 🛡️ AI安全进阶 → 红队测试 / 对抗攻防
├── ⚖️ AI法规合规 → EU AI Act / 生成式AI管理办法
├── 🏭 AI行业应用 → 教育 / 金融 / 制造
├── 💼 AI商业化 → SaaS模式 / 创业趋势
├── 🎙️ AI语音技术 → ASR / TTS / 语音克隆
├── 🔍 AI搜索引擎 → Perplexity / AI搜索
├── 📊 AI数据分析 → BI / NL2SQL / AutoML
└── 🧪 AI测试 → 测试生成 / 缺陷预测
```

### 2.2 学习路线图

| 阶段 | 内容 | 时间 | 产出 |
|------|------|------|------|
| 基础 | Python + NumPy/Pandas + 线性代数 + 概率论 | 1-2月 | 数据处理能力 |
| 入门 | 机器学习基础 + Scikit-learn + 经典算法 | 2-3月 | Kaggle入门赛 |
| 进阶 | 深度学习 + PyTorch + CNN/RNN/Transformer | 2-3月 | 图像/NLP项目 |
| 专精 | LLM/RAG/Agent/AIGC 方向深入 | 3-6月 | 完整AI应用 |
| 工程 | MLOps + 模型部署 + 生产环境优化 | 持续 | 上线产品 |

---

## 3. 核心技术模块详解

### 3.1 数学基础

#### 线性代数

| 概念 | 说明 | AI中的应用 |
|------|------|-----------|
| 向量 | 一维数组，表示方向和大小 | 词向量(Word2Vec)、特征向量 |
| 矩阵 | 二维数组，线性变换 | 权重矩阵、图像表示 |
| 矩阵乘法 | 线性变换的组合 | 神经网络前向传播 |
| 特征值/特征向量 | Av = λv | PCA降维、谱聚类 |
| SVD分解 | 矩阵分解为UΣV^T | 推荐系统、降维 |
| 范数 | 向量/矩阵的大小度量 | 正则化(L1/L2)、梯度裁剪 |

#### 概率论与统计

| 概念 | 说明 | AI中的应用 |
|------|------|-----------|
| 贝叶斯定理 | P(A\|B) = P(B\|A)P(A)/P(B) | 朴素贝叶斯、贝叶斯优化 |
| 概率分布 | 高斯/伯努利/泊松分布 | 生成模型、VAE |
| 最大似然估计 | MLE参数估计 | 模型训练目标函数 |
| KL散度 | 两个分布的差异度量 | VAE损失函数 |
| 信息熵 | 不确定性度量 | 交叉熵损失函数 |

#### 微积分与优化

| 概念 | 说明 | AI中的应用 |
|------|------|-----------|
| 梯度 | 函数变化最快的方向 | 梯度下降优化 |
| 链式法则 | 复合函数求导 | 反向传播算法 |
| 梯度下降 | 沿负梯度方向更新参数 | SGD/Adam优化器 |
| 凸优化 | 凸函数的全局最优 | SVM、逻辑回归 |
| 拉格朗日乘子 | 约束优化方法 | SVM对偶问题 |

---

### 3.2 机器学习

#### 监督学习算法

| 算法 | 类型 | 特点 | 适用场景 |
|------|------|------|----------|
| 线性回归 | 回归 | 简单、可解释 | 房价预测 |
| 逻辑回归 | 分类 | 输出概率、高效 | 二分类问题 |
| 决策树 | 分类/回归 | 可解释、易过拟合 | 规则提取 |
| SVM | 分类 | 核技巧、高维有效 | 文本分类 |
| KNN | 分类/回归 | 简单、计算量大 | 小数据集 |
| 朴素贝叶斯 | 分类 | 快速、适合文本 | 垃圾邮件过滤 |

#### 无监督学习算法

| 算法 | 类型 | 特点 | 适用场景 |
|------|------|------|----------|
| K-Means | 聚类 | 简单高效、需指定K | 客户分群 |
| DBSCAN | 聚类 | 任意形状、自动确定簇数 | 异常检测 |
| PCA | 降维 | 线性降维、保留方差 | 数据可视化 |
| t-SNE | 降维 | 非线性、适合可视化 | 高维数据可视化 |
| AutoEncoder | 降维/生成 | 神经网络、非线性 | 特征学习 |

#### 集成学习

| 方法 | 策略 | 代表算法 |
|------|------|----------|
| Bagging | 并行训练、投票/平均 | 随机森林(Random Forest) |
| Boosting | 串行训练、逐步纠错 | XGBoost、LightGBM、CatBoost |
| Stacking | 多层模型组合 | 元学习器 |

> **Gotcha**: XGBoost/LightGBM 在结构化数据竞赛中仍然是王者级算法，深度学习在图像/NLP领域占主导。

#### 模型评估指标

| 任务 | 指标 | 说明 |
|------|------|------|
| 分类 | Accuracy, Precision, Recall, F1, AUC-ROC | 精确率查准率、召回率查全率 |
| 回归 | MSE, RMSE, MAE, R² | 均方误差、平均绝对误差 |
| 聚类 | 轮廓系数、DB指数 | 簇内紧密度、簇间分离度 |
| 排序 | NDCG, MAP, MRR | 推荐系统评估 |

---

### 3.3 深度学习

#### 神经网络基础

| 概念 | 说明 |
|------|------|
| 感知机 | 最简单的神经网络，单层 |
| 激活函数 | ReLU、Sigmoid、Tanh、GELU（引入非线性） |
| 反向传播 | 链式法则计算梯度，更新权重 |
| 优化器 | SGD、Adam、AdamW、LAMB |
| 正则化 | Dropout、BatchNorm、LayerNorm、权重衰减 |
| 梯度消失/爆炸 | 残差连接、梯度裁剪、合适初始化 |

#### 激活函数对比

| 函数 | 公式 | 优点 | 缺点 |
|------|------|------|------|
| ReLU | max(0,x) | 计算快、缓解梯度消失 | Dead ReLU |
| Sigmoid | 1/(1+e^(-x)) | 输出(0,1)概率 | 梯度消失 |
| Tanh | (e^x-e^(-x))/(e^x+e^(-x)) | 零中心 | 梯度消失 |
| GELU | x·Φ(x) | Transformer常用 | 计算稍慢 |
| Swish | x·sigmoid(x) | 平滑、性能好 | 计算稍慢 |

#### CNN 卷积神经网络

| 组件 | 作用 |
|------|------|
| 卷积层(Conv) | 提取局部特征，参数共享 |
| 池化层(Pool) | 降维、平移不变性 |
| 全连接层(FC) | 分类决策 |
| 批归一化(BN) | 加速训练、稳定梯度 |

经典 CNN 架构演进：LeNet-5(1998) → AlexNet(2012) → VGGNet(2014) → GoogLeNet(2014) → ResNet(2015) → EfficientNet(2019) → ConvNeXt(2022)

#### Transformer 架构（核心！）

> **⭐ Transformer 是现代AI的基石架构**，GPT、BERT、ViT、Stable Diffusion 等全部基于Transformer。

**Self-Attention 核心公式**：
```
Attention(Q, K, V) = softmax(Q·K^T / √d_k) · V

# Q(Query查询) K(Key键) V(Value值)
# d_k: 缩放因子，防止点积过大
# softmax: 归一化为注意力权重
```

**Transformer 关键组件**：

| 组件 | 作用 |
|------|------|
| Self-Attention | 捕获序列内任意位置关系 |
| Multi-Head Attention | 多角度注意力 |
| 位置编码 | 注入序列顺序信息 |
| 残差连接 + LayerNorm | 稳定训练 |
| 前馈网络(FFN) | 非线性变换 |
| Encoder-Decoder | 编码-解码结构 |

---

### 3.4 大语言模型 LLM

#### 架构类型

| 架构 | 代表模型 | 特点 |
|------|----------|------|
| Decoder-only | GPT、LLaMA、Qwen | 自回归生成，最流行 |
| Encoder-only | BERT、RoBERTa | 双向理解，适合NLU |
| Encoder-Decoder | T5、BART | 适合翻译、摘要 |

#### 训练流程

```
预训练(Pre-training) → 监督微调(SFT) → RLHF/DPO对齐 → 部署上线
海量文本学习语言    高质量指令数据    人类偏好对齐      生产环境服务
```

| 阶段 | 数据 | 目标 |
|------|------|------|
| 预训练 | 海量文本（TB级） | 学习语言模式（下一个token预测） |
| SFT | 高质量指令-回答对 | 学习遵循指令 |
| RLHF | 人类偏好排序数据 | 对齐人类价值观 |
| DPO | 偏好对数据 | 简化版RLHF，无需奖励模型 |

#### 主流大模型

| 模型 | 公司 | 特点 |
|------|------|------|
| GPT-4/4o | OpenAI | 综合能力最强之一 |
| Claude 4 | Anthropic | 长上下文、安全性强 |
| Gemini | Google | 原生多模态 |
| LLaMA 3 | Meta | 开源标杆 |
| Qwen 2.5 | 阿里 | 中文能力强 |
| DeepSeek V3 | DeepSeek | 高性能开源 |

#### 模型微调技术

| 方法 | 说明 | 显存需求 |
|------|------|----------|
| 全量微调 | 更新所有参数 | 极高（8×A100） |
| LoRA | 低秩适配，插入小矩阵 | 低（单卡可调7B） |
| QLoRA | 4-bit量化+LoRA | 极低（24GB可调65B） |
| Prefix Tuning | 在输入前加可训练前缀 | 低 |
| P-Tuning | 连续提示词 | 低 |

**LoRA 代码示例**：
```python
from transformers import AutoModelForCausalLM
from peft import get_peft_model, LoraConfig, TaskType

lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,                        # 秩（越小越省显存）
    lora_alpha=16,              # 缩放因子
    lora_dropout=0.05,
    target_modules=["q_proj", "v_proj"]  # 目标模块
)

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")
peft_model = get_peft_model(model, lora_config)
peft_model.print_trainable_parameters()
# 输出: trainable params: 4,194,304 || all params: 6,742,609,920 || trainable%: 0.062
```

**微调工具推荐**：HuggingFace PEFT、HuggingFace TRL、LlamaFactory、Unsloth、Axolotl、LLaMA-Factory

---

### 3.5 RAG 与 AI Agent

#### RAG 检索增强生成

```
用户提问 → 向量化查询 → 向量数据库检索相关文档 → 文档作为上下文 + 问题 → LLM生成回答
```

**RAG 解决的问题**：
- LLM 幻觉问题：基于真实文档生成，减少编造
- 知识时效性：实时更新知识库，无需重新训练
- 领域专业性：注入企业/行业专属知识
- 可追溯性：回答可引用来源文档

#### 向量数据库选型

| 数据库 | 类型 | 特点 |
|--------|------|------|
| Milvus | 开源 | 高性能、分布式 |
| Chroma | 开源 | 轻量、易上手 |
| FAISS | 开源(Meta) | 高性能向量搜索 |
| Pinecone | 云服务 | 全托管、易用 |
| Weaviate | 开源 | 多模态支持 |
| Qdrant | 开源 | Rust实现、高性能 |

#### AI Agent 智能体

```
AI Agent = LLM + 工具调用 + 记忆 + 规划能力

# 核心能力
1. 理解任务: LLM解析用户意图
2. 规划步骤: 将复杂任务分解为子步骤
3. 调用工具: 搜索引擎、数据库、API、代码执行
4. 记忆管理: 短期记忆(对话历史) + 长期记忆(向量数据库)
5. 反思纠错: 检查结果、自动修正
```

**Agent 框架对比**：

| 框架 | 特点 |
|------|------|
| LangChain | 最流行、生态丰富 |
| LlamaIndex | 专注RAG、数据索引 |
| AutoGen | 微软、多Agent协作 |
| CrewAI | 角色扮演Agent |
| Dify | 低代码AI应用平台 |
| Coze | 字节跳动、可视化搭建 |

**2025-2026 Agent 趋势**：

| 趋势 | 说明 |
|------|------|
| MCP协议 | Model Context Protocol，Agent标准通信协议 |
| A2A协议 | Google提出的Agent-to-Agent通信协议 |
| 多Agent编排 | 从单Agent转向复杂多Agent系统 |
| 生产级框架 | LangGraph、AutoGen等成熟化 |
| 国产平台 | Coze、百炼、元器等平台兴起 |

---

### 3.6 AIGC 与生成模型

#### GAN vs Diffusion 对比

| 特性 | GAN | Diffusion |
|------|-----|-----------|
| 训练稳定性 | 较难、模式坍塌 | 更稳定 |
| 生成质量 | 高质量、多样性有限 | 高质量且多样 |
| 生成速度 | 快（一次前向） | 慢（多步迭代） |
| 可控性 | 一般 | 强（配合文本条件） |

**Diffusion 核心原理**：
- 前向过程（加噪）：逐步向图像添加高斯噪声，直到变成纯噪声
- 反向过程（去噪）：学习从纯噪声逐步去噪，恢复清晰图像
- 训练时学习预测每一步加入的噪声

#### AI 绘画工具

| 工具 | 来源 | 特点 |
|------|------|------|
| Stable Diffusion | Stability AI | 开源、可本地部署、生态丰富 |
| Midjourney | Midjourney Inc. | 高质量艺术风格、Discord交互 |
| DALL·E 3 | OpenAI | 与ChatGPT集成 |
| 通义万相 | 阿里 | 中文优化 |
| 文心一格 | 百度 | 中文生态 |

**Stable Diffusion 核心技术**：Diffusion Model + CLIP(文本编码器) + VAE(图像编解码) + U-Net(去噪网络) + LoRA(风格微调) + ControlNet(姿态/边缘/深度控制)

#### 视频生成

| 模型 | 公司 | 特点 |
|------|------|------|
| Sora | OpenAI | 文本→60秒高质量视频 |
| 可灵(Kling) | 快手 | 中文视频生成 |
| Runway Gen-3 | Runway | 专业视频生成 |
| Pika | Pika Labs | 简单易用 |

---

### 3.7 提示词工程 Prompt Engineering

#### 核心技巧

| 技巧 | 说明 | 示例 |
|------|------|------|
| Zero-shot | 直接提问，无示例 | "将以下文本分类为正面/负面" |
| Few-shot | 提供2-5个示例 | 给出输入-输出对，让模型学习模式 |
| Chain-of-Thought | 引导逐步推理 | "让我们一步一步思考" |
| Role Prompting | 角色设定 | "你是一位资深Python开发者" |
| ReAct | 推理+行动结合 | 思考→行动→观察循环 |
| Tree-of-Thought | 多路径推理 | 探索多条推理路径，投票选择 |
| Self-Consistency | 多次采样取多数 | 多次生成答案，投票选最优 |

#### Prompt 最佳实践

- **明确指令**：清晰描述任务目标和输出格式
- **分隔符**：用 ```、---、XML标签分隔不同内容
- **输出格式**：指定JSON、Markdown、表格等格式
- **示例质量**：Few-shot示例应覆盖多样化场景
- **迭代优化**：根据输出不断调整Prompt
- **温度控制**：创意任务用高温(0.7-1.0)，精确任务用低温(0-0.3)

---

### 3.8 MLOps 与部署

#### ML 流水线

```
数据收集 → 数据处理 → 特征工程 → 模型训练 → 模型评估 → 模型部署 → 监控迭代
```

#### 模型部署方案

| 方案 | 说明 | 适用场景 |
|------|------|----------|
| FastAPI | Python Web API | 快速原型 |
| TorchServe | PyTorch官方服务 | PyTorch模型 |
| TFServing | TensorFlow官方服务 | TF模型 |
| Triton | NVIDIA推理服务器 | 高性能生产环境 |
| vLLM | LLM高性能推理 | 大模型部署 |
| Ollama | 本地LLM运行 | 个人/小团队 |

#### 推理优化技术

| 技术 | 说明 | 加速比 |
|------|------|--------|
| ONNX | 通用模型交换格式 | 1.5-3x |
| TensorRT | NVIDIA GPU优化 | 3-10x |
| 量化(INT8) | 降低精度 | 2-4x |
| 知识蒸馏 | 大模型→小模型 | 模型压缩 |
| 剪枝 | 移除冗余参数 | 模型压缩 |

#### 监控与迭代工具

| 工具 | 说明 |
|------|------|
| MLflow | 实验跟踪、模型管理 |
| Weights & Biases | 实验可视化 |
| DVC | 数据版本控制 |
| Kubeflow | K8s上的ML流水线 |
| Great Expectations | 数据质量监控 |

---

### 3.9 AI 基础设施与分布式训练

#### GPU 选型

| GPU | 厂商 | 显存 | 适用场景 |
|-----|------|------|----------|
| A100 | NVIDIA | 80GB HBM2e | 大模型训练主力 |
| H100 | NVIDIA | 80GB HBM3 | 新一代训练加速 |
| H200 | NVIDIA | 141GB HBM3e | 超大模型训练 |
| B200 | NVIDIA | 192GB HBM3e | Blackwell架构 |
| MI300X | AMD | 192GB HBM3 | NVIDIA竞品 |
| 昇腾910B | 华为 | 64GB HBM2e | 国产AI芯片 |

#### 分布式训练策略

| 策略 | 说明 | 框架 |
|------|------|------|
| 数据并行 | 数据分片到多GPU，梯度同步 | PyTorch DDP |
| 模型并行 | 模型层分到不同GPU | Megatron-LM |
| 流水线并行 | 模型层按阶段分配 | PipeDream |
| 张量并行 | 单层内部分割 | Megatron-LM |
| ZeRO | 分片优化器/梯度/参数 | DeepSpeed |

#### 训练优化技术

| 技术 | 说明 | 效果 |
|------|------|------|
| 混合精度训练 | FP16/BF16+FP32 | 2x加速，显存减半 |
| 梯度检查点 | 用计算换显存 | 显存大幅降低 |
| Flash Attention | IO感知的注意力 | 2-4x注意力加速 |
| 算子融合 | 合并多个操作 | 减少kernel调用 |
| 梯度累积 | 多步累积再更新 | 等效大batch |

---

### 3.10 混合专家模型 MoE

**核心原理**：
```
输入 → Gate网络(选择Top-K专家) → 激活的专家计算 → 加权求和 → 输出
```

**核心优势**：
- 稀疏激活：每次推理只激活部分专家，计算量远小于同等参数量的稠密模型
- 参数扩展：总参数量大但活跃参数少，兼顾容量和效率
- 代表模型：DeepSeek V3、Mixtral、Qwen MoE、Grok

**主流 MoE 模型**：

| 模型 | 公司 | 特点 |
|------|------|------|
| DeepSeek V3 | DeepSeek | 671B参数，37B激活，开源标杆 |
| Mixtral 8x7B | Mistral | 8个专家，Top-2激活 |
| Qwen MoE | 阿里 | 中文MoE模型 |
| Grok-1 | xAI | 314B参数MoE |

---

### 3.11 AI 安全与伦理

#### AI 对齐技术

| 技术 | 说明 |
|------|------|
| RLHF | 人类反馈强化学习 |
| DPO | 直接偏好优化（简化版RLHF） |
| Constitutional AI | Anthropic宪法AI |
| 红队测试 | 对抗性安全测试 |
| 可解释性 | 理解模型决策过程 |

#### 对抗攻击与防御

| 攻击类型 | 说明 | 防御方法 |
|----------|------|----------|
| 越狱攻击 | DAN、AutoDAN、GCG等绕过安全限制 | 输入过滤、输出审核 |
| 提示注入 | 在输入中嵌入恶意指令 | 输入清洗、分隔符 |
| 对抗样本 | 微小扰动导致误判 | 对抗训练、输入变换 |
| 数据投毒 | 训练数据中注入恶意样本 | 数据清洗、异常检测 |
| 模型窃取 | 通过API查询复制模型 | 速率限制、水印 |

#### 隐私保护技术

| 技术 | 说明 |
|------|------|
| 联邦学习 | 数据不出本地，模型聚合 |
| 差分隐私 | 添加噪声保护个体数据 |
| 同态加密 | 密文上直接计算 |
| 安全多方计算 | 多方协作不泄露各自数据 |

---

### 3.12 AI 法规与合规

#### 全球 AI 法规

| 法规 | 地区 | 要点 |
|------|------|------|
| EU AI Act | 欧盟 | 全球首部综合性AI法规，风险分级，2025年起分阶段生效 |
| 生成式AI管理办法 | 中国 | 2023年8月施行，规范生成式AI服务 |
| 算法推荐管理规定 | 中国 | 算法备案、透明度要求 |
| 深度合成管理规定 | 中国 | 规范AI换脸、语音合成 |
| AI安全治理框架 | 中国 | 2024年发布，分类分级治理 |
| NIST AI RMF | 美国 | AI风险管理框架 |

#### EU AI Act 风险分级

| 风险级别 | 说明 | 要求 |
|----------|------|------|
| 不可接受风险 | 社会评分、实时生物识别 | 禁止 |
| 高风险 | 医疗、招聘、司法AI | 严格合规要求 |
| 有限风险 | 聊天机器人、深度伪造 | 透明度义务 |
| 最小风险 | 垃圾邮件过滤、游戏AI | 无特殊要求 |

---

### 3.13 AI 商业化与创业

#### AI SaaS 商业模式

| 模式 | 说明 | 代表 |
|------|------|------|
| API收费 | 按调用量计费 | OpenAI API |
| 订阅制 | 月/年费 | ChatGPT Plus |
| Freemium | 免费+付费增值 | Notion AI |
| 企业定制 | 私有化部署+定制 | 百度文心 |
| PLG | 产品驱动增长 | Cursor |

#### 2025-2026 AI 创业趋势

| 趋势 | 说明 |
|------|------|
| AI Agent | 智能体成为新的应用范式 |
| Vertical AI SaaS | 垂直行业AI解决方案 |
| AI-native应用 | 从AI-first设计产品 |
| 端侧AI | 本地化AI部署需求增长 |
| 数据飞轮 | 用户数据持续优化模型 |

---

## 4. 深度学习框架对比

| 特性 | PyTorch | TensorFlow | JAX |
|------|---------|------------|-----|
| 易用性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 学术研究 | ⭐⭐⭐⭐⭐ (80%+论文) | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 工业部署 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 动态图 | ✅ 默认 | ✅ TF2支持 | ✅ 函数式 |
| 社区 | 快速增长 | 成熟庞大 | 学术前沿 |

---

## 5. 端侧 AI 与边缘计算

### 端侧 AI 芯片

| 芯片 | 厂商 | 特点 |
|------|------|------|
| Snapdragon 8 Gen 3 | 高通 | 端侧支持LLM（Llama 2 7B） |
| 天玑9300 | 联发科 | 第七代APU，生成式AI |
| A17 Pro / M系列 | 苹果 | Neural Engine持续升级 |
| 昇腾310/910 | 华为 | 国产AI芯片 |
| Jetson系列 | NVIDIA | 边缘AI计算平台 |

### 模型压缩技术

| 技术 | 说明 | 压缩比 |
|------|------|--------|
| 量化 | FP32→FP16/INT8/INT4 | 2-8x |
| 剪枝 | 移除冗余参数 | 2-10x |
| 知识蒸馏 | 大模型→小模型 | 模型压缩 |
| NAS | 神经架构搜索 | 自动优化 |

### 端侧部署框架

| 框架 | 来源 | 适用平台 |
|------|------|----------|
| TensorFlow Lite | Google | Android/iOS/嵌入式 |
| ONNX Runtime | Microsoft | 跨平台 |
| NCNN | 腾讯 | 移动端高性能 |
| MNN | 阿里 | 移动端推理 |
| llama.cpp | 开源 | CPU端侧LLM |
| MLC-LLM | 开源 | 多平台LLM部署 |
| ExecuTorch | Meta | PyTorch端侧部署 |

> **2025-2026趋势**：4-bit/2-bit量化(GPTQ/AWQ/GGUF)在端侧LLM部署中广泛应用，手机可运行7B参数大模型。

---

## 6. 具身智能

**定义**：将大语言模型（LLM）与物理机器人身体相结合的AI研究方向，让AI能够感知、理解并与物理世界交互。

**人形机器人代表**：

| 公司 | 产品 | 特点 |
|------|------|------|
| Figure AI | Figure 02/03 | OpenAI合作，AI驱动 |
| Tesla | Optimus | 自动驾驶技术迁移 |
| Boston Dynamics | Atlas(电动版) | 运动控制标杆 |
| 宇树科技 | Unitree H1/G1 | 中国人形机器人 |
| 优必选 | Walker X | 商业化探索 |
| 智元机器人 | 远征A2 | AI+机器人融合 |

**关键技术**：多模态感知、LLM规划、运动控制、仿真环境(Isaac Sim/MuJoCo)、端到端学习

---

## 7. AI 面试题精选

### 机器学习

| 问题 | 关键点 |
|------|--------|
| Bias-Variance Tradeoff | 偏差-方差权衡，欠拟合vs过拟合 |
| L1/L2正则化区别 | L1稀疏(特征选择)、L2平滑(防止过拟合) |
| 梯度下降变种 | SGD、Mini-batch、Adam、AdamW |
| 决策树 vs 随机森林 vs XGBoost | 单树→Bagging→Boosting |
| SVM核函数 | 线性核、RBF核、多项式核 |

### 深度学习

| 问题 | 关键点 |
|------|--------|
| CNN工作原理 | 卷积(特征提取) → 池化(降维) → 全连接(分类) |
| RNN/LSTM/GRU区别 | LSTM门控机制解决长距离依赖 |
| Transformer注意力机制 | Q·K^T/√d_k → softmax → 加权V |
| BatchNorm vs LayerNorm | BN按batch、LN按特征，Transformer用LN |
| ResNet残差连接 | 解决退化问题，y = F(x) + x |

### 大模型

| 问题 | 关键点 |
|------|--------|
| GPT和BERT的区别 | Decoder自回归 vs Encoder双向理解 |
| RAG原理 | 检索+生成，解决幻觉和知识时效 |
| LoRA微调原理 | 低秩矩阵分解，减少可训练参数 |
| RLHF流程 | SFT→奖励模型→PPO优化 |
| Prompt Engineering | Few-shot、CoT、ReAct |

---

## 8. 推荐学习资源

### 课程推荐

| 课程 | 平台 | 方向 |
|------|------|------|
| 吴恩达 Machine Learning | Coursera | ML入门经典 |
| 吴恩达 Deep Learning Specialization | Coursera | 深度学习5门课 |
| 李宏毅 机器学习 | B站/YouTube | 中文最佳ML课程 |
| CS229 (Stanford) | YouTube | ML理论深入 |
| CS231n (Stanford) | YouTube | 计算机视觉 |
| CS224N (Stanford) | YouTube | NLP |
| CS285 (UC Berkeley) | YouTube | 深度强化学习 |
| Fast.ai | fast.ai | 实践导向DL |

### 经典论文

| 论文 | 年份 | 意义 |
|------|------|------|
| Attention Is All You Need | 2017 | Transformer架构 |
| BERT | 2018 | 预训练语言模型 |
| GPT-2/GPT-3 | 2019/2020 | 大规模语言模型 |
| ResNet | 2015 | 残差连接 |
| GAN | 2014 | 生成对抗网络 |
| DDPM | 2020 | 扩散模型 |
| LoRA | 2021 | 高效微调 |
| CLIP | 2021 | 图文对齐 |
| ViT | 2020 | Transformer用于视觉 |
| InstructGPT/RLHF | 2022 | 大模型对齐 |

### 学习平台

Kaggle（数据竞赛）、HuggingFace（模型库）、d2l.ai（在线深度学习）、arXiv（最新论文）、Papers With Code（论文+代码）、百度AI Studio（中文AI学习平台）

---

## 9. 场景脚本

### 场景一：AI 初学者学习路径规划

**用户**：我是零基础，想学 AI，怎么开始？

**执行流程**：
1. 评估用户当前水平和目标
2. 推荐学习路线图第 1-2 阶段（基础 + 入门）
3. 推荐课程：吴恩达 Machine Learning + 李宏毅机器学习
4. 推荐实践：Kaggle 入门赛
5. 给出 3 个月学习计划

### 场景二：技术选型咨询

**用户**：我要部署一个 7B 大模型到生产环境，选什么方案？

**执行流程**：
1. 评估需求：推理性能、显存预算、并发要求
2. 对比部署方案：vLLM vs Ollama vs Triton
3. 推荐推理优化：量化(INT8) + TensorRT
4. 给出监控方案：MLflow + W&B
5. 提供配置建议和代码示例

### 场景三：RAG 系统设计

**用户**：我要搭建一个企业知识库问答系统，怎么设计？

**执行流程**：
1. 分析需求：文档规模、更新频率、准确率要求
2. 推荐架构：LangChain + 向量数据库 + LLM
3. 对比向量数据库：Milvus vs Chroma vs Qdrant
4. 设计 RAG 流水线：文档加载 → 分块 → 向量化 → 检索 → 生成
5. 提供代码示例和优化建议

### 场景四：AI 面试准备

**用户**：我要面试大模型算法工程师，需要准备什么？

**执行流程**：
1. 列出高频面试题分类（ML/DL/LLM）
2. 提供关键问题答案要点
3. 推荐重点论文阅读清单
4. 给出代码实践建议（PyTorch + LoRA 微调）
5. 提供模拟面试问题

---

## 10. Gotchas（踩坑记录）

1. **PyTorch vs TensorFlow 选型**：学术研究选 PyTorch（80%+论文使用），工业部署看团队积累，新项目建议 PyTorch + TorchServe
2. **LoRA 微调不是万能的**：适合轻量微调，但对领域知识注入有上限；全量微调效果更好但成本极高
3. **RAG 不是简单接向量数据库**：分块策略、chunk_overlap、embedding 模型选择、重排序都会显著影响效果
4. **量化精度损失**：INT8 量化通常损失 <1%，但 INT4 需要仔细验证关键任务
5. **Agent 不是万能管家**：当前 Agent 仍需人类监督，复杂任务拆解质量取决于 LLM 推理能力
6. **MoE 不一定更快**：虽然稀疏激活减少计算量，但 Gate 网络路由和专家负载不均可能导致实际加速不如预期
7. **端侧 AI 不是简单压缩模型**：需要考虑芯片 NPU 兼容性、量化格式支持、推理框架适配
8. **EU AI Act 合规**：2025 年起分阶段生效，高风险 AI 系统需提前 6-12 个月准备合规

---

## 11. 技能路径

`C:\Users\22812\.trae\skills\ai-knowledge-compendium\SKILL.md`

---

*基于《AI人工智能知识大全 - 全方向深度指南》（洞察AI-Onlyone, 2026）封装*
*原文件来源：https://ai.huamp.com*
