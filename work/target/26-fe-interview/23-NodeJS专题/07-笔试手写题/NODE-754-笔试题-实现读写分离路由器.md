---
title: [NODE-754] 笔试题——实现读写分离路由器（延迟感知 + 读己之写）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-754：手写读写分离

**需求与边界**：
- 需求：读写分离（SCN-NODE-706）——① 副本延迟感知摘流（per-replica——SCN-NODE-706 隔离到副本粒度）；② 读己之写 bypass（写后 30s 读主——SCN-NODE-654）；③ 强一致显式（query 标注 strong 走主）；④ 副本轮询负载均衡（健康副本间）。
- 边界：① 写记录（Redis rw:user——写时 set 30s——SCN-NODE-654 实现细节）；② 摘流恢复（延迟回落自动回流——SCN-NODE-726 熔断恢复语义）；③ 事务内强制主库（事务语义）。

**答**：
```javascript
class ReadWriteRouter {
  constructor(primary, replicas) {
    this.primary = primary; this.replicas = replicas;
    replicas.forEach(r => monitorLag(r, { maxLag: 2, onExceed: () => r.healthy = false,
      onRecover: () => r.healthy = true }));           // 延迟感知摘流（副本粒度）
  }
  async write(q) {
    await this.primary.query(q);
    if (ctx.getStore()?.user)                          // 写后 30s 读己之写
      await redis.set(`rw:${ctx.getStore().user}`, 1, 'EX', 30);
  }
  async read(q, { consistency = 'eventual', inTx = false } = {}) {
    if (consistency === 'strong' || inTx || await redis.get(`rw:${ctx.getStore()?.user}`))
      return this.primary.query(q);                    // 强一致/事务/读己之写 → 主库
    const healthy = this.replicas.filter(r => r.healthy);
    const r = healthy[this.roundRobin() % healthy.length] ?? this.primary;   // 全挂回主（保底）
    return r.query(q);
  }
}
```

**评分点**:
- 副本粒度延迟摘流（非全局切主——SCN-NODE-706 隔离）。
- 读己之写 bypass 三通道（Redis 标记/strong 标注/事务）。
- 全副本挂回主（保底——可用性优先）。
- 写后标记（Redis 30s——SCN-NODE-654 实现细节）。
