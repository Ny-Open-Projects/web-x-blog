---
title: [MFW-012] loading.js 和 Suspense fallback 有什么区别？粒度与嵌套规则？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-012：loading.js 和 Suspense fallback 有什么区别？粒度与嵌套规则？
**答**：
- `loading.js` 是 Next 的**路由级 Suspense 语法糖**：等价于把 page.tsx 自动包进 `<Suspense fallback={<Loading/>}>`，在该路由（含懒加载段）渲染挂起时展示。
- 粒度：loading.js 作用于**整个 page**（含 async 的 layout 也会挂起），Suspense 可精确到**组件级**——一个慢组件一个边界，其余内容立即显示。
- 嵌套规则：导航时父级的 loading 先亮（page 还没数据），进入后页内自己的 Suspense 接管；多层 loading.js 从上到下嵌套展示。
- 性能要点：loading.js 应展示骨架屏布局占位，避免布局抖动（CLS）；内部再拆 Suspense 让关键内容先出。
- 注意：loading.js 只在**导航/初始加载挂起**时出现，Client Component 里的 fetch 不归它管。

```jsx
// app/products/loading.js —— 路由级，等价于 page 外面包一层 Suspense
export default function Loading() {
  return (
    <div className="grid grid-cols-4 gap-4">
      {Array.from({ length: 8 }).map((_, i) => (
        <div key={i} className="h-40 bg-gray-100 animate-pulse rounded" />
      ))}
    </div>
  );
}
```

```jsx
// app/products/page.tsx —— 页内再细拆组件级边界
import { Suspense } from 'react';

export default async function Page() {
  return (
    <>
      <Suspense fallback={<FilterSkeleton />}>   {/* 组件级：比 loading.js 更细 */}
        <Filters />      {/* 内部 await 慢接口，只挂起这一块 */}
      </Suspense>
      <Suspense fallback={<ListSkeleton />}>
        <ProductList />  {/* 另一个独立慢源 */}
      </Suspense>
    </>
  );
}
```
