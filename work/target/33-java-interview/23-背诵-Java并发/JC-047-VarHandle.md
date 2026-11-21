---
title: "[JC-047] 原子类·VarHandle（语义）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 原子类 · VarHandle（语义）

- **事实**：JDK9 引入 VarHandle 替代 Unsafe 提供安全的字段级原子操作
- **原理**：提供 getAndSet、compareAndSet、getAndAddRelease 等带内存语义的方法，且模块系统下不依赖内部 API
- **常见误区**：
  1. VarHandle 只能读写字段（错）
  2. Unsafe 在 JDK9 后被删除（错）
  3. VarHandle 与 AtomicInteger 能力不同级（错）
- **工程用法**：新代码用 VarHandle 与 MethodHandles
- **版本锚点**：JEP 193
