---
title: "[JB-039] CHM·null拒绝（误用）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## CHM · null拒绝（误用）

- **事实**：ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。
- **原理**：并发环境下 get 返回 null 存在"不存在"与"值为 null"的二义性。
- **常见误区**：
  1. CHM 允许一个 null key 与多个 null 值。（错）
  2. CHM 的 null 处理与 HashMap 完全相同。（错）
  3. CHM 会把 null 转换为默认值存储。（错）
- **工程用法**：二义性论证是二面高频考点。
- **版本锚点**：CHM javadoc
