---
title: "[JA-102] RAG·rerank（重排）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## RAG · rerank（重排）

- **事实**：检索与重排分离：向量召回 topK 较大（如 20）再由重排模型精排出少量（如 3）注入上下文
- **原理**：重排模型（交叉编码）精度高但慢，只处理少量候选；Java 侧 LC4j 有 ScoringModel 抽象，Spring AI 可经服务 API 接入
- **常见误区**：
  1. 重排是必选步骤（错）
  2. rerank 模型处理全库（错）
  3. topK 直接给模型最优（错）
- **工程用法**：RAG 质量进阶
- **版本锚点**：实战共识
