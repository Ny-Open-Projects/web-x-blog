---
title: "[MQ-076] 运维·leader 偏斜（均衡）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 运维 · leader 偏斜（均衡）

- **事实**：Kafka leader 偏斜：分区 leader 集中在少数 broker（流量不均）
- **原理**：auto.leader.rebalance.enable 默认开，手动 Preferred leader election 修正，broker 负载监控（入流量分布），扩容后偏斜常见
- **常见误区**：
  1. leader 自动完美均衡（错）
  2. 偏斜不影响性能（错）
  3. 扩容自动均衡（错）
- **工程用法**：集群运维细节
- **版本锚点**：实战共识
