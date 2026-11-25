---
title: [NODE-144] 削峰填谷如何用消息队列实现？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-144：削峰填谷如何用消息队列实现？
**答**：
- 思想：入口只做"受理"（校验 + 预扣 + 入队），重活由 worker 以 DB 扛得住的**恒定速率**消化——峰值写入变平稳消费。
- 三要素：Redis 预扣挡超卖（Lua 原子）、MQ 削峰挡 DB（BullMQ limiter 限速）、**202 异步受理**返回排队凭证。
- 可靠性：job 设 attempts + 指数退避；幂等靠业务唯一键（orderId）在消费端去重（NODE-076/146）。
- 可观测：队列长度与消费速率是核心指标，积压超阈值告警并联动扩容 worker。

```javascript
const { Queue, Worker } = require('bullmq');
const orderQueue = new Queue('orders', { connection: redis });

// 入口：3ms 内返回，QPS 10000 也扛得住
const SECKILL_LUA = `local s = tonumber(redis.call("get", KEYS[1]) or "0")
if s <= 0 then return -1 end
redis.call("decr", KEYS[1])
return s - 1`;

app.post('/seckill/:id', async (ctx) => {
  const left = await redis.eval(SECKILL_LUA, 1, `stock:${ctx.params.id}`); // 预扣
  if (left < 0) { ctx.status = 409; ctx.body = { msg: 'sold out' }; return; }
  const orderId = genOrderId();
  await orderQueue.add('create', { uid: ctx.state.uid, skuId: ctx.params.id, orderId },
    { attempts: 3, backoff: { type: 'exponential', delay: 1000 } });
  ctx.status = 202;                                   // 受理而非承诺成功
  ctx.body = { orderId, status: 'QUEUED' };
});

// 消费端：恒速 500/s，错峰写 DB
new Worker('orders', async (job) => {
  await createOrderTx(job.data);                      // 事务 + orderId 唯一键幂等
}, { connection: redis, concurrency: 50, limiter: { max: 500, duration: 1000 } });

setInterval(() => {                                   // 积压监控
  orderQueue.getJobCounts().then((c) => metrics.gauge('mq_waiting', c.waiting));
}, 5000).unref();
```
