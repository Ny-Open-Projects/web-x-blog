---
title: "[JC-043] 阻塞队列·DelayQueue（实现）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 阻塞队列 · DelayQueue（实现）

- **事实**：DelayQueue 按到期时间出队元素必须实现 Delayed 接口
- **原理**：内部优先堆按剩余延迟排序，take 阻塞到队首到期，用于订单超时关单等延迟任务（小规模方案，大规模用时间轮或 RocketMQ 延迟消息）
- **常见误区**：
  1. DelayQueue 按 FIFO 出队（错）
  2. 元素自动在到期时被删除（错）
  3. 不需要实现任何接口（错）
- **工程用法**：订单超时关闭的小规模实现
- **版本锚点**：JDK 文档
