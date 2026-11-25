---
title: [ZSM-635] useInfiniteQuery 的 pages 游标：双向加载与 pageParam 的内部语义
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-635：useInfiniteQuery 的 pages 游标：双向加载与 pageParam 的内部语义

**答**：
- useInfiniteQuery 的缓存形态：`pages: [page1, page2, ...]` + `pageParams: [初始param, 下一页param, ...]` 两数组平行。queryFn 收到 `pageParam`，返回值必须同时携带「数据」和「下一页游标」（`getNextPageParam` 从返回值里提取），游标逻辑是声明式的——库内部只管把「数据+游标」配对追加。
- 双向语义：`getNextPageParam(lastPage, allPages, lastParam, allParams)`（向下）与 `getPreviousPageParam`（向上，IM 聊天记录向上翻历史）。返回 `undefined` 表示没有更多页——`hasNextPage` 据此为 false，fetchNextPage 变 no-op。**游标函数只在「决定下一次的 param」时调用，不参与当前页渲染**。
- 缓存条目按「首参数」identity：切换筛选条件换 queryKey，pages 重置——infinite query 的 key 也要包含筛选参数。
- 刷新语义：stale 后 invalidate 会 refetch **所有已加载页**（每页一次请求，用各页的 pageParams 重放）；`maxPages` 选项限制缓存页数（内存控制，超出从头部淘汰）。
- 追问钩子：`select` 对 infinite 数据的扁平化（`pages.flatMap(p => p.items)`）要 memo——select 默认每次渲染都执行。

```javascript
const { data, fetchNextPage, fetchPreviousPage, hasNextPage, hasPreviousPage } = useInfiniteQuery({
  queryKey: ['messages', chatId],
  queryFn: ({ pageParam }) => api.getMessages({ chatId, cursor: pageParam }),
  initialPageParam: null,                            // v5 必填
  getNextPageParam: (lastPage, allPages, lastParam) =>
    lastPage.nextCursor ?? undefined,                // undefined = 没有下一页
  getPreviousPageParam: (firstPage) => firstPage.prevCursor ?? undefined,   // 向上翻历史
  maxPages: 20,                                      // 缓存上限，头尾淘汰
  select: (data) => data.pages.flatMap((p) => p.items),   // 扁平化（记得 memo 化用 useMemo 包）
})

// 渲染：双向触发
<div onScrollTop={() => fetchPreviousPage()} onScrollBottom={() => fetchNextPage()} />

// 内部追加逻辑（简化）
function fetchNextPageInternal() {
  const nextParam = getNextPageParam(pages.at(-1), pages, pageParams.at(-1), pageParams)
  if (nextParam === undefined) return promise.resolve()   // 没有更多：no-op
  const result = await queryFn({ pageParam: nextParam })
  // pages 与 pageParams 平行追加，缓存原子更新
  setData({ pages: [...pages, result], pageParams: [...pageParams, nextParam] })
}

// invalidate 重放：按已存 pageParams 逐页重拉（保留加载位置）
// queryClient.invalidateQueries({ queryKey: ['messages', chatId] })
```
