---
title: "[JB-035] HashMap·null键（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## HashMap · null键（语法语义）

- **事实**：HashMap 允许最多一个 null 键（放在 table[0] 桶），null 值不限。
- **原理**：hash(null) 返回 0，直接落在 0 号桶。
- **常见误区**：
  1. HashMap 不允许 null 键。（错）
  2. HashMap 允许多个 null 键。（错）
  3. HashMap 的 null 键会抛 NPE。（错）
- **工程用法**：对比：Hashtable 与 CHM 都拒绝 null 键。
- **版本锚点**：JDK 8+ 源码
