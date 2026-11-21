---
title: "[MG-021] 索引·sparse（sparse）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 索引 · sparse（sparse）

- **事实**：sparse 索引跳过不含该字段的文档
- **原理**：与 partial 的区别：按字段存在性过滤（partial 按任意表达式），组合查询行为注意（不含字段文档查不到）
- **常见误区**：
  1. sparse 与 partial 相同（错）
  2. sparse 索引所有文档（错）
  3. sparse 会自动填充字段（错）
- **工程用法**：字段稀疏集合优化
- **版本锚点**：官方文档
