---
title: "[JC-042] 阻塞队列·SynchronousQueue（实现）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 阻塞队列 · SynchronousQueue（实现）

- **事实**：SynchronousQueue 没有容量每个 put 必须等 take 直接交接
- **原理**：不存储元素，newCachedThreadPool 用它实现来一个任务建一个线程的设计
- **常见误区**：
  1. SynchronousQueue 容量是 1（错）
  2. put 会先暂存在队列中（错）
  3. 适合任务缓冲场景（错）
- **工程用法**：线程池需要快速扩张时选用
- **版本锚点**：JDK 文档
