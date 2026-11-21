---
title: "[AI-009] RAG·rerank（重排）"
date: 2026-11-18
categories: [Java面试, AI应用]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## RAG · rerank（重排）

- **事实**：重排（rerank）：用交叉编码模型对召回的 top 20-50 精排取 top 3-5
- **原理**：召回模型（双塔）快但粗，重排模型（交叉编码）准但慢（只处理少量候选），两段式兼顾质量与延迟，RAG 效果提升明显的一环
- **常见误区**：
  1. rerank 可以省略（错）
  2. rerank 越多越好（错）
  3. rerank 与召回相同（错）
- **工程用法**：检索精排
- **版本锚点**：实战共识
