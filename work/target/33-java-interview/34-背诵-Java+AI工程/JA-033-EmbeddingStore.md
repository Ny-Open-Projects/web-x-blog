---
title: "[JA-033] LangChain4j·EmbeddingStore（向量）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · EmbeddingStore（向量）

- **事实**：LangChain4j 的向量抽象是 EmbeddingStore<TextSegment>，内置 InMemoryEmbeddingStore 等实现
- **原理**：pgvector/Milvus/Chroma 等以独立模块提供，接口统一换库不改代码，与 Spring AI 的 VectorStore 同思想
- **常见误区**：
  1. EmbeddingStore 存原始文档字符串（错）
  2. 内置实现可承载生产（错）
  3. 换库需要重写业务（错）
- **工程用法**：向量库选型自由度
- **版本锚点**：LangChain4j 1.0
