---
title: [MFW-017] Data Cache 的 revalidate 和 tags 怎么用？on-demand 失效怎么做？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-017：Data Cache 的 revalidate 和 tags 怎么用？on-demand 失效怎么做？
**答**：
- `next: { revalidate: N }`：时间失效，后台 stale-while-revalidate 式刷新（先回旧值，再重取）。
- `next: { tags: ['a','b'] }`：给缓存打标签，用 `revalidateTag('a')` **主动失效**——写操作完成后立即刷新读缓存，是电商库存/订单场景的标准做法。
- 三种失效方式优先级：**写后 `revalidateTag`（最准）> 按需路由 `revalidatePath`（页面级）> 时间 revalidate（兜底）**。
- tags 要设计成「业务实体粒度」：`product-${id}`、`products-list`，失效时精准打击，避免整站重渲染。
- 注意：`revalidateTag` 只能在 Server Action/Route Handler 里调（服务端），且会连带失效引用该数据的 Full Route Cache。

```ts
// app/api/products/[id]/route.ts —— 更新商品
import { revalidateTag } from 'next/cache';

export async function PATCH(req, { params }) {
  const body = await req.json();
  await db.product.update({ where: { id: params.id }, data: body });
  revalidateTag(`product-${params.id}`);   // 精准失效单商品
  revalidateTag('products-list');          // 列表页也要刷新
  return Response.json({ ok: true });
}
```

```jsx
// 读侧：两个粒度的缓存都打 tag
export async function getProduct(id) {
  return fetch(`${process.env.API}/products/${id}`, {
    next: { revalidate: 600, tags: [`product-${id}`, 'products-list'] },
  }).then((r) => r.json());
}

// 或者对 ORM 数据：unstable_cache 同样支持 tags
const list = unstable_cache(() => db.product.findMany(), ['pl'], { tags: ['products-list'] });
```
