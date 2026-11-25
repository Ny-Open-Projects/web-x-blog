---
title: [ZSM-632] dehydration / hydration：服务端缓存怎么安全传到客户端
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-632：dehydration / hydration：服务端缓存怎么安全传到客户端

**答**：
- SSR 流程：服务端 `dehydrate(queryClient)` 把 QueryCache 里的 Query（含 data/dataUpdatedAt）序列化成 JSON → 嵌入 HTML（`<script>window.__QUERY_STATE__</script>`）→ 客户端 `new QueryClient()` 后 `hydrate(dehydratedState)` 灌进缓存——首屏 useQuery 直接命中缓存不发请求，且 staleTime 语义基于服务端的 dataUpdatedAt 继续。
- 安全三原则：1) **dehydrate 默认剔除 error**（错误对象不可序列化且可能泄内部信息）；2) `shouldDehydrateQuery` 白名单——只传输首屏必需的 query（`shouldDehydrateQuery: (q) => q.state.status === 'success' && q.state.dataUpdatedAt > Date.now() - 60000`）；3) **必须每请求新建 QueryClient**——共享实例会把用户 A 的数据带给用户 B（资损级事故）。
- 时钟偏差：服务端 dataUpdatedAt 与客户端时钟可能差几秒——hydrate 时 staleTime 判断用的服务端时间戳会让缓存「过早过期」或「过期不拉」，重流控场景用 `defaultOptions.queries.staleTime` 放宽或校时。
- 版本一致性：HTML 里的缓存和 JS bundle 版本要一致（CDN 缓存错位会让客户端 hydrate 出旧 schema 数据）——dehydrated state 里带 data 结构版本号做防御。
- 追问钩子：React 19 的 `<QueryClientProvider>` + RSC 环境（Next.js App Router）下，Server Components 直接传 dehydrated state 作为 props 是标准接法，避免 window 全局。

```javascript
// 服务端（Next.js App Router 示例）
export default async function Page() {
  const queryClient = new QueryClient()          // ① 每请求新实例
  await queryClient.prefetchQuery({              // ② 服务端预取
    queryKey: ['todos', 'list'],
    queryFn: () => api.getTodos(),
    staleTime: 10 * 1000,
  })
  const dehydrated = dehydrate(queryClient, {
    shouldDehydrateQuery: (q) => q.state.status === 'success',   // ③ 白名单
  })
  return (
    <HydrationBoundary state={dehydrated}>       // ④ 通过 props 传递
      <TodoList />
    </HydrationBoundary>
  )
}

// 客户端：HydrationBoundary 内部就是 hydrate(client, state)
// 首屏 useQuery(['todos','list']) 命中服务端缓存，staleTime 从 dataUpdatedAt 起算

// 时钟偏差防御
const dehydratedState = dehydrate(queryClient, {
  defaultShouldDehydrateQuery: (q) => q.state.status === 'success',
})
// 客户端兜底：首次 mount 强制 revalidate 一次
// defaultOptions: { queries: { staleTime: 0, refetchOnMount: 'always' } }
```
