---
title: [NODE-656] 高并发下单（库存扣减）怎么设计？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-656：库存扣减怎么做？
**答**：
- 扣减方案：DB 原子扣减（UPDATE stock SET n=n-1 WHERE id=? AND n>0——条件更新防超卖，行锁串行化是瓶颈）、Redis 预扣（Lua 原子 DECR——扛流量，DB 异步落库）、分段库存（拆 N 段并行扣——行锁分片提高吞吐）。
- 漏斗设计：前端限流（SCN-857 按钮）→ 排队削峰（SCN-855）→ Redis 预扣 → MQ 异步落库——每层削一部分流量，DB 只见稳态。
- 回补与一致性：Redis 预扣成功但 DB 落库失败 → 回补 Redis（补偿）；对账（Redis vs DB 定期校准——SCN-867）；超卖的最后防线是 DB 条件更新。
- 追问钩子：为什么「Redis 预扣 + MQ 异步落库」不等于「放弃 DB 一致性」——Redis 预扣只是「准入控制」（挡住超卖流量），真正的账本仍是 DB（条件更新是超卖的最后防线）；MQ 异步落库丢失时对账兜底修正 Redis——每层各司其职：Redis 管吞吐、MQ 管削峰、DB 管正确性。

```javascript
// Redis Lua 预扣（原子）
const script = `local s = tonumber(redis.call('get', KEYS[1]))
  if s <= 0 then return -1 end
  redis.call('decr', KEYS[1]) return s - 1`;
// DB 条件更新（最后防线）
const r = await db.query(
  'UPDATE stock SET n = n - 1 WHERE sku_id = $1 AND n > 0 RETURNING n', [sku]);
if (r.rowCount === 0) { await redis.incr(skuKey); throw new SoldOut(); }   // 失败回补
```
