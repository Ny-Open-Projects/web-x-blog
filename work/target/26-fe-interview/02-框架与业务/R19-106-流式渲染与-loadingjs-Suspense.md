---
title: [R19-106] 流式渲染与 loading.js、Suspense 如何配合？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-106：流式渲染与 loading.js、Suspense 如何配合？
**答**：
- loading.js 是段级约定：导航发生时先推骨架，页面数据就绪后再替换，对用户是"瞬间响应"。
- 页面内部再用 Suspense 划分更细的流式单元：谁慢谁自己挂起，不阻塞兄弟节点与外壳。
- 划分原则：外壳与首屏关键内容不包 Suspense（阻塞渲染保证完整），图表、榜单、推荐等非关键模块各自包。
- Suspense 的 fallback 要与真实内容布局一致，避免内容注入后布局跳动（CLS）。

```tsx
// app/dashboard/loading.tsx —— 段级即时 loading：导航瞬间就显示
export default function Loading() {
  return <DashboardSkeleton />;
}

// app/dashboard/page.tsx —— 更细粒度：页面内部用 Suspense 划分流式单元
import { Suspense } from 'react';

export default function Dashboard() {
  return (
    <>
      <h1>概览</h1>
      <Suspense fallback={<ChartSkeleton />}>
        <Chart />        {/* 内部 await fetch，未就绪时先推 fallback */}
      </Suspense>
      <Suspense fallback={<ListSkeleton />}>
        <SlowList />     {/* 谁慢谁自己挂起，不阻塞兄弟节点 */}
      </Suspense>
    </>
  );
}
```
