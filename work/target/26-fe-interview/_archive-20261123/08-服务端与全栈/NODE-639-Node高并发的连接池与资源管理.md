---
title: [NODE-639] 高并发的连接池与资源管理怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-639：连接池怎么管理？
**答**：
- 池的核心参数：max（上限——按下游容量而非本地 CPU）、min（预热保底）、idleTimeout（空闲回收）、acquireTimeout（获取超时——池耗尽快速失败优于排队雪崩）。
- 池耗尽策略：排队等待（有限队列 + 超时）vs 快速失败（立即 503 + 重试头）——高并发下快速失败 + 上游退避比无限排队稳定；监控池水位（使用率/等待队列——SCN-SLA-711 数据新鲜度同源）。
- 泄漏防御：借出必须归还（finally + 超时强制回收——「借出未还」检测与告警）；事务连接的归还点显式化。
- 多池协调：读写分离池/不同下游独立池——每池独立参数独立监控；下游容量 = 池 max × 实例数的全局校验（别把下游打挂）。
- 追问钩子：为什么「acquireTimeout 快速失败」优于「无限等待」——池耗尽通常是下游变慢（DB 慢查询），无限等待让请求堆积（内存涨 + 线程池饿死），雪崩放大；快速失败让上游立即感知并触发熔断/降级——把过载转化为快速拒绝，是限流的池化版本。

```javascript
const pool = createPool({
  max: 20, idleTimeout: 30_000, acquireTimeout: 2_000, // 2s 拿不到快速失败
});
async function withConn(fn) {
  const conn = await pool.acquire();                   // 超时即抛
  try { return await fn(conn); }
  finally { pool.release(conn); }                      // finally 归还（泄漏防御）
}
telemetry.push({ poolUsing: pool.using, poolWaiting: pool.waiting });   // 水位
```
