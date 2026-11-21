---
title: "[MQ-002] 基础·Kafka（选型）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 基础 · Kafka（选型）

- **事实**：主流选型：Kafka（日志流/大数据吞吐）、RocketMQ（业务消息/事务/延迟）、RabbitMQ（企业路由复杂场景）
- **原理**：吞吐排序 Kafka≈RocketMQ>RabbitMQ，功能差异：事务消息与延迟消息 RocketMQ 原生，路由灵活度 RabbitMQ 最强
- **常见误区**：
  1. Kafka 适合所有场景（错）
  2. RabbitMQ 吞吐最高（错）
  3. 选型只看性能（错）
- **工程用法**：消息中间件选型框架
- **版本锚点**：实战共识
