---
title: "[MQ-007] 生产·acks（确认）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 生产 · acks（确认）

- **事实**：生产者 acks 三档：0（不等）、1（leader 确认）、all（ISR 全确认）
- **原理**：acks=1 leader 挂且未复制则丢，acks=all+min.insync.replicas=2 才是生产标准（broker 端配合）
- **常见误区**：
  1. acks 默认是 all（默认 1）（错）
  2. acks=all 单副本时退化为 1（错）
  3. acks=0 最安全（错）
- **工程用法**：不丢消息配置链第一环
- **版本锚点**：官方文档
