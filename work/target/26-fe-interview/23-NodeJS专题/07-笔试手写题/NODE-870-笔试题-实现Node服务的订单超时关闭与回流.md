---
title: [NODE-870] 笔试题——实现订单超时关闭与库存回流（延迟任务）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-870：手写超时关闭

**需求与边界**：
- 需求：订单超时（SCN-联想-862）——① 延迟关闭任务（15 分钟——延迟队列 SCN-NODE-693）；② 幂等关闭（已支付不关——状态机守卫 SCN-FIN-548）；③ 库存回流（关单回补——SCN-NODE-738 回补）；④ 回流开抢通知（SCN-联想-862）。
- 边界：① 关单与支付的竞态（支付回调与关单并发——version 守卫，SCN-FIN-548）；② 回流的库存校准（Redis 与 DB——SCN-NODE-738）；③ 关单的通知（用户——SCN-NODE-685）。

**答**：
```javascript
// 延迟关闭（SCN-NODE-693 延迟队列）
await delayedQueue.schedule('order-timeout', orderId, 15 * 60_000);
consumer.on('order-timeout', async (orderId) => {
  const r = await db.query(`UPDATE orders SET status = 'CLOSED', version = version + 1
    WHERE id = $1 AND status IN ('CREATED','PAYING') RETURNING id`, [orderId]);   // 状态机守卫（SCN-FIN-548）
  if (!r.rowCount) return;                             // 已支付：不关（竞态防御）
  await redis.incr(`stock:${order.sku}`);              // 库存回流（SCN-NODE-738）
  await mq.publish('stock.refund', { sku: order.sku });   // DB 侧回流（异步）
  notify(order.userId, { type: 'ORDER_CLOSED', note: '库存将回流' });   // SCN-联想-862
});
```

**评分点**:
- 延迟队列 + 状态机守卫（已支付不关——SCN-FIN-548）。
- 库存回流双通道（Redis 立即 + DB 异步——SCN-NODE-738）。
- 用户通知（SCN-联想-862）。
- 幂等（version 条件更新——重复关单无副作用）。
