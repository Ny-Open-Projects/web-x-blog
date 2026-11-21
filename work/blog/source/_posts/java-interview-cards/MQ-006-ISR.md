---
title: "[MQ-006] 复制·ISR（ISR）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 复制 · ISR（ISR）

- **事实**：ISR（in-sync replicas）是与 leader 保持同步的副本集合
- **原理**：acks=all 时消息需 ISR 全部确认才算写入，落后超过 replica.lag.time.max.ms 的副本被移出 ISR，HW 由 ISR 决定
- **常见误区**：
  1. ISR 固定不变（错）
  2. acks=all 需要 ACK 全部副本（仅 ISR）（错）
  3. ISR 越大吞吐越高（错）
- **工程用法**：副本机制核心概念
- **版本锚点**：官方文档
