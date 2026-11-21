---
title: "[MQ-005] 消费·rebalance（再平衡）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 消费 · rebalance（再平衡）

- **事实**：rebalance（再平衡）触发：组内成员增减、订阅变化、消费者超时（max.poll.interval.ms 超时）
- **原理**：rebalance 期间整组停止消费（STW 式），长业务处理超时被踢出引发循环 rebalance，是经典生产事故
- **常见误区**：
  1. rebalance 不影响消费（错）
  2. rebalance 是增量的（错）
  3. max.poll.interval 默认足够大（默认 5 分钟但仍会撞）（错）
- **工程用法**：消费稳定性核心机制
- **版本锚点**：官方文档
