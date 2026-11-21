---
title: [NODE-160] 设计一个订单服务简化版（状态机/事务/幂等）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-160：设计一个订单服务简化版（状态机/事务/幂等）？
**答**：
- 状态机驱动一切：`CREATED → PAID → SHIPPED → DONE`，分支 `CANCELED/REFUNDED`；流转函数是唯一入口，非法流转拒绝。
- 并发正确性：流转用 `updateMany where status = 当前态` 做 **CAS 乐观锁**，防两个回调同时改状态。
- 幂等三处：支付回调按状态机天然幂等（已 PAID 再回调 count=0 直接 ACK）、下单按 orderId 唯一键、消息消费按 outbox（NODE-146）。
- 超时关单：下单投递**延迟消息**（15min），消费时校验仍是 CREATED 才取消并回补库存。

```javascript
const TRANSITIONS = {
  CREATED: ['PAID', 'CANCELED'],
  PAID: ['SHIPPED', 'REFUNDED'],
  SHIPPED: ['DONE'],
};

async function transition(orderId, to) {
  return db.$transaction(async (tx) => {
    const o = await tx.order.findUnique({ where: { id: orderId } });
    if (!TRANSITIONS[o.status]?.includes(to)) {
      throw badRequest(`非法流转 ${o.status} → ${to}`);
    }
    const updated = await tx.order.updateMany({   // CAS：只允许从当前状态流转
      where: { id: orderId, status: o.status },
      data: { status: to },
    });
    if (updated.count === 0) throw conflict('并发流转冲突'); // 幂等兜底
    return o;
  });
}

// 超时关单：延迟消息，消费时二次校验状态
await closeQueue.add('close', { orderId },
  { delay: 15 * 60 * 1000, jobId: `close:${orderId}` }); // jobId 防重复入队
// 消费端：status 仍为 CREATED 才 CANCELED + 回补库存
```
