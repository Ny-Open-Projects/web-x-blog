---
title: "[JB-040] CHM·size计数（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## CHM · size计数（语法语义）

- **事实**：CHM 的 size 通过 baseCount + CounterCell[] 分段计数，返回的是近似值。
- **原理**：计数分散避免单点 CAS 热点（LongAdder 同源思想）。
- **常见误区**：
  1. CHM 的 size() 返回精确值。（错）
  2. CHM 用一个 volatile int 记录 size。（错）
  3. CHM 的 size 计算需要加全局锁。（错）
- **工程用法**：强一致 size 需求要自行加锁或换数据结构。
- **版本锚点**：JDK 8 源码
