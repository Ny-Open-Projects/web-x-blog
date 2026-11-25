---
title: [NODE-738] 笔试题——实现库存扣减链路（Redis 预扣 + DB 条件更新 + 回补）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-738：手写库存扣减

**需求与边界**：
- 需求：库存扣减完整链路（SCN-NODE-656）——① Redis Lua 预扣（准入）；② MQ 异步落库（削峰）；③ DB 条件更新（超卖最后防线）；④ 失败回补 Redis（补偿）；⑤ 对账校准（SCN-NODE-682）。
- 边界：① 预扣幂等（同订单重复预扣——订单号幂等键）；② MQ 消费失败回补（预扣成功落库失败——补偿闭环）；③ 分段库存可选（热点 sku 拆段——SCN-NODE-656）。

**答**：
```javascript
// 1. Redis Lua 预扣（准入 + 幂等）
const DEDUCT = `
  if redis.call('hexists', KEYS[1], ARGV[1]) == 1 then return -2 end   -- 幂等：同订单
  local s = tonumber(redis.call('get', KEYS[1]))
  if s <= 0 then return -1 end                          -- 售罄
  redis.call('hset', KEYS[1], ARGV[1], 1)               -- 记订单防重
  redis.call('decr', KEYS[1]) return s - 1`;
const r = await redis.eval(DEDUCT, 1, `stock:${sku}`, orderId);
if (r === -1) throw new SoldOut();
await mq.publish('stock-deduct', { sku, orderId });    // 2. 异步落库（削峰）
// 3. MQ 消费：DB 条件更新（最后防线）
consumer.on('stock-deduct', async ({ sku, orderId }) => {
  const row = await db.query(
    'UPDATE stock SET n = n - 1 WHERE sku_id = $1 AND n > 0 RETURNING id', [sku]);
  if (row.rowCount === 0) {                             // DB 无库存：回补 Redis（补偿闭环）
    await redis.incr(`stock:${sku}`);
    await redis.hdel(`stock:${sku}`, orderId);
    await notifySoldOut(orderId);                       // 用户侧补偿
  }
});
// 4. 对账校准（SCN-NODE-682）
cron('0 * * * *', async () => {                        // Redis 与 DB diff
  const diff = await reconcileStock();
  if (diff) await syncRedis(diff);                     // 校准 Redis
});
```

**评分点**:
- Redis Lua 预扣 + 订单幂等键（重复预扣防御——SCN-NODE-655）。
- DB 条件更新是超卖最后防线（Redis 只管准入）。
- 失败回补闭环（DB 无库存 → Redis 回补 + 用户补偿）。
- 定期对账校准（Redis/DB diff——SCN-NODE-682 联动）。
