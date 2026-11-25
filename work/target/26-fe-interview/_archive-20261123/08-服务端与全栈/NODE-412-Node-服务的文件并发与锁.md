---
title: [NODE-412] Node 服务的并发控制（乐观锁/悲观锁/队列串行化）如何选？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-412：并发控制选型
**答**:
- 乐观锁（默认选择）：版本号/条件更新（update ... where version=n），冲突率低的场景成本最小；冲突响应给前端合并 UI（ARC-483）。
- 悲观锁（select for update）：冲突率高或必须串行的短临界区（库存扣减、余额变更）——注意锁范围最小（行级）、事务内短持锁（锁内不做外部调用）、死锁检测与重试（按固定顺序加锁防死锁）。
- 分布式锁（Redis）：跨进程/跨服务的互斥（定时任务 NODE-345、单飞 NODE-378）——用于"同一时刻只有一个执行者"，不用于数据正确性（那用 DB 约束）。
- 队列串行化：同一实体操作串行（同订单状态变更按 orderId 分区投递 MQ，天然串行，避免锁）——高并发写热点实体的首选。
- 热点行优化：库存超热点行（NODE-384 分片配额）、批量合并扣减（攒批一次 update）。
```javascript
// 乐观锁 + 冲突检测
const r = await db.query(
  `update accounts set balance = balance - $1, version = version + 1
   where id = $2 and version = $3 and balance >= $1`, [amt, id, ver]);
if (r.rowCount === 0) throw new Conflict('版本冲突或余额不足');   // 前端重拉合并
// 悲观锁短临界区
await db.tx(async t => {
  const row = await t.query('select * from stock where sku=$1 for update', [sku]); // 锁行
  await t.query('update stock set qty = qty - $1 where sku = $1', [qty]);
});                                                              // 锁内无外部调用
```
