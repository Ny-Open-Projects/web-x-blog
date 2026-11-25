---
title: [NODE-386] Node 服务的分库分表与路由（拆分键选择）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-386：分库分表与路由
**答**:
- 先穷尽单库手段：索引优化/读写分离/归档冷数据/换存储——分库分表是最后的重武器（运维复杂度陡增）。
- 拆分键选择：按最高频查询维度（订单按 userId 查 → userId 分片；若同时要按商家查 → 冗余双写或异构索引表/ES）。原则：单分片内完成主要查询（避免跨片 JOIN/聚合）。
- 路由实现：应用层路由（sharding key 哈希 → 连接对应库，Node 侧中间件封装）vs 中间件代理（MyCat/ShardingSphere-Proxy）vs 分布式数据库（TiDB/Vitess，免手工分片，新项目优先评估）。
- 带来的问题清单：跨片分页/聚合（聚合到路由层汇总，深分页禁止——cursor + 分片内限制）、全局唯一 ID（雪花/号段）、扩容（一致性哈希/预分片 1024 槽，迁移工具双写切换）、跨片事务（ARC-380 saga）。
- 冷热分层：历史数据归档库（查询走归档入口，业务无感降级——旧订单查询慢一点可接受）。
```javascript
// 应用层分片路由
function routeOrder(userId) {
  const slot = hash(userId) % 1024;                             // 逻辑槽
  const shard = SLOT_MAP[slot];                                 // 槽 → 物理库（扩容只改映射）
  return pools[shard];
}
// 用户维度查询：routeOrder(uid).query('select * from orders where user_id=$1', [uid])
// 商家维度：走异构索引（ES/宽表，异步同步）
```
