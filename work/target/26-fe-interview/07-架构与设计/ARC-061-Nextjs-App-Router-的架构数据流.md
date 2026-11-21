---
title: [ARC-061] Next.js App Router 的架构数据流是怎样的（RSC / Server Actions）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-061：Next.js App Router 的架构数据流是怎样的（RSC / Server Actions）？
**答**：
- RSC（React Server Component）在服务端执行、不打包进 JS bundle，可直接 await 数据源；客户端组件用 `'use client'` 显式标记，二者通过 props（可序列化）传递。
- Server Actions 让"表单提交/变更"直接调服务端函数，省去手写 API 端点；但仍需鉴权、校验、revalidate。
- 架构收益：数据获取下沉到服务端减少瀑布请求与包体积；代价是心智模型复杂（序列化边界、缓存语义）。

```typescript
// app/orders/page.tsx —— Server Component：服务端直连数据源，零客户端 fetch
export default async function OrdersPage() {
  const orders = await db.order.findMany({ where: { userId: await currentUserId() } }); // 直连 DB
  return <OrderTable orders={orders} />;   // 可序列化 props 传给客户端/服务端组件
}

// app/orders/actions.ts —— Server Actions：变更走服务端函数，带鉴权与缓存失效
'use server';
export async function shipOrder(formData: FormData) {
  const user = await requireRole('OPERATOR');              // 鉴权必须在 action 内做
  const id = z.string().parse(formData.get('orderId'));    // 入参校验
  await db.order.update({ where: { id }, data: { status: 'shipped' } });
  revalidatePath(`/orders/${id}`);                          // 声明式失效缓存
}

// app/orders/ship-button.tsx —— Client Component 调 action
'use client';
export function ShipButton({ orderId }: { orderId: string }) {
  return <form action={shipOrder}><input type="hidden" name="orderId" value={orderId} />
    <button>发货</button></form>;
}
```
