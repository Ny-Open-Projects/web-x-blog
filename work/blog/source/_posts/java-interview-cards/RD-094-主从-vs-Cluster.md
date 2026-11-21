---
title: "[RD-094] 架构·主从 vs Cluster（选型）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 架构 · 主从 vs Cluster（选型）

- **事实**：架构选型：单机+哨兵（数据量小）/Cluster（分片需求）/多级（本地+Redis）
- **原理**：数据量 <25GB 且无分片需求用主从+哨兵（简单可靠），超限或需要水平扩展才上 Cluster，避免过早分片
- **常见误区**：
  1. Cluster 永远优于主从（错）
  2. 本地缓存与 Redis 二选一（错）
  3. 选型只看内存容量（错）
- **工程用法**：架构选型方法论
- **版本锚点**：实战方法论
