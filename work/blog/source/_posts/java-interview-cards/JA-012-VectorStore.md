---
title: "[JA-012] Spring AI·VectorStore（向量）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · VectorStore（向量）

- **事实**：VectorStore 接口两个核心动作：add(List<Document>) 写入与 similaritySearch(SearchRequest) 检索
- **原理**：检索参数在 SearchRequest 上（query/topK/similarityThreshold），接口统一所以换向量库不改业务代码
- **常见误区**：
  1. VectorStore 自带嵌入能力无需 EmbeddingModel（错）
  2. similaritySearch 返回完整文档集合不带相似度（错）
  3. add 接收字符串（错）
- **工程用法**：RAG 存取标准动作
- **版本锚点**：Spring AI 1.0 GA
