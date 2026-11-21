---
title: "[JA-013] Spring AI·SimpleVectorStore（向量）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · SimpleVectorStore（向量）

- **事实**：SimpleVectorStore 是 Spring AI 内置的内存向量库实现
- **原理**：零依赖快速起 RAG（开发/测试），生产换 pgvector/Milvus/Chroma 等 starter 实现，接口不变
- **常见误区**：
  1. SimpleVectorStore 可持久化生产使用（错）
  2. 内置向量库性能接近专用库（错）
  3. 换向量库要改业务代码（错）
- **工程用法**：开发环境 RAG 快速验证
- **版本锚点**：Spring AI 1.0 GA
