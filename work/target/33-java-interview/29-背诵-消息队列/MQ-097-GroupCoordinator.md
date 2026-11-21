---
title: "[MQ-097] 架构·GroupCoordinator（协调）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 架构 · GroupCoordinator（协调）

- **事实**：每个消费组由一个 broker 担任 GroupCoordinator 管理成员与位移提交
- **原理**：coordinator 按组名哈希分配到 broker，心跳/加入组/位移提交都经它，coordinator 宕机组重新加入（短暂暂停），大规模消费组时 coordinator 是均衡关注点
- **常见误区**：
  1. coordinator 是独立服务（错）
  2. 每个消费者有自己的 coordinator（错）
  3. 位移存 ZooKeeper（老版本是）（错）
- **工程用法**：消费组内部机制
- **版本锚点**：官方文档
