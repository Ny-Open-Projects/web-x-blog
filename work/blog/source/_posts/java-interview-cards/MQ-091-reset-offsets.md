---
title: "[MQ-091] 运维·reset-offsets（位移）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 运维 · reset-offsets（位移）

- **事实**：kafka-consumer-groups --reset-offsets 支持按时间/位移/最早最晚重置消费组位移
- **原理**：重置前消费组需停（活跃组拒绝重置），按 --to-datetime 修复数据（补数）标准动作，重放消费必须幂等（MQ-022 联动）
- **常见误区**：
  1. 位移重置可在线执行（错）
  2. 重置影响所有消费组（只影响指定组）（错）
  3. 重置后消息不会重复（错）
- **工程用法**：补数/修复标准流程
- **版本锚点**：官方文档
