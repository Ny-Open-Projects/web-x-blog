---
title: [MFW-015] Next.js 四种缓存（Request/Router/Data/Full Route）分别是什么、怎么协作？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-015：Next.js 四种缓存（Request/Router/Data/Full Route）分别是什么、怎么协作？
**答**：
- **Request Memoization**：同一次渲染请求内，相同 URL/参数的 fetch 只发一次（React `cache()` 语义），生命周期 = 单次请求。解决「组件树多处请求同一数据」。
- **Data Cache**：fetch 跨请求、跨部署的持久缓存（服务端，可配 revalidate/next.tags），生命周期由 `next: { revalidate, tags }` 控制。
- **Full Route Cache**：整条路由的 HTML + RSC Payload 在构建期/运行期的缓存，静态路由默认启用；数据没变时连渲染都省掉。
- **Client Router Cache**：浏览器内存里存已访问路由的 RSC Payload，导航/返回时先用缓存渲染（staleTime 默认：动态 30s / 静态 5min）。
- 协作链：fetch 先看 Request Memo → 再看 Data Cache；Data 变了会失效对应 Full Route；Router Cache 是客户端最后一层。**只有 fetch 默认进 Data Cache，DB 直查（如 ORM）不缓存**，要用 `unstable_cache`/`revalidate` 控制。

```jsx
// 1) Request Memoization：一次渲染内去重
async function getUser() {
  return fetch('https://api.example.com/user').then((r) => r.json());
}
// Layout 和 Page 都调 getUser() —— 同一请求内只发一次真实网络请求

// 2) Data Cache：跨请求持久化
const res = await fetch('https://api.example.com/posts', {
  next: { revalidate: 3600, tags: ['posts'] }, // 1h 缓存 + 标签
});

// 3) ORM 数据的缓存包装（Prisma 不会自动缓存）
import { unstable_cache } from 'next/cache';
const getProducts = unstable_cache(
  () => db.product.findMany({ take: 20 }),
  ['products-list'],
  { revalidate: 300, tags: ['products'] },
);

// 4) Client Router Cache：控制新鲜度（next.config.js）
// const nextConfig = { experimental: { staleTimes: { dynamic: 30, static: 180 } } };
```
