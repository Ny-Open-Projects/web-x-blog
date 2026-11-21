---
title: [ZSM-144] useInfiniteQuery 怎么限制缓存页数？maxPages 和双向滚动（前翻页）怎么实现？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-144：useInfiniteQuery 怎么限制缓存页数？maxPages 和双向滚动（前翻页）怎么实现？
**答**：
- `maxPages: n` 让缓存最多保留 n 页，超出时从头丢弃旧页——无限滚动会话内存可控，游标链也要按剩余首页重新推导。
- 双向滚动（聊天记录向上下都能翻）：pageParam 支持两个方向游标（before/after），getKey 按 direction 参数生成；数据页要用 `pages.flat()` 时注意方向页的排序合并。
- hasPreviousPage/hasNextPage 配合 fetchPreviousPage/fetchNextPage 分别驱动两个方向的加载器；方向错乱的表现是「历史消息倒序插入」，要在 select 里统一排序。
- 追问钩子：maxPages 截断后 fetchPreviousPage 需要首页游标，v5 会基于保留页自动续链，这正是 maxPages 能双向工作的前提。

```javascript
const { data, fetchNextPage, fetchPreviousPage,
        hasNextPage, hasPreviousPage } = useInfiniteQuery({
  queryKey: ['messages', roomId],
  queryFn: ({ pageParam }) =>
    api.messages({ roomId, ...pageParam }),        // { before } | { after }
  initialPageParam: { after: 0 },
  maxPages: 10,                                    // 最多缓存 10 页
  getPreviousPageParam: (first) =>
    first.hasBefore ? { before: first.oldestId } : undefined,
  getNextPageParam: (last) =>
    last.hasMore ? { after: last.newestId } : undefined,
})

const messages = useMemo(() =>
  (data?.pages ?? []).flatMap(p => p.items)
    .sort((a, b) => a.ts - b.ts), [data])          // 双方向统一按时间排序
```
