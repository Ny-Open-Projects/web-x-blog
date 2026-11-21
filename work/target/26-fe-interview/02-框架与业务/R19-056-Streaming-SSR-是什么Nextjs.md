---
title: [R19-056] Streaming SSR 是什么？Next.js 里怎么用？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-056：Streaming SSR 是什么？Next.js 里怎么用？
**答**：
- 服务端不必等整棵组件树的数据就绪：先流式输出静态外壳，慢的部分由 Suspense 边界分块补发。
- 用户更早看到首屏内容，慢数据区域显示骨架屏，TTFB 与 FCP 显著改善。
- App Router 里最简单的用法是路由目录放 loading.jsx，Next 自动包 Suspense。
- 也可以在页面内手动放多个 Suspense 边界实现分段流式。

```jsx
// app/dashboard/loading.jsx —— 路由级 streaming UI
export default function Loading() {
  return <p>仪表盘加载中...</p>;
}

// 页面内更细粒度的分段流式输出
export function Dashboard() {
  return (
    <>
      <Suspense fallback={<RevenueSkeleton />}>
        <Revenue />   {/* 查询快的部分先流出去 */}
      </Suspense>
      <Suspense fallback={<StatsSkeleton />}>
        <UserStats /> {/* 慢查询不阻塞整个页面 */}
      </Suspense>
    </>
  );
}
```

---

## 第九章 React Testing Library 测试（R19-057 ~ R19-060）
