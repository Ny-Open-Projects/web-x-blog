---
title: "[MQ-038] 集群·quorum queue（quorum）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 集群 · quorum queue（quorum）

- **事实**：RabbitMQ 集群：经典镜像队列（已过时推荐）→quorum queue（Raft，3.8+）
- **原理**：quorum 队列基于 Raft 多数派写，比镜像队列强一致且无脑裂，官方推荐替代，延迟略高
- **常见误区**：
  1. 镜像队列是当前推荐（错）
  2. quorum 队列无多数派要求（错）
  3. 集群自动处理脑裂（错）
- **工程用法**：RabbitMQ 高可用演进
- **版本锚点**：官方文档
