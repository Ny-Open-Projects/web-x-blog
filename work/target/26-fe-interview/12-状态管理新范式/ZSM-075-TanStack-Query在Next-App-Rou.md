---
title: [ZSM-075] Next.js App Router 里 TanStack Query 怎么搭？QueryClient 为什么不能放模块顶层？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-075：Next.js App Router 里 TanStack Query 怎么搭？QueryClient 为什么不能放模块顶层？
**答**：
- QueryClient 不能放模块顶层：服务端模块常驻，所有请求共享一个 client → 用户数据串味、缓存互相污染。必须「每请求一个」（用 useState/ref 惰性创建）。
- 结构：`'use client'` 的 Providers 组件持有 `useState(() => makeQueryClient())`，包 QueryClientProvider；浏览器侧可用单例（无并发请求问题）。
- dehydrate/hydrate 在 RSC 里完成首屏预热；导航后 App Router 自动缓存 RSC payload，Query 缓存独立于路由缓存，注意卸载后的 gcTime。
- 浏览器.makeQueryClient 可设 staleTime 略大于 0，避免 StrictMode 双挂载重复请求。

```javascript
// providers.tsx
'use client'
export function Providers({ children }) {
  const [qc] = useState(() => new QueryClient({ // 每请求实例
    defaultOptions: { queries: { staleTime: 60_000 } },
  }))
  return <QueryClientProvider client={qc}>{children}</QueryClientProvider>
}
```
