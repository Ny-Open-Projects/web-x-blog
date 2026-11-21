---
title: "[MQ-032] 消费·push vs pull（模式）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 消费 · push vs pull（模式）

- **事实**：Kafka/RocketMQ 是 pull（客户端拉取长轮询），RabbitMQ 是 push（服务端推送）
- **原理**：pull 语义消费者自主控速（防压垮），push 容易压垮慢消费者（prefetch 限流补救），长轮询（long polling）兼顾延迟与效率
- **常见误区**：
  1. pull 实时性差于 push（长轮询弥补）（错）
  2. 长轮询是频繁短连接（错）
  3. push 一定更快（错）
- **工程用法**：消费模式原理
- **版本锚点**：实战共识
