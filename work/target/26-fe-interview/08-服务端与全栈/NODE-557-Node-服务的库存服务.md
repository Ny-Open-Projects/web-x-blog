---
title: [NODE-557] Node 服务的库存服务（预扣/回补/分层）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-557：库存服务
**答**:
- 库存层次：销售库存（可售）→ 预扣（下单占用，限时释放）→ 真实扣减（支付后落定）；共享库存 vs 独立活动库存（秒杀独立池——隔离热点 NODE-438）。
- 预扣与回补：预扣原子（Redis Lua 扣可售加预扣——秒杀性能路径）、超时释放（预扣单超时 → 回补任务——延迟任务 NODE-379）、回补幂等（预扣单状态机：paid 才真扣，closed 回补——重复回补防）。
- 热点优化：分片库存（热点商品拆 N 份配额轮询——ARC-438）、扣减合并（攒批一次落 DB——最终真库存 DB 为准异步同步）。
- 一致性：Redis 与 DB 的最终一致（对账：DB 库存 = Redis 剩余 + 在途预扣——差异告警 NODE-382）、超卖防线（DB 层条件更新兜底——Redis 层挡流量 DB 层保正确）。
- 观测：预扣成功率/回补量/超卖告警（应为 0）、库存周转指标。
```javascript
// 预扣（Redis 原子）+ 超时回补
const ok = await redis.eval(`if redis.call('get',K1)+0 >= ARGV1 then
  redis.call('decr',K1); redis.call('incr',K2); return 1 end`, sell, hold, qty);
scheduleRelease(preOrderId, { delay: 15 * 60e3 });               // 15min 未支付回补
// 落定：支付成功 → db.tx(真扣 + 销预扣) —— DB 条件更新保底防超卖
```
