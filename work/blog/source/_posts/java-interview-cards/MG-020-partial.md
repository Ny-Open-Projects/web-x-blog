---
title: "[MG-020] 索引·partial（partial）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 索引 · partial（partial）

- **事实**：partial 索引只索引满足条件的文档（如只索引 status=active）
- **原理**：省空间与写放大，查询条件必须匹配过滤表达式才能用上该索引，部分条件高频的集合优化
- **常见误区**：
  1. partial 索引所有查询都能用（错）
  2. partial 是稀疏索引的别名（错）
  3. partial 不省空间（错）
- **工程用法**：索引空间优化
- **版本锚点**：官方文档
