---
title: [MFW-128] RRv7 的多 loader 并行与流式（defer）怎么做？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-128：RRv7 的多 loader 并行与流式（defer）怎么做？
**答**：
- 并行：嵌套路由匹配到的**所有 loader 同时发起**（不是瀑布），这是 RRv7/Remix 的核心卖点——Next 靠开发者自己 Promise.all，RRv7 是框架默认行为。
- 流式：loader 返回 `Promise` 不 await（v7 直接返回带 promise 的对象），组件里用 `<Await>` + `<Suspense>` 消费——慢数据不阻塞首屏。
- 关键点：返回裸 promise 时错误要在 `<Await errorElement>` 里处理，否则会漏到上层 ErrorBoundary；`useLoaderData` 只拿同步部分。
- 与 Next 对照：机制同构（RR 的 Await ≈ Suspense + RSC await），但 RR 不需要 RSC，客户端组件直接消费。

```tsx
// app/routes/product.tsx
export async function loader({ params }: any) {
  // 同步数据立即返回；慢数据以 promise 下发
  const product = await db.product.findUnique({ where: { id: params.id } });
  const reviews = getReviews(params.id); // 不 await -> 流式
  return { product, reviews };
}

import { Suspense } from 'react';
import { Await, useLoaderData } from 'react-router';

export default function Product() {
  const { product, reviews } = useLoaderData<typeof import('./product').loader>();
  return (
    <>
      <h1>{product.name}</h1>          {/* 立即渲染 */}
      <Suspense fallback={<p>评论加载中…</p>}>
        <Await resolve={reviews} errorElement={<p>评论加载失败</p>}>
          {(list) => <ReviewList items={list} />}
        </Await>
      </Suspense>
    </>
  );
}
```

**追问**：

1. 嵌套路由里某个 loader 抛错，其他并行 loader 会怎样？→ 整条路由进 ErrorBoundary，其他结果被丢弃；要高可用就把易错数据降级成 defer 的 promise。
2. defer 的 promise 在 hydrate 前 reject 会怎样？→ 必须由 `<Await errorElement>` 接住，否则冒泡到路由级 ErrorBoundary 把整页干掉。
3. 流式返回后 `useLoaderData` 里拿到的到底是什么？→ 拿到的是 promise 本身，同步字段可直读，消费 promise 必须走 `<Await>` 或 `use()`。
