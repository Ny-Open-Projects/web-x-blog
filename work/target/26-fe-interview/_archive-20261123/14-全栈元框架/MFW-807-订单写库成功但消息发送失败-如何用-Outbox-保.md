---
title: [MFW-807] 订单写库成功但消息发送失败，如何用 Outbox 保证 Server Action 的原子性
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-807：订单写库成功但消息发送失败，如何用 Outbox 保证 Server Action 的原子性

**答**：
- 结论：把「要发的消息」作为业务数据和订单写进同一个本地事务（outbox 表）；提交后由独立 worker 读取发送、成功后标记，失败定时重试。
- 这样 DB 与消息只有一个本地事务的原子边界，跨系统一致性退化为「至少一次投递 + 消费者幂等」。
- 追问钩子：为什么不让 worker 做强一致？——没有分布式事务管理器时，at-least-once + 幂等是工程上最稳的折中。

```javascript
async function createOrder(input) {
  'use server';
  const tx = await db.begin();
  try {
    const order = await tx.insert('orders', input);
    // 消息与业务同事务落库：要么都成功，要么都不存在
    await tx.insert('outbox', {
      id: order.id,                               // 幂等 key = orderId
      type: 'ORDER_CREATED',
      payload: JSON.stringify(order)
    });
    await tx.commit();
    return { orderId: order.id };
  } catch (e) { await tx.rollback(); throw e; }
}

// worker：独立进程轮询 outbox，至少一次投递
async function deliver() {
  const rows = await db.outbox.pending(100);
  for (const m of rows) {
    await mq.publish(m.type, m.payload, { key: m.id }); // 幂等键
    await db.outbox.markSent(m.id);
  }
}
```
