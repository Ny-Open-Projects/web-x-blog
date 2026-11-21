---
title: "[MY-054] 高可用·MGR（集群）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 高可用 · MGR（集群）

- **事实**：MGR（组复制）基于 Paxos 多数派写提供强一致高可用
- **原理**：8.0 引入 MySQL InnoDB Cluster（MGR+Router+Shell），多数派确认防脑裂，代价是写性能与运维复杂度，国内主用主从+MHA/Orchestrator
- **常见误区**：
  1. MGR 是 MySQL 默认架构（错）
  2. MGR 无多数派要求（错）
  3. MGR 与主从性能相同（错）
- **工程用法**：高可用方案对比题
- **版本锚点**：MySQL 8.0
