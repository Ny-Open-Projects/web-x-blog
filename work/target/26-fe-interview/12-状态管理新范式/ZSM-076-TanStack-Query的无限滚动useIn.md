---
title: [ZSM-076] TanStack Query 的 useInfiniteQuery 怎么用？pageParam、hasNextPage 和反向分页怎么处理？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-076：TanStack Query 的 useInfiniteQuery 怎么用？pageParam、hasNextPage 和反向分页怎么处理？
**答**：
- queryFn 收 `({ pageParam })`：第一页 pageParam = initialPageParam，后续由 getNextPageParam 返回值决定；返回 undefined 表示没有更多页。
- 返回结构 data.pages（每页数组）+ data.pageParams；渲染要 flatMap 合并，或 getNextPageParam 里做去重（游标重复时防重复加载）。
- 反向分页（聊天记录从最新往上翻）：getPreviousPageParam + fetchPreviousPage；游标型（按 message id）比页码型更适合 IM。
- 配 IntersectionObserver 触发 fetchNextPage；注意 staleTime 设大些，避免滚动中 refetch 闪烁。

```javascript
const { data, fetchNextPage, hasNextPage } = useInfiniteQuery({
  queryKey: ['chat', roomId],
  queryFn: ({ pageParam }) => api.messages(roomId, { before: pageParam }),
  initialPageParam: undefined,
  getNextPageParam: last => last.nextCursor ?? undefined, // undefined = 到底
})
const messages = data.pages.flatMap(p => p.items)
// 触底：if (inView && hasNextPage && !isFetchingNextPage) fetchNextPage()
```
