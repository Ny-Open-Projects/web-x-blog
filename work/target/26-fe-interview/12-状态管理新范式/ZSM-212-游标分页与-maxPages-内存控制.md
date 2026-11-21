---
title: [ZSM-212] 游标分页无限滚动怎么控制缓存页数内存
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-212：游标分页无限滚动怎么控制缓存页数内存

**答**：
- `useInfiniteQuery` 用 pageParam 游标翻页，`getNextPageParam(lastPage)` 返回 undefined 表示到底
- v5 的 `maxPages` 限制缓存内保留的页数，防止长刷列表内存膨胀；翻新页时自动丢最旧页并更新 pageParams
- maxPages 裁剪后向上翻页要靠 `getPreviousPageParam` 重建游标，设计游标时要可逆或可从首项推导
- 裁剪导致 `hasNextPage` 计算可能受影响，配合 `hasPreviousPage`/双向分页时要在 API 层面同时支持双向游标

```javascript
useInfiniteQuery({
  queryKey: ['feed', tab],
  queryFn: ({ pageParam }) => fetchFeed({ cursor: pageParam, tab }),
  initialPageParam: 0,                      // v5 必填
  getNextPageParam: (last) => last.nextCursor,
  getPreviousPageParam: (first) => first.prevCursor,
  maxPages: 5,                              // 只留 5 页
})
```
