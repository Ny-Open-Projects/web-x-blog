---
title: "[JC-058] 并发容器·null（CHM）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 并发容器 · null（CHM）

- **事实**：ConcurrentHashMap 不允许 null 键与 null 值
- **原理**：并发下 get 返回 null 无法区分"键不存在"与"值就是 null"，HashMap 单线程可用 containsKey 二次确认，CHM 不行所以直接禁止
- **常见误区**：
  1. CHM 可以存 null 值（错）
  2. 禁止 null 是性能原因（错）
  3. TreeMap 也不允许 null 键（错）
- **工程用法**：向 CHM put null 编译不报错运行时 NPE
- **版本锚点**：JDK 文档
