---
title: "[JC-041] 阻塞队列·ArrayBlockingQueue（实现）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 阻塞队列 · ArrayBlockingQueue（实现）

- **事实**：ArrayBlockingQueue 是单锁有界数组队列
- **原理**：读写共用一把锁，容量构造时固定，支持公平模式，与 Linked 双锁版本并发度不同
- **常见误区**：
  1. ArrayBlockingQueue 读写两把锁（错）
  2. 容量可以动态增长（错）
  3. 它比 LinkedBlockingQueue 并发更高（错）
- **工程用法**：有界队列首选之一，容量固定场景
- **版本锚点**：JDK 源码
