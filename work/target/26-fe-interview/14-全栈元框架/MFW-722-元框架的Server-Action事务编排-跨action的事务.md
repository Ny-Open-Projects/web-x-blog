---
title: [MFW-722] Server Action 事务编排：跨 action 的事务
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-722：Server Action 事务编排

**答**:
- 跨 action 的事务问题：1) **多个 action 的原子性**（下单 action（创建订单）+ 库存 action（扣库存）——两个独立 action 的操作需要原子性（一个失败另一个也要回滚——分布式事务/Saga）；2) **action 的不可组合**（每个 action 是独立请求——不能在 action A 内调用 action B（跨 action 调用 = 新 HTTP 请求——事务边界断裂）；3) **解决：单 action 内多操作**（把多操作合并到一个 action（db.$transaction 内多个操作——单事务多表）；4) **跨服务的 Saga**（不同服务的操作（DB + 支付网关）——Saga 模式（补偿操作）。
- Saga 的补偿模式：步骤 1 成功 → 步骤 2 失败 → 补偿步骤 1（回滚已完成的操作——「正向操作 + 反向补偿」的链式执行）。
- 追问钩子：为什么「把多操作合并到一个 action」是跨事务问题的首选解？——单 action 内 = 单事务（db.$transaction 原子保证——无跨事务一致性风险）；跨 action = 分布式事务（复杂度暴涨——Saga/2PC）；「合并到单 action」的前提是操作在同一 DB（同事务可达）；跨 DB/跨服务 = 不可避免需要 Saga——「同一 DB 合并、跨服务 Saga」的分层解。

```typescript
// 单 action 多操作（同 DB 事务）
'use server';
export async function placeOrder(orderData: OrderInput) {
  return db.$transaction(async (tx) => {
    const order = await tx.order.create({ data: orderData });       // 创建订单
    await tx.inventory.update({ where: { sku: orderData.sku },       // 扣库存
      data: { count: { decrement: orderData.qty } } });
    await tx.points.create({ data: { userId: orderData.userId,        // 加积分
      amount: orderData.total * 0.01 } });
    return order;
  });                                                    // 单事务：任一失败全回滚
}
// 跨服务 Saga（补偿模式）
'use server';
export async function placeOrderWithPayment(orderData: OrderInput) {
  const order = await db.order.create({ data: orderData });  // 步骤 1：DB
  try {
    const payment = await paymentService.charge(order.total, order.id);  // 步骤 2：支付网关
    await db.order.update({ where: { id: order.id }, data: { status: 'paid', paymentId: payment.id } });
    return order;
  } catch (e) {
    await db.order.update({ where: { id: order.id }, data: { status: 'payment-failed' } });   // 补偿：标记失败
    await inventoryService.restore(orderData.sku, orderData.qty);   // 补偿：恢复库存
    throw e;                                             // 错误上报
  }
}
```
