---
title: [MFW-006] App Router 一次页面请求的完整渲染流程是怎样的？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-006：App Router 一次页面请求的完整渲染流程是怎样的？
**答**：
- 顺序：**中间件（middleware）→ 匹配路由段 → 检查 Full Route Cache → 命中直接返回；未命中则依次执行 layout→page 的 Server Component，并行启动数据请求 → 渲染为 HTML + RSC Payload → 流式返回 → 客户端 hydrate**。
- 缓存命中判定在最前面：`revalidate` 未过期的静态页直接从 Full Route Cache 拿 HTML，跳过整个 React 渲染（这是静态化的价值）。
- 渲染期：Server Component 里 await 的数据获取并行发生（同层组件不互相阻塞，除非嵌套依赖）；`<Suspense>` 边界允许先发 shell。
- 客户端导航时上面流程缩短为：只请求 RSC Payload，React patch 更新，不再整页 HTML。
- 追问钩子：动态函数（cookies/headers/searchParams）的使用会把路由打入「动态渲染」，跳过 Full Route Cache。

```jsx
// app/blog/[slug]/page.tsx
import { Suspense } from 'react';

export const revalidate = 300; // 决定 Full Route Cache 生命周期

export default async function Page({ params }) {
  const { slug } = params;
  return (
    <>
      {/* 顶层：静态壳，立即流式发送 */}
      <Header title={slug} />
      {/* 慢数据：Suspense 边界内流式补齐 */}
      <Suspense fallback={<CommentsSkeleton />}>
        <Comments slug={slug} /> {/* 内部 fetch 有 Data Cache */}
      </Suspense>
    </>
  );
}

async function Comments({ slug }) {
  const data = await fetch(`https://api.example.com/comments?slug=${slug}`, {
    next: { revalidate: 60 }, // Data Cache：60s 内重复渲染不发真实请求
  }).then((r) => r.json());
  return <List items={data} />;
}
```
