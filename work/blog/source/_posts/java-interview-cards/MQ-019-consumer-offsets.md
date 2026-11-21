---
title: "[MQ-019] 消费·__consumer_offsets（位移）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 消费 · __consumer_offsets（位移）

- **事实**：消费位移存内部主题 __consumer_offsets（50 分区）
- **原理**：消费组提交 offset（自动/手动），rebalance 后按提交位移继续，位移重复提交幂等，位移丢失导致重复消费
- **常见误区**：
  1. 位移存在 ZooKeeper（旧版本是，KRaft 后完全废弃）（错）
  2. 自动提交保证不丢（错）
  3. 位移提交是事务性的（与消息处理非原子）（错）
- **工程用法**：消费语义基础
- **版本锚点**：官方文档
