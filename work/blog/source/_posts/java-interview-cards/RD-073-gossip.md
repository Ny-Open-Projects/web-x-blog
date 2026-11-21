---
title: "[RD-073] Cluster·gossip（通信）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Cluster · gossip（通信）

- **事实**：Cluster 节点间 gossip 协议交换状态（PING/PONG/MEET）
- **原理**：去中心化元数据传播（100ms 级收敛），节点数增加心跳开销增长，这就是 16384 槽位图的由来背景
- **常见误区**：
  1. Cluster 有中心节点管理元数据（错）
  2. gossip 实时一致（错）
  3. 通信协议是主从复制协议（错）
- **工程用法**：集群原理深入
- **版本锚点**：官方文档
