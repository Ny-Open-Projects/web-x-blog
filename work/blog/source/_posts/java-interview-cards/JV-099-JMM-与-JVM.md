---
title: "[JV-099] 并发·JMM 与 JVM（内存）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 并发 · JMM 与 JVM（内存）

- **事实**：JMM 是内存可见性规范 JVM 实现负责落地（内存屏障/缓存一致性）
- **原理**：JMM 定义 happens-before 等抽象语义，HotSpot 用 CPU 指令（lock 前缀、mfence）与缓存一致性协议实现，两者层次不同不可混谈
- **常见误区**：
  1. JMM 就是 JVM 内存结构（错）
  2. 内存屏障是 JMM 定义的指令（错）
  3. JMM 与硬件无关（错）
- **工程用法**：区分规范与实现的答题层次
- **版本锚点**：JSR-133
