---
title: [MFW-011] Next.js 流式渲染的原理是什么？Suspense 边界起什么作用？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-011：Next.js 流式渲染的原理是什么？Suspense 边界起什么作用？
**答**：
- 流式渲染：服务端用 `renderToPipeableStream` **边渲染边把 HTML 分块写入响应**，不等整棵树完成——首屏（shell）提前到达，TTFB 与 FCP 显著降低。
- `<Suspense>` 边界是流式的**切割单位**：边界内的内容没准备好时，先发 fallback 占位；数据到达后，把真实 HTML 用一段 inline script 换进 DOM（React 原生的流式替换机制）。
- 没有 Suspense 包裹的慢数据会阻塞整个响应（整棵树等它）；所以**每个慢数据源都应该有自己的 Suspense 边界**，或用 loading.js（路由级等价物）。
- 与数据获取的关系：App Router 鼓励「先发起请求再 await」——父组件创建 Promise 不 await、传给子组件 await，让多个慢源并行流水线化。
- 追问钩子：流式对 SEO 安全——爬虫拿到的也是完整流（内容顺序到达），但 status code 必须在 shell 阶段就定死（之后无法改）。

```jsx
// app/dashboard/page.tsx
import { Suspense } from 'react';

// 并行流水线：创建 Promise 不等待，真正用时再 await
function getData(url) {
  const p = fetch(url, { next: { revalidate: 30 } });
  p.catch(() => {}); // 防未处理拒绝
  return p;
}

export default async function Dashboard() {
  const userPromise = getData('/api/user');     // 立即发起
  const chartPromise = getData('/api/chart');   // 立即发起
  return (
    <>
      <Suspense fallback={<UserSkeleton />}>
        <UserCard data={userPromise} />
      </Suspense>
      <Suspense fallback={<ChartSkeleton />}>
        <Chart data={chartPromise} />   {/* 最慢的源被隔离在自己的边界里 */}
      </Suspense>
    </>
  );
}

async function UserCard({ data }) {
  const user = await data; // 子组件才 await
  return <div>{user.name}</div>;
}
```
