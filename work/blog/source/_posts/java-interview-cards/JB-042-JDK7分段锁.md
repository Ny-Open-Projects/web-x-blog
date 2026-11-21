---
title: "[JB-042] CHM·JDK7分段锁（版本）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## CHM · JDK7分段锁（版本）

- **事实**：JDK7 的 CHM 用 Segment 分段锁（默认 16 段，段继承 ReentrantLock），并发度等于段数。
- **原理**：分段把锁竞争分散，但并发度上限固定、hash 到同段的操作仍串行。
- **常见误区**：
  1. JDK7 的 CHM 没有任何锁。（错）
  2. JDK7 的 CHM 并发度等于数组长度。（错）
  3. JDK7 与 JDK8 的实现完全相同。（错）
- **工程用法**："JDK7→8 重构原因"是并发面试的分水岭题。
- **版本锚点**：JDK 7→8 版本史
