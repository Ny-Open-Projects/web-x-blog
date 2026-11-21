---
title: "[MQ-008] 生产·min.insync.replicas（min.insync）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 生产 · min.insync.replicas（min.insync）

- **事实**：min.insync.replicas=2 要求 ISR 至少 2 个否则写入报错
- **原理**：与 acks=all 配合：ISR 缩到 1 时拒绝写（宁可不可用不丢数据），是"不丢消息"的 broker 端保证
- **常见误区**：
  1. 该参数默认 2（错）
  2. 它与 acks 无关（错）
  3. ISR 不足时自动降级写入（错）
- **工程用法**：不丢消息配置链第二环
- **版本锚点**：官方文档
