---
title: [NODE-763] 笔试题——实现分库分表路由器（基因法 + 一致性 hash）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-763：手写分片路由

**需求与边界**：
- 需求：分片路由（SCN-NODE-705）——① 基因法 ID（order_id 嵌 user_gene——双维度路由）；② 一致性 hash 分片（虚拟节点——扩容平滑）；③ 跨片查询检测（无分片键查询 → 拒绝或走异构索引——SCN-NODE-705 约束）；④ 扩容迁移双写（SCN-OPS-331）。
- 边界：① 一致性 hash 虚拟节点数（150/物理节点——均匀性）；② 跨片聚合的代价声明（聚合查询走数仓——SCN-NODE-714）；③ 路由不可用 fail-closed（路由服务挂拒绝写——防错片写）。

**答**：
```javascript
class ShardRouter {
  constructor({ nodes = 64, vnodes = 150 } = {}) {
    this.ring = buildConsistentHashRing(nodes, vnodes);   // 虚拟节点环
  }
  route(gene) { return this.ring.lookup(gene); }        // 基因 → 分片
  async insert(order) {
    const gene = order.userId.slice(-8);                // user 基因（SCN-NODE-705）
    const shard = this.route(gene);
    if (!shard) throw new Error('ROUTE_UNAVAILABLE');   // fail-closed（防错片写）
    return shard.db.insert(order);
  }
  async queryByUser(userId) {                           // 同基因同片（双维度）
    const shard = this.route(userId.slice(-8));
    return shard.db.queryByUser(userId);
  }
  async queryBySomethingElse(q) {                       // 无分片键
    throw new NoShardKey();                             // 拒绝（走 ES 异构索引）
  }
}
```

**评分点**:
- 基因法双维度路由（order/user 同片——SCN-NODE-705）。
- 一致性 hash 虚拟节点（扩容平滑）。
- 跨片查询 fail-closed（拒绝 → 异构索引——约束显式）。
- 路由不可用 fail-closed（防错片写——数据正确性优先）。
