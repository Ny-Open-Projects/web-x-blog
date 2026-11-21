---
title: "[RD-011] 扩展类型·Stream（Stream）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 扩展类型 · Stream（Stream）

- **事实**：Redis Stream（5.0）是带消费组的持久化消息流（类 Kafka）
- **原理**：XADD/XREADGROUP/XACK，支持消费组与 pending 列表，弥补 Pub/Sub 不持久不确认的缺陷，小规模消息场景可用
- **常见误区**：
  1. Stream 替代 Kafka 无限制（有内存与持久化代价）（错）
  2. Stream 消息不确认也会删除（在 pending 里保留）（错）
  3. Stream 是 4.0 特性（错）
- **工程用法**：轻量消息队列选型
- **版本锚点**：Redis 5.0
