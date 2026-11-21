---
title: "[MQ-071] 高可用·Dledger（Dledger）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 高可用 · Dledger（Dledger）

- **事实**：RocketMQ 高可用演进：主从（2M-2S）→Dledger（Raft 自动切换，4.5+）
- **原理**：Dledger 基于 Raft 自动选主（免人工切主），与 Kafka ISR 机制对比：Raft 多数派写 vs ISR+acks，5.x  continua 迭代
- **常见误区**：
  1. Dledger 是主从复制（错）
  2. Dledger 不支持自动切换（错）
  3. 4.5 之前就能自动切主（错）
- **工程用法**：高可用架构演进
- **版本锚点**：RocketMQ 4.5
