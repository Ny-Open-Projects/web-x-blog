---
title: [R19-217] Action 中多表写入怎么保证原子性（下单：订单+库存+积分）？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-217：Action 中多表写入怎么保证原子性？
**答**：
- 数据库事务包裹多表写入（Prisma $transaction / SQL BEGIN），任一步失败整体回滚——action 里只管「调事务」。
- 跨服务写（订单服务 + 积分服务）：本地事务 + 消息队列最终一致，或 Saga 补偿；action 返回「已受理」而非「全部完成」。
- 幂等键：事务以 requestId 为唯一键，重试安全。
- 失败返回：事务失败返回结构化错误（库存不足 code），不 throw 5xx 让用户看到白屏。
- 审计点：事务内不要放外部 HTTP 调用（慢、且失败回滚后外部动作无法撤销），外部通知放事务提交后。
```javascript
await prisma.$transaction([
  prisma.order.create({ data: orderData }),
  prisma.stock.update({ where: { id }, data: { count: { decrement: qty } } }),
  prisma.point.update({ where: { userId }, data: { value: { decrement: cost } } })
], { isolationLevel: 'Serializable' })
```
