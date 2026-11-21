---
title: "[JC-092] JMM·double（64 位）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## JMM · double（64 位）

- **事实**：非 volatile 的 long 与 double 读写可能不是原子的（字撕裂）
- **原理**：JLS 允许 64 位读写分两半执行，并发下可能读到高 32 位新值加低 32 位旧值，声明 volatile 即可保证原子性
- **常见误区**：
  1. 所有基本类型读写都是原子的（错）
  2. long 读写撕裂只在 32 位 JVM 发生（错）
  3. long 撕裂会导致崩溃（错）
- **工程用法**：跨线程共享的 long 计数加 volatile
- **版本锚点**：JLS 17.7
