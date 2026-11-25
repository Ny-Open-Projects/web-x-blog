---
title: [ZSM-211] SSR 水合时 Query 数据不一致报错怎么排查
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-211：SSR 水合时 Query 数据不一致报错怎么排查

**答**：
- 正确姿势是服务端 prefetch + `dehydrate(queryClient)` 注入 HTML，客户端 `HydrationBoundary` + 新的 queryClient 复水，客户端首屏不发重复请求
- 复水后客户端 query 的 `updatedAt` 继承服务端时间戳，staleTime 大于「服务端取数到客户端水合」的间隔时不会立刻 refetch
- 不一致的典型原因：服务端用了带时间戳的 key、客户端组件又用了不同 key；或复水前组件就手动触发了 fetch
- 排查手段：对比 `dehydrate` 输出与 devtools 中缓存条目的 key 与 data；确认没有在模块顶层创建 queryClient（每请求要新建，避免串数据）

```javascript
// server: 每请求新建 client，防串数据
const queryClient = new QueryClient()
await queryClient.prefetchQuery({ queryKey: ['home'], queryFn: fetchHome })
const dehydratedState = dehydrate(queryClient)

// client: <HydrationBoundary state={dehydratedState}> 包住应用
// client 端同一 key 的 useQuery 直接复用服务端 data，不重复请求
```
