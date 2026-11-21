---
title: "[MQ-011] 幂等·enable.idempotence（生产者）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 幂等 · enable.idempotence（生产者）

- **事实**：生产者幂等：enable.idempotence=true 用 PID+序列号防 broker 端重复
- **原理**：broker 按生产者 ID+分区+序号去重（只防单会话重试），跨会话/跨实例仍需业务幂等，3.0 起默认开启
- **常见误区**：
  1. 幂等生产者防止所有重复（只防重试窗口）（错）
  2. 幂等开启后无需业务幂等（错）
  3. 默认关闭（错）
- **工程用法**：不丢不重的生产端配置
- **版本锚点**：Kafka 3.0
