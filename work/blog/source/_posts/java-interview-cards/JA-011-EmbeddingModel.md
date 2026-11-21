---
title: "[JA-011] Spring AI·EmbeddingModel（向量）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · EmbeddingModel（向量）

- **事实**：EmbeddingModel.embed("文本") 返回 float[] 向量，支持批量 embed(List)
- **原理**：嵌入模型抽象屏蔽厂商差异（OpenAI/Ollama 等），向量喂给 VectorStore 做检索
- **常见误区**：
  1. embed 返回 String（错）
  2. 嵌入不需要网络调用（错）
  3. float[] 与 List<Double> 等价混用（错）
- **工程用法**：RAG 管道第一步
- **版本锚点**：Spring AI 1.0 GA
