---
title: [R19-101] 首屏优化中代码分割与 Suspense 流式如何组合？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-101：首屏优化中代码分割与 Suspense 流式如何组合？
**答**：
- 思路是"关键路径最小化"：首屏必需的数据阻塞渲染保证可见即完整，非关键模块（图表、榜单）用 Suspense 包住随流注入。
- Next.js App Router 下：loading.js 提供段级即时骨架；页面内更细粒度用 `<Suspense>` 包异步服务端组件。
- 首屏之外的交互模块用 React.lazy 代码分割，配合 hover/空闲预取消除点击延迟。
- 度量闭环：用 LCP/INP 指标验证，流式边界划得是否合理看 TTFB 到 LCP 的间隔。

```jsx
// 首屏优化组合：关键内容阻塞 + 非关键内容流式 + 交互模块懒加载
import { lazy, Suspense } from 'react';

export default function Dashboard() {
  return (
    <main>
      {/* 首屏关键数据：阻塞渲染，保证可见即完整 */}
      <KpiCards />

      {/* 非关键模块：稍后随流注入，不拖慢首屏 */}
      <Suspense fallback={<ChartSkeleton />}><SlowChart /></Suspense>
      <Suspense fallback={<TableSkeleton />}><BigRankTable /></Suspense>

      {/* 首屏之外的交互模块懒加载（该页为客户端组件或 'use client' 区域） */}
      <Suspense fallback={null}>
        <LazySettings />
      </Suspense>
    </main>
  );
}

const LazySettings = lazy(() => import('./SettingsPanel'));
// Next.js 中配合 app/dashboard/loading.tsx 提供段级骨架，导航瞬间就有响应
```

---

## 第十六章 RSC 与 Next.js 实战（R19-102 ~ R19-107）
