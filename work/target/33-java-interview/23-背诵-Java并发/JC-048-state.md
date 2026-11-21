---
title: "[JC-048] AQS·state（实现）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## AQS · state（实现）

- **事实**：AQS 核心是一个 volatile int state 加 CLH 变体等待队列
- **原理**：获取失败的线程封装成 Node 入队 park，释放时唤醒队首后继；state 语义由子类定义（重入次数、许可数、闩计数）
- **常见误区**：
  1. AQS 内部用 HashMap 管理等待线程（错）
  2. AQS 的队列是无锁链表（错）
  3. state 是普通 int 不需要 volatile（错）
- **工程用法**：实现自定义同步器直接复用 AQS
- **版本锚点**：JDK 源码
