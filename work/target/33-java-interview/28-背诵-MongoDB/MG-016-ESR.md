---
title: "[MG-016] 索引·ESR（原则）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 索引 · ESR（原则）

- **事实**：复合索引设计 ESR 原则：Equality 等值→Sort 排序→Range 范围
- **原理**：等值列保证排序连续性，范围列放最后，官方设计原则（与 MySQL 联合索引原则同构）
- **常见误区**：
  1. R 应该放最前（错）
  2. S 在 E 前（错）
  3. ESR 只适用聚合查询（错）
- **工程用法**：索引设计口诀
- **版本锚点**：官方文档
