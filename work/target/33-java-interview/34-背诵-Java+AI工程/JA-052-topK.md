---
title: "[JA-052] RAG·topK（检索）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## RAG · topK（检索）

- **事实**：检索参数治理：topK 与相似度阈值决定注入上下文的量，量大→token 贵且噪声多，量小→漏答案
- **原理**：Java 侧在 SearchRequest/retriever 配置，按业务调参并进评估集回归（AI-082 指标），是 RAG 调优第一旋钮
- **常见误区**：
  1. topK 越大越好（错）
  2. 阈值不需要调（错）
  3. 参数一次性设定永久有效（错）
- **工程用法**：RAG 调参方法论
- **版本锚点**：实战共识
