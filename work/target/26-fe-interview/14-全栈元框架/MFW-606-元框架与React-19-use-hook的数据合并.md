---
title: [MFW-606] React 19 use hook 与 RSC 数据合并
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-606：React 19 use hook 与 RSC 数据

**答**:
- use hook 在 client 组件消费 RSC 传来的 Promise：server 传 promise props（RSC 序列化 Promise RBL-502）→ client `use(promise)` 挂起消费——「server 异步数据直接传 client」而不用 pre-hydrate；Suspense 边界控制挂起。
- use 与 SSR 流式的时序：promise 的 resolve 在 Flight 流中到达（$@ 引用 RBL-501）→ client 的 use 解析——「数据未到时 Suspense fallback、到达后渲染」——RSC 流式与 use 的协同。
- use vs useSyncExternalStore/自定义 hook：use 是「消费任何 thenable」的统一入口（promise/context）——「数据到达即渲染」的声明式表达；错误处理（promise reject → error boundary）。
- 追问钩子：为什么「server 传 Promise」比「server 传 resolved 值」更好？——resolved 值 = server 等 fetch 完才发（串行：payload 等 IO）；Promise = Flight 流先传占位、数据后到（并行：payload 与数据同流）；「传输时序的解耦」：数据慢不影响 payload 首发——use 让 client 消费「未来值」成为一等（流式 RBL-520 的组件 API 化）。

```tsx
// server 组件传 Promise
export default async function Page() {
  return <ClientView reviewsPromise={getReviews(id)} />;   // Promise 直接传（未 await）
}
// client 组件 use 消费
'use client';
import { use } from 'react';
export function ClientView({ reviewsPromise }) {
  const reviews = use(reviewsPromise);                   // 挂起直到 Flight $@ resolve
  return <ul>{reviews.map(r => <li key={r.id}>{r.text}</li>)}</ul>;
}
// Suspense 边界控制挂起
// <Suspense fallback={<Skeleton />}><ClientView ... /></Suspense>
// 错误处理：promise reject → 最近 error boundary
// 对比：await 后传值 = server 串行（payload 晚发）
// use(promise) = payload 与数据并行（RBL-520 TTFB）
```
