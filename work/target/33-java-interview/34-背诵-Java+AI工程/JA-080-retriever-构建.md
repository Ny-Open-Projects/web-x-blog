---
title: "[JA-080] LangChain4j·retriever 构建（检索）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · retriever 构建（检索）

- **事实**：EmbeddingStoreContentRetriever.builder().embeddingStore(...).embeddingModel(...).maxResults(k).minScore(t).build()
- **原理**：检索参数 builder 声明（数量/分数下限），与 Spring AI 的 SearchRequest 同思想，面向接口可替换
- **常见误区**：
  1. 检索参数不可配置（错）
  2. maxResults 无上限（错）
  3. 构建必须静态（错）
- **工程用法**：RAG 检索精调
- **版本锚点**：LangChain4j 1.0
