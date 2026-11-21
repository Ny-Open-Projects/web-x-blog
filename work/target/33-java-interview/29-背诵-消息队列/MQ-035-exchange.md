---
title: "[MQ-035] 架构·exchange（交换机）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 架构 · exchange（交换机）

- **事实**：RabbitMQ 架构：producer→exchange（交换机路由）→queue→consumer
- **原理**：消息先到交换机按 binding 规则路由到队列，无匹配队列则丢弃（mandatory 标记退回），与 Kafka/RocketMQ 的 topic 直投不同
- **常见误区**：
  1. RabbitMQ 消息直接进队列（错）
  2. exchange 有存储能力（错）
  3. 无匹配路由消息自动排队（错）
- **工程用法**：架构模型差异
- **版本锚点**：官方文档
