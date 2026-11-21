---
title: "[JC-066] 并发容器·ConcurrentLinkedQueue（无锁）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 并发容器 · ConcurrentLinkedQueue（无锁）

- **事实**：ConcurrentLinkedQueue 是 CAS 无锁非阻塞队列
- **原理**：基于 Michael-Scott 无锁算法，size() 是 O(n) 弱一致遍历，适合无界并发生产消费但不是 BlockingQueue
- **常见误区**：
  1. 它实现 BlockingQueue 接口（错）
  2. size() 是 O(1) 精确值（错）
  3. 入队出队需要加锁（错）
- **工程用法**：高吞吐异步任务传递
- **版本锚点**：JDK 源码
