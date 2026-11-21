---
title: [MFW-171] Server Action 的错误处理与重试策略怎么设计？
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-171：Server Action 的错误处理与重试策略怎么设计？
**答**：
- 错误分三类：可重试（网络抖动、瞬时 5xx）、不可重试（校验失败、权限拒绝）、部分成功（多步事务断在中间），先分类再定策略。
- Server Action 会自动重试幂等请求（Next.js 对 GET 语义的 Action 有自动重试），所以 Action 必须**幂等化**——否则用户双击或框架重试会重复下单。
- 用户可见错误走 `useActionState` 返回结构化结果 `{ ok, message, fieldErrors }`，而不是 throw：throw 只用于让 error.js 接管的意外错误。
- 多步写操作要包事务或加补偿逻辑；Action 内不要裸写「先扣库存再建订单」两段独立 IO。
- 未捕获异常在服务端会被序列化为通用错误（消息不透传给客户端，防泄漏），要在 Action 里显式返回可展示的信息。

```javascript
'use server';
import { revalidateTag } from 'next/cache';

class RetryableError extends Error {}

export async function createOrder(formData) {
  const requestId = formData.get('requestId'); // 客户端生成的幂等键
  // 幂等：同一 requestId 只生效一次
  const existing = await db.orders.findByRequestId(requestId);
  if (existing) return { ok: true, orderId: existing.id, duplicated: true };

  try {
    // 单事务包裹多步写，避免部分成功
    const order = await db.transaction(async (tx) => {
      const stock = await tx.products.decrementStock(formData.get('sku'), 1);
      if (!stock) return { failed: 'SOLD_OUT' };
      return tx.orders.create({ ...Object.fromEntries(formData), requestId });
    });
    if (order.failed) return { ok: false, code: order.failed }; // 业务失败不 throw
    revalidateTag('orders');
    return { ok: true, orderId: order.id };
  } catch (e) {
    // 瞬时错误标记为可重试，客户端据此提示「重试」；其余交给 error.js
    if (isTransient(e)) throw new RetryableError('transient');
    return { ok: false, code: 'UNKNOWN' };
  }
}
```
