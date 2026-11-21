---
title: [ZSM-074] TanStack Query 的 dehydrate/hydrate 是什么？SSR 数据怎么流进客户端缓存？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-074：TanStack Query 的 dehydrate/hydrate 是什么？SSR 数据怎么流进客户端缓存？
**答**：
- dehydrate 把 QueryClient 缓存序列化成可传输对象；hydrate 在客户端把它灌进浏览器 QueryClient，客户端首渲染直接命中缓存，无 loading 闪烁。
- 流程：RSC/服务端入口 fetch prefetch → `dehydrate(client)` → 数据嵌进 HTML → 客户端 `useHydratedClient`（new QueryClient + hydrate）。
- 关键点：每请求新建 QueryClient（防串用户）；prefetch 的查询要配相同 key；dehydratedState 默认含 stale 数据也可传，靠 staleTime 控制客户端是否重取。
- RSC 直传 props vs Query hydrate：一次性的静态数据直传更轻；需要客户端后续缓存/失效/交互的数据走 hydrate。

```javascript
// 服务端组件
export default async function Page() {
  const qc = new QueryClient()
  await qc.prefetchQuery({ queryKey: ['goods', kw], queryFn: () => api.goods(kw) })
  return (
    <HydrationBoundary state={dehydrate(qc)}>
      <GoodsList kw={kw} /> {/* 客户端 useQuery 同 key 直接命中 */}
    </HydrationBoundary>
  )
}
```
