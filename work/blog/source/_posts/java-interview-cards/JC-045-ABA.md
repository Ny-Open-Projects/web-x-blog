---
title: "[JC-045] CAS·ABA（误用）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## CAS · ABA（误用）

- **事实**：CAS 存在 ABA 问题：值从 A 改回 A 时 CAS 无法察觉
- **原理**：解决方式是加版本号，AtomicStampedReference 维护引用加 stamp 二元组，数据库乐观锁 version 字段同理
- **常见误区**：
  1. AtomicLong 能解决 ABA（错）
  2. ABA 在 Java 中不可能发生（错）
  3. AtomicReference 天然防 ABA（错）
- **工程用法**：链表类无锁结构必须防 ABA
- **版本锚点**：学术与实战共识
