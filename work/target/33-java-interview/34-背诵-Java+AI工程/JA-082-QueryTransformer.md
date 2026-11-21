---
title: "[JA-082] LangChain4j·QueryTransformer（查询改写）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · QueryTransformer（查询改写）

- **事实**：QueryTransformer 把对话历史压缩成独立检索查询（如 CompactingQueryTransformer）
- **原理**：对话式提问直接检索效果差（指代不明），改写为自包含查询提升召回，是高级 RAG 的第一环
- **常见误区**：
  1. 检索查询必须原样使用（错）
  2. QueryTransformer 是日志组件（错）
  3. 改写会破坏语义（错）
- **工程用法**：多轮 RAG 召回优化
- **版本锚点**：LangChain4j 1.0
