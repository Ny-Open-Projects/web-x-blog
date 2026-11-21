---
title: "[JC-023] ThreadLocal·ThreadLocalMap（内存语义）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## ThreadLocal · ThreadLocalMap（内存语义）

- **事实**：每个 Thread 内部持有 ThreadLocalMap 以 ThreadLocal 为 key
- **原理**：数据实际存在线程对象里，多个线程访问同一个 ThreadLocal 变量读到的是各自的副本，天然隔离
- **常见误区**：
  1. ThreadLocal 数据存在 ThreadLocal 对象里（错）
  2. ThreadLocalMap 是 HashMap 的子类（错）
  3. ThreadLocal 通过加锁实现线程隔离（错）
- **工程用法**：上下文传递（登录用户、traceId）首选 ThreadLocal
- **版本锚点**：JDK 源码 Thread
