---
title: "[MQ-094] 运维·quota（限速）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 运维 · quota（限速）

- **事实**：Kafka client quota 按 clientId/user 限速（生产/消费带宽与请求时间占比）
- **原理**：防单业务打满 broker 网卡（多租户隔离），配额动态生效（kafka-configs 命令），超限被节流而非拒绝，与网关限流分层
- **常见误区**：
  1. quota 会拒绝超限请求（是节流延迟）（错）
  2. quota 只能按 IP（错）
  3. 配额默认无限制无需配置（错）
- **工程用法**：多租户 MQ 治理
- **版本锚点**：官方文档
