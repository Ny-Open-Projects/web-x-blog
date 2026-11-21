---
title: "[MQ-092] 高可用·unclean election（选主）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 高可用 · unclean election（选主）

- **事实**：unclean.leader.election.enable=false（默认）禁止非 ISR 副本当 leader 宁可分区不可用
- **原理**：非干净选主会丢 ISR 未同步的消息（可用性换一致性），关闭是"不丢消息"链（MQ-021）的 broker 端一环，开启是日志类可容忍场景的权衡
- **常见误区**：
  1. 该参数默认开启非干净选主（错）
  2. 开启后不丢数据（错）
  3. 与 ISR 无关（错）
- **工程用法**：一致性与可用性权衡题
- **版本锚点**：官方文档
