---
title: "[MQ-017] 架构·KRaft（KRaft）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 架构 · KRaft（KRaft）

- **事实**：KRaft 模式用内置 Raft 取代 ZooKeeper（3.x 引入，4.0 彻底移除 ZK 支持）
- **原理**：元数据进内部主题（__cluster_metadata）由 controller quorum 管理，简化部署与扩容，官方文档核对（本项目已核对版本线）
- **常见误区**：
  1. KRaft 仍需要 ZooKeeper（错）
  2. KRaft 是 1.0 特性（错）
  3. 移除 ZK 影响 ISR 机制（错）
- **工程用法**：架构演进版本线
- **版本锚点**：Kafka 3.x/4.0 核对
