---
title: [NODE-332] Node 服务的 DB 连接池治理？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-332：Node 服务的 DB 连接池治理？
**答**:
- 池参数：max（实例数×max ≤ DB max_connections，NODE-250）、min（预热）、idleTimeout、acquireTimeout（获取超时快速失败）。
- 排队与背压：池耗尽时请求排队——acquire 等待时间指标；P95 等待 > 100ms 说明池小或查询慢。
- 慢查询隔离：慢查询占用连接 → 池饿死；超时杀查询（statement_timeout）+ 慢查询归因（NODE-38x trace db span）。
- 多库策略：读写分离（读走副本+容忍复制延迟）、按域分池（隔离故障域）。

```javascript
// 池监控与调优
pool.on('acquire', () => metrics.inc('pool.acquire'));
setInterval(() => {
  metrics.gauge('pool.total', pool.totalCount);
  metrics.gauge('pool.idle', pool.idleCount);
  metrics.gauge('pool.waiting', pool.waitingCount);   // 排队数：>0 持续 → 告警
}, 5000);
// 查询超时保护
await pool.query('SET statement_timeout = 3000');      // pg：3s 杀慢查询
// 声明：{ max: 20, idleTimeoutMillis: 30000, connectionTimeoutMillis: 2000 }（快速失败优于长等）
```
