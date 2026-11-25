---
title: [MFW-815] Server Action 事务提交成功但响应在网络中丢失，客户端重试怎么防重复执行
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-815：Server Action 事务提交成功但响应在网络中丢失，客户端重试怎么防重复执行

**答**：
- 结论：重试必须复用同一个幂等键（不是生成新键）；服务端用该键查已提交结果并直接回放，而不是再次执行事务。
- 落地：提交前生成 requestId 随请求发送并写入幂等表；重试带同一 requestId；命中已完成记录回放结果。
- 追问钩子：幂等记录多久清理？——至少覆盖客户端最大重试窗口 + 时钟偏移，通常 T+24h。

```javascript
// 客户端：首次与重试共用同一 requestId
function useCheckout() {
  const requestIdRef = useRef(crypto.randomUUID());   // 只生成一次
  return () => checkout({ requestId: requestIdRef.current, cart });
}

// 服务端 Action
async function checkout({ requestId, cart }) {
  'use server';
  const hit = await db.idem.find(requestId);
  if (hit?.state === 'done') return hit.result;       // 回放，不重做
  const tx = await db.begin();
  try {
    const order = await tx.orders.create(cart);
    await tx.idempotency.upsert(requestId, 'done', order);
    await tx.commit();
    return order;
  } catch (e) {
    // 提交成功但响应丢失：下次重试靠 requestId 回放
    await tx.rollback(); throw e;
  }
}
```
