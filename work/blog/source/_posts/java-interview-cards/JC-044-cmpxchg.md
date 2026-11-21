---
title: "[JC-044] CAS·cmpxchg（原子性）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## CAS · cmpxchg（原子性）

- **事实**：CAS 依赖 CPU 的原子比较交换指令（x86 上 cmpxchg 配 lock 前缀）
- **原理**：Java 通过 Unsafe 调用硬件原子指令，失败则自旋重试，全程无锁，JDK9 后推荐 VarHandle
- **常见误区**：
  1. CAS 是 JVM 软件实现的锁机制（错）
  2. CAS 需要操作系统内核参与（错）
  3. cmpxchg 单独使用不带 lock 前缀也是原子的（错）
- **工程用法**：谈无锁编程先落到硬件原子指令
- **版本锚点**：x86 手册
