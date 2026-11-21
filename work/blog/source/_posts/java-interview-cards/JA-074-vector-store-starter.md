---
title: "[JA-074] Spring AI·vector store starter（向量）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · vector store starter（向量）

- **事实**：向量库以 starter 集成（如 spring-ai-starter-vector-store-pgvector），自动装配对应 VectorStore bean
- **原理**：换向量库换 starter 依赖与连接配置即可，业务面向 VectorStore 接口
- **常见误区**：
  1. 向量库需要手写连接代码（错）
  2. starter 只支持一种库（错）
  3. 装配后不能有多个 VectorStore（错）
- **工程用法**：生产向量库接入
- **版本锚点**：Spring AI 1.0 GA
