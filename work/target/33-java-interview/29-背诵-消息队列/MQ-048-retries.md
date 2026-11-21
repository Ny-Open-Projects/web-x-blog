---
title: "[MQ-048] 生产·retries（重试）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 生产 · retries（重试）

- **事实**：生产者重试：retries 大值+enable.idempotence=true 组合防重试乱序
- **原理**：幂等开启后重试在单分区有序（序列号），未开启幂等时 max.in.flight>1 重试可能乱序，超时与重试策略按业务延迟容忍
- **常见误区**：
  1. 重试不影响顺序（幂等未开时影响）（错）
  2. 重试次数越多越好（错）
  3. 重试由 MQ 自动处理无需配置（错）
- **工程用法**：生产端可靠性
- **版本锚点**：官方文档
