---
title: [NODE-707] Redis 集群模式（哨兵/Cluster）怎么选？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-707：Redis 集群怎么选？
**答**：
- 哨兵模式：主从 + 哨兵自动故障转移——单主写（写容量受限）、全量数据单内存（容量受限）、命令全兼容（Lua/multi-key 事务可用）。
- Cluster 模式：16384 slot 分片（写与容量水平扩展）；multi-key 操作限制（同 slot 才能事务——hash tag `{user1000}` 强制同 slot）；Lua 限制（keys 必须同 slot）。
- 选型：容量/写 QPS 未达单机瓶颈 → 哨兵（简单）；超了 → Cluster（hash tag 规划——SCN-NODE-656 库存 key 的 slot 设计）。
- 客户端适配：Cluster 模式的客户端重定向（MOVED/ASK——SDK 自动处理）+ hash tag 约定进代码规范。
- 追问钩子：为什么 Cluster 模式的「multi-key 操作」是架构级约束——multi-key 事务/Lua 要求 keys 同 slot，业务代码里的 multi-key 操作（用户信息+订单缓存原子更新）在 Cluster 下必须 hash tag 规划（设计期决定）或改语义（拆成两次非原子 + 补偿）——slot 规划是 Cluster 迁移里最需要业务参与的设计决策。

```javascript
// Cluster hash tag：同用户同 slot
await redis.mset(`{u1000}:profile`, p, `{u1000}:orders`, o);   // tag 保证同 slot
// 哨兵客户端（自动 failover 感知）
const redis = new Redis({ sentinels: [...], name: 'mymaster' });
```
