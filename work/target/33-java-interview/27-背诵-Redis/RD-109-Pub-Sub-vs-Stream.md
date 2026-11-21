---
title: "[RD-109] 消息·Pub/Sub vs Stream（选型）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 消息 · Pub/Sub vs Stream（选型）

- **事实**：Pub/Sub（不持久/无确认/在线才能收）vs Stream（持久/消费组/ACK/pending 重试）
- **原理**：Pub/Sub 适合"在线广播"（配置失效通知），Stream 适合"可靠消息"（任务投递），选错是丢消息事故源，与 MQ 能力对齐理解（RD-053/011 联动）
- **常见误区**：
  1. Pub/Sub 会补发离线消息（错）
  2. 两者持久化相同（错）
  3. Stream 消息自动确认（错）
- **工程用法**：消息能力选型线
- **版本锚点**：官方文档
