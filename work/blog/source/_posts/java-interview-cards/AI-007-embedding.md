---
title: "[AI-007] RAG·embedding（嵌入）"
date: 2026-11-18
categories: [Java面试, AI应用]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## RAG · embedding（嵌入）

- **事实**：embedding 把文本映射为高维向量（语义相近距离近），检索用向量相似度（cosine）
- **原理**：嵌入模型决定检索质量（bge/text-embedding 系列），跨模型向量不兼容（换模型需全量重嵌入），维度常用 768-1536
- **常见误区**：
  1. embedding 是关键词匹配（错）
  2. 向量可跨模型混用（错）
  3. 相似度就是字面相似（错）
- **工程用法**：向量检索原理
- **版本锚点**：实战共识
