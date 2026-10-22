# 34. 课程全景回顾：RAG 全栈五大模块思维导图

## 纲要

- **课程总览（五大模块）**：① RAG 三大组件（大模型 / 知识库 / 检索）；② RAG 评估；③ RAG + 扩展（Graph RAG / agenticRAG / 微调）；④ RAG 实战项目（erag 企业员工助手）；⑤ AI 应用开发软技能。
- **模块一·大模型**：自回归接龙（预测 next token）、token 与分词、Transformer + self-attention、训练三阶段（预训练/SFT/RLHF）、国内外模型、选型四标准（模型大小/能力评测/推理成本/部署设备+数据安全决定本地 or 第三方）、GPU 原理、三种调用（transformers / Ollama / 厂商 API，均支持流式）。
- **模块一·知识库**：Embedding（BERT 架构、MLM+NSP 训练、MTEB 基准、中文 GTE/BGE 加度量+对比学习、三种调用、相似度/聚类应用）；向量数据库（Chroma 易用小规模 vs Milvus 云原生分布式，索引 Flat/IVF/PQ/HNSW，使用五步：连接-元数据-建集合-建索引-查询）；文件解析分块（垃圾进垃圾出、PDF/HTML/Markdown/JSON/Office 解析、RAGFlow deepDOC 视觉解析、递归/embedding/模型语义分块）；图数据库（三元组、Neo4j vs NebulaGraph、Cypher、py2neo）。
- **模块一·检索（14 种增强）**：查询增强 5 法（Query2doc/HyDE/子问题/改写/Step Back）；多索引 3 法（父文档/总结/假设问题）；检索后 2 法（Re-rank / 稀疏+稠密融合 RRF）；系统性 2 法（迭代检索增强生成 / Self-RAG）。
- **模块二·评估**：三大标准（忠实性 / 答案相关性 / 上下文相关性）；Ragas 四指标（忠实性 / 答案相关性 / 上下文召回 / 上下文精度）；三步（建数据集→选指标→执行）；评估驱动迭代优化（有的放矢）。
- **模块三·扩展**：Graph RAG（多跳/语义关联/综合查询，构建3步：提关键词→图谱检索→LLM 生成）；agenticRAG（ReAct：Thought/Action/Observation，实现 RAG Router 自动切换）；模型微调（LoRA 参数高效，框架如 SWIFT/LLaMA-Factory 全流程：数据准备-调参-训练-跟踪-评估；原则：非必要不微调）。
- **模块四·实战**：erag 企业员工助手（制度问答 RAG + 金融智库 Graph RAG + Router 三模块整合，Gradio 界面 + FastAPI/uvicorn 多进程部署）。
- 本章按课程口径重构；产品/框架名已规范化（RAGFlow/LightRAG/VisualRAG/Ragas/MTEB/GTE/BGE/Chroma/Milvus/Neo4j/NebulaGraph/SWIFT/LLaMA-Factory）；剥离营销与课程群引流。

## 一、RAG 三大组件

| 组件 | 核心知识点 |
| --- | --- |
| 大模型 | 自回归/token/Transformer+self-attention/训练三阶段(预训练·SFT·RLHF)/国内外模型/选型四标准(大小·评测·成本·安全部署)/GPU/三种调用(transformers·Ollama·API·均流式) |
| 知识库 | Embedding(BERT·MLM+NSP·MTEB·GTE/BGE)/向量库(Chroma vs Milvus·索引 Flat/IVF/PQ/HNSW·五步用法)/文件解析分块(GIGO·多格式·deepDOC·递归/语义分块)/图数据库(三元组·Neo4j/Nebula·Cypher·py2neo) |
| 检索 | 14 种增强：查询增强5/多索引3/检索后2(Re-rank·RRF)/系统性2(迭代·Self-RAG) |

## 二、RAG 评估（最重要环节）

- **为什么最重要**：决定系统能否上线；评估不通过时结果为优化指明方向，让迭代「有的放矢」而非无头苍蝇。
- **三大标准**：忠实性（答案↔上下文事实一致）、答案相关性（答案↔问题）、上下文相关性（上下文↔问题）。
- **Ragas 四指标**：忠实性、答案相关性、上下文召回、上下文精度（含排序权重）。
- **三步**：建评估数据集 → 选指标 → 执行；据结果针对性迭代优化。

## 三、RAG 三大扩展

1. **Graph RAG**：借图库强关联数据做多跳/语义关联/综合查询；构建三步走（提关键词→图谱检索实体关系→LLM 生成）。
2. **agenticRAG**：ReAct（Thought/Action/Observation 循环），实现 RAG Router 按问题智能选 pipeline。
3. **模型微调**：大模型与 Embedding 微调；LoRA 参数高效；框架（SWIFT/LLaMA-Factory）全流程；**原则：非必要不微调**。

## 四、实战与软技能

- **erag 企业员工助手**：制度问答 RAG + 金融智库 Graph RAG + Router 整合，Gradio 界面 + FastAPI/uvicorn 多进程部署，对外提供完整服务。
- **软技能**：贯穿课程的 AI 应用开发工程素养（代码规范、git 管理、beta 思维等）。

## 五、FAQ

**Q1：课程五大模块是哪些？**
RAG三大组件、评估、扩展(Graph/agentic/微调)、实战 erag、软技能。

**Q2：RAG 为什么评估最关键？**
它决定能否上线，并给优化指明方向，让迭代有的放矢。

**Q3：14 种检索增强怎么分？**
查询增强5 + 多索引3 + 检索后2(Re-rank/RRF) + 系统性2(迭代/Self-RAG)。

**Q4：微调的原则？**
非必要不微调——微调有成本，先试换模型/换库/加 Re-rank 等低成本手段。

## 六、面试高频问答

**1. RAG 三大组件？**
大模型（生成）、知识库（Embedding+向量库+解析分块+图库）、检索（增强）。

**2. 评估三大标准 + Ragas 四指标？**
标准：忠实性/答案相关性/上下文相关性；指标：忠实性/答案相关性/上下文召回/上下文精度。

**3. RAG 扩展三方向？**
Graph RAG（多跳）、agenticRAG（ReAct Router）、模型微调（LoRA）。

**4. 实战 erag 含哪三模块？**
制度问答 RAG + 金融智库 Graph RAG + RAG Router，Gradio 整合部署。

## 七、ops 提示（增效）

> **学完本课程的能力基线**：已具备从选型→建库→检索增强→评估→Graph/Agent 扩展→界面部署的完整 RAG 全栈视野。
>
> **扩展学习无障碍**：在此基线上可直读 LightRAG / VisualRAG / 多模态 RAG 等前沿，无需补基础。
>
> **微调是最后手段**：先用评估定位瓶颈，换 Embedding/加 Re-rank/换 LLM 多试几轮，再考虑微调。

