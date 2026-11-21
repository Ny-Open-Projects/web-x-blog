---
title: "[JC-008] synchronized·Class 对象（锁机制）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## synchronized · Class 对象（锁机制）

- **事实**：static synchronized 方法锁的是 Class 对象与实例锁互不冲突
- **原理**：类的所有实例共享同一把 Class 锁，静态与实例同步方法可并发执行
- **常见误区**：
  1. static synchronized 与实例方法锁同一把锁（错）
  2. Class 锁可以保护实例字段（错）
  3. 静态锁比实例锁性能更差（错）
- **工程用法**：保护静态状态用 Class 锁或专用锁对象
- **版本锚点**：JLS 8.4.3.6
