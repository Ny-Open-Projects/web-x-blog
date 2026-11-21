---
title: [NODE-124] Redis 集群（Cluster）与哨兵（Sentinel）如何概览与选型？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-124：Redis 集群（Cluster）与哨兵（Sentinel）如何概览与选型？
**答**：
- 哨兵解决**高可用**：主从复制 + 故障自动转移，容量仍是单机；客户端先问哨兵要主节点地址再读写。
- Cluster 解决**容量/写吞吐**：16384 slot 分片到多主，键路由按 CRC16；多键操作要求同 slot，用 hash tag `user:{1001}:xxx` 控制。
- 客户端要点：哨兵模式配 `sentinels` 列表与 `name`；Cluster 模式管好 `maxRedirections`（MOVED/ASK 重定向）与离线队列行为。
- 选型：数据量与写 QPS 单机扛得住 → 哨兵（简单稳）；超过单机内存或写瓶颈 → Cluster（运维与多键成本上升）。

```javascript
const Redis = require('ioredis');

// 哨兵：高可用，自动发现主节点
const sentinel = new Redis({
  sentinels: [
    { host: 'redis-s1', port: 26379 },
    { host: 'redis-s2', port: 26379 },
  ],
  name: 'mymaster',     // 哨兵配置里的 master 名
  maxRetriesPerRequest: 2,
});

// Cluster：分片容量扩展
const cluster = new Redis.Cluster(
  [{ host: 'redis-c1', port: 7000 }, { host: 'redis-c2', port: 7000 }],
  {
    maxRedirections: 3,        // MOVED/ASK 重定向上限
    enableOfflineQueue: false, // 集群故障快速失败而非无限排队
  });

// Cluster 多键操作：hash tag 强制同 slot
await cluster.mset('user:{1001}:profile', 'a', 'user:{1001}:orders', 'b');
// 读从库：role: 'slave' + preferredSlaves 做读写分离（容忍复制延迟）
```
