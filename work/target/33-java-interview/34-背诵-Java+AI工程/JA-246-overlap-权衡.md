---
title: "[JA-246] RAG·overlap 权衡（切分）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## RAG · overlap 权衡（切分）

- **事实**：chunk overlap 的权衡：跨边界语义保留（正）vs 内容重复稀释（负），重叠通常取 chunk 的 10-20%
- **原理**：重叠过大让相似检索返回重复内容挤占 topK（JA-052 联动），重叠为零则切断关键句
- **常见误区**：
  1. overlap 越大越好（错）
  2. 重叠没有代价（错）
  3. overlap 必须 50%（错）
- **工程用法**：切分参数权衡
- **版本锚点**：实战共识
