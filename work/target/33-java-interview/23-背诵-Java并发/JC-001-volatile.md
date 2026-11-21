---
title: "[JC-001] volatile·volatile（内存语义）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## volatile · volatile（内存语义）

- **事实**：volatile 保证可见性与有序性，但不保证原子性
- **原理**：JMM 对 volatile 写强制刷新到主存、读强制从主存加载，并通过内存屏障禁止特定重排；但 i++ 这类复合操作仍是读-改-写三步
- **常见误区**：
  1. volatile 能保证 i++ 的原子性（错）
  2. volatile 完全替代 synchronized（错）
  3. volatile 变量读写有锁开销与 synchronized 相当（错）
- **工程用法**：状态标志位、一写多读的配置开关
- **版本锚点**：JLS 17.4
