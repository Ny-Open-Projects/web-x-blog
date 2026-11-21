---
title: "[JC-006] synchronized·monitor（锁机制）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## synchronized · monitor（锁机制）

- **事实**：synchronized 基于对象头的 monitor 机制实现互斥与可见性
- **原理**：字节码层面是 monitorenter 与 monitorexit 指令，进入时 invalidate 缓存、退出时 flush 写，语义与 volatile 写读对应
- **常见误区**：
  1. synchronized 只保证互斥不保证可见性（错）
  2. synchronized 是 JVM 层完全独立于对象头的机制（错）
  3. monitorenter 是 Java 方法字节码（错）
- **工程用法**：互斥与可见性需求同时存在时首选 synchronized
- **版本锚点**：JLS 17.x
