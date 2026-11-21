---
title: [NODE-161] 设计一个秒杀服务端（限流/预扣/队列）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-161：设计一个秒杀服务端（限流/预扣/队列）？
**答**：
- 三级漏斗：**网关限流挡量**（令牌桶，NODE-132）→ **Redis 预扣挡超卖**（Lua 原子扣减）→ **MQ 削峰挡 DB**（恒速消费，NODE-144）。
- 入口毫秒级返回：校验 → 一人一单去重 → 预扣 → 入队 → 202 + 排队凭证；前端轮询或 WS 查结果。
- 数据库最终一致：消费端事务里 `UPDATE stock SET n = n - 1 WHERE sku = ? AND n > 0` 扣真实库存，失败回补 Redis。
- 收尾细节：超时未支付释放库存（延迟消息）、热点 sku 库存分桶（把一个 key 拆 10 个降低竞争）。

```mermaid
flowchart TD
    A[用户抢购请求] --> B[网关令牌桶限流]
    B --> C[一人一单去重]
    C --> D[Redis 预扣库存 Lua 原子扣减]
    D -- 库存不足 --> E[直接返回售罄]
    D -- 预扣成功 --> F[消息队列异步下单]
    F --> G[立即返回排队中]
    G --> H[消费端恒速创建订单]
    H --> I[数据库事务扣真实库存]
    I -- 失败 --> J[回补 Redis 库存]
    I -- 成功 --> K[通知用户下单成功]
```

```javascript
const SECKILL_LUA = `local s = tonumber(redis.call("get", KEYS[1]) or "0")
if s <= 0 then return -1 end
redis.call("decr", KEYS[1])
return s - 1`;

app.post('/seckill/:skuId', limiter({ qps: 5000 }), async (ctx) => {
  const uid = ctx.state.uid;
  if (!(await redis.set(`seckill:dup:${ctx.params.skuId}:${uid}`, 1, 'PX', 86400000, 'NX'))) {
    ctx.throw(409, '重复参与');                       // 一人一单
  }
  const left = await redis.eval(SECKILL_LUA, 1, `stock:${ctx.params.skuId}`);
  if (left < 0) { ctx.status = 409; ctx.body = { msg: 'sold out' }; return; }
  const orderId = genOrderId();
  await orderQueue.add('seckill', { skuId: ctx.params.skuId, uid, orderId },
    { attempts: 5, backoff: { type: 'fixed', delay: 500 } });
  ctx.status = 202;
  ctx.body = { orderId, status: 'PROCESSING' };       // 异步结果页
});
```
