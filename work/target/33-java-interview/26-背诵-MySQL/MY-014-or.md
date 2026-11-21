---
title: "[MY-014] 索引·or（失效）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 索引 · or（失效）

- **事实**：or 两边有一侧无索引则整体走全表扫描（union 可绕开）
- **原理**：or 语义要求两侧结果并集，一侧全扫则另一侧索引无意义，改写 union all 各走各的索引
- **常见误区**：
  1. or 有索引一侧会走索引（错）
  2. or 与 in 等价（in 单列枚举可走索引）（错）
  3. or 优化只能靠改写 SQL（错）
- **工程用法**：SQL 改写手法之一
- **版本锚点**：实战共识
