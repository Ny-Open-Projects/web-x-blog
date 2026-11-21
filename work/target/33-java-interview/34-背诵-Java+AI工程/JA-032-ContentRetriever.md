---
title: "[JA-032] LangChain4j·ContentRetriever（RAG）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · ContentRetriever（RAG）

- **事实**：LangChain4j 的 RAG 接口是 ContentRetriever，EmbeddingStoreContentRetriever 为向量检索实现
- **原理**：AiServices.contentRetriever(...) 挂载后提问自动检索注入，换检索源只换实现类
- **常见误区**：
  1. RAG 必须手写检索与拼接（错）
  2. ContentRetriever 是文档加载器（错）
  3. 挂载后不再使用模型（错）
- **工程用法**：RAG 管道装配
- **版本锚点**：LangChain4j 1.0
