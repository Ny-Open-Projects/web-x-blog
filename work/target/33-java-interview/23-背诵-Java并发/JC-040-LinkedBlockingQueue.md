---
title: "[JC-040] 阻塞队列·LinkedBlockingQueue（实现）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 阻塞队列 · LinkedBlockingQueue（实现）

- **事实**：LinkedBlockingQueue 不传容量参数时容量为 Integer.MAX_VALUE
- **原理**：两把锁分离读写提高并发但默认容量形同无界，用在 newFixedThreadPool 就是 OOM 根源
- **常见误区**：
  1. LinkedBlockingQueue 默认容量是 10（错）
  2. 它默认有界（错）
  3. 无界时队列满会拒绝任务（错）
- **工程用法**：当业务队列必须显式传容量
- **版本锚点**：JDK 源码
