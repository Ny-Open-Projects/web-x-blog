---
title: [NODE-380] Node 服务的分布式事务边界：何时用 saga/最终一致？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-380：分布式事务边界
**答**:
- 决策顺序：优先单库事务解决（拆服务不拆数据，能在一个 PG 事务内完成的绝不分布式）；跨服务才考虑 saga（编排式：中央协调器按序调用 + 逆序补偿，或协同式：事件链各自触发）。
- saga 设计核心：每步必须有补偿（取消订单 ↔ 恢复库存 ↔ 退积分），补偿也要幂等；中间态可见（订单"支付中"状态，用户与下游都能理解）；补偿失败进人工/重试队列（ARC-324 对账兜底）。
- 不用 2PC/XA 的理由：同步阻塞、可用性差、运维复杂；业务几乎都用"最终一致 + 补偿 + 对账"。
- 本地消息表模式：业务写与事件写同一本地事务，再异步投递 MQ——避免"DB 写成功但 MQ 发送失败"的经典不一致。
- TCC（try/confirm/cancel）用于强一致资金场景，实现成本高，能用 saga 不用 TCC。
```javascript
// 本地消息表
await db.tx(async (t) => {
  await t.query('update orders set status=paying where id=$1', [id]);     // 业务写
  await t.query(`insert into outbox(topic, payload, status) values($1,$2,'pending')`,
    ['order.paying', JSON.stringify({ orderId: id })]);                   // 同事务写事件
});
// 独立 worker 扫 outbox pending → 发 MQ → 标记 sent（重试幂等，下游消费幂等）
```
