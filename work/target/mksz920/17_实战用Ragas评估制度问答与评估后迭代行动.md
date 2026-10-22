# 17. 实战用 Ragas 评估制度问答与评估后迭代行动

## 纲要

- **实战目标**：在已构建的制度问答 RAG 上，用 Ragas 自动评估性能（除人工评估外）。
- **重建 RAG pipeline**：引入 embedding + LLM + Chroma 检索；加载「制度 DB」向量集合（传 Chroma 连接与 embedding 函数）；pipeline 给定问题 → 检索 k 个文档 → 拼接上下文 + 问题入 prompt → LLM 生成答案，**同时返回上下文列表**供评估使用。
- **构建评估数据集**：四部分 = 问题、GT 标准答案（手动提供）、检索上下文与生成答案（由 pipeline 产出）；把两问题送入 pipeline（k=3）收集答案与上下文 → 组装成 `Dataset`（问题 / 答案 / 上下文 / GT）。
- **选择四指标**：忠实性、答案相关性、上下文召回、上下文精度。
- **执行评估**：实例化 LLM（Qwen2-72B）+ embedding（BGE-M3）；因评估多次调 LLM 较耗时，配置文件加长超时；`evaluate` 传入 dataset / LLM / embedding / 指标 / 配置 → 结果转表格。
- **结果解读与迭代**：示例结果中检索上下文质量高；第二问的忠实性、答案相关性略差；实际项目需生成更多问题（可用 LLM 自动生成）覆盖多场景。
- **评估后行动（关键）**：符合预期 → 上线；不符合 → 分析 badcase 定因（检索精度 / 召回差 → 改进检索或换 embedding；答案问题 → 改写 prompt 或换 LLM）→ 重新评估 → 多轮迭代至达标 → 上线。
- 本章按课程口径重构；产品 / 框架名已规范化（Ragas / Chroma / Qwen2-72B / BGE-M3）；剥离营销与课程群引流。

## 一、重建可评估的 RAG pipeline

- 加载已构建的 Chroma「制度 DB」知识库（传连接 + embedding 函数）。
- pipeline 逻辑：问题 → 检索 k=3 相关文档 → 拼 `page_content` 为大上下文 → 填入 prompt → LLM 生成答案；**同时把上下文列表返回**，供 Ragas 取用。

## 二、构建评估数据集

- 手动提供：问题 + GT 标准答案（至少覆盖代表性场景；生产中要更多问题，可用 LLM 自动生成扩充）。
- 自动产出：把问题送入 pipeline，收集生成答案与检索上下文列表。
- 四元组组装成 Ragas `Dataset`：问题 / 生成答案 / 上下文（**顺序即排序**）/ GT。

## 三、执行 Ragas 评估

```python
from ragas import evaluate
from datasets import Dataset
# 指标：faithfulness, answer_relevance, context_recall, context_precision
dataset = Dataset.from_dict({"question":..., "answer":..., "contexts":..., "ground_truth":...})
result = evaluate(dataset, metrics=[...], llm=llm, embeddings=emb, run_config=timeout_cfg)
```
- LLM 用 Qwen2-72B、embedding 用 BGE-M3；评估多次调用 LLM，需调长超时。
- 结果示例：上下文质量高；第二问忠实性、答案相关性略差。

## 四、评估后如何迭代

- **符合预期** → 上线部署。
- **不符合** → 定位 badcase：
 - 上下文召回 / 精度差 → 改进检索方式、替换 embedding 模型；
 - 答案有问题时 → 改写生成 prompt、或换 LLM。
- 提出方案后**重新评估验证**，多轮迭代直到达标，再上线。
- 生产应生成更多问题覆盖多样场景（可借 LLM 自动生成）。

## 五、FAQ

**Q1：Ragas 评估为什么要让 pipeline 返回上下文？**
四大指标都依赖检索到的上下文（含排序），pipeline 必须把上下文列表回传。

**Q2：为什么评估耗时要加长超时？**
Ragas 对每题多次调用 LLM（拆分 / 推断 / 生成潜在问题），累计耗时大。

**Q3：评估后第一件事做什么？**
看指标定位问题类型：检索类（召回/精度）还是生成类（忠实/答案相关性），再对症优化。

**Q4：生产中测试集要多大？**
至少覆盖主要提问场景，并可用 LLM 自动生成大量问题扩充，避免只测两题。

## 六、面试高频问答

**1. 用 Ragas 评估 RAG 的基本流程？**
重建返回上下文的 pipeline → 组装 问题/答案/上下文/GT 的 Dataset → 选四指标 → evaluate 算分。

**2. 评估后指标差怎么迭代？**
召回/精度差→改检索或换 embedding；忠实/答案相关性差→改 prompt 或换 LLM；再评估验证。

**3. 为什么生产要更多评估问题？**
两题覆盖不足，需用 LLM 自动生成多场景问题，才能真实反映系统性能。

**4. Ragas 数据集四元组？**
问题、生成答案、检索上下文（顺序=排序）、人工标准答案 GT。

## 七、ops 提示（增效）

> **pipeline 必备返回上下文**：没上下文列表，Ragas 四大指标算不了。
>
> **超时别默认**：评估多轮调 LLM，务必加长 run_config 超时。
>
> **先诊断再改**：指标差先分「检索类 vs 生成类」，对症改 embedding/prompt，避免盲调。

