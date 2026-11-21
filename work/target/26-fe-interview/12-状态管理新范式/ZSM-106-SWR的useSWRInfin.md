---
title: [ZSM-106] SWR 怎么做无限滚动？useSWRInfinite 的页游标机制是怎样的？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-106：SWR 怎么做无限滚动？useSWRInfinite 的页游标机制是怎样的？
**答**：
- useSWRInfinite 用「页索引 → key」的 getter 管理分页：`(index, previous) => key`，每次 setSize(index+1) 会按 getter 生成新页 key 并缓存，多页缓存互不干扰。
- `previousPageData` 用来判断终止：没有下一页游标时返回 null，SWR 就不再请求（等价于 enabled 门控）。
- 渲染时把 pages 二维数组 flat 成一维列表；`getSize() < data.length` 或拿到 `hasMore` 字段判断是否还有更多。
- 与 TanStack Query 的 useInfiniteQuery 对应：概念同构（pageParam vs index+previousPageData），面试答出一个再说另一个即可。

```javascript
import useSWRInfinite from 'swr/infinite'

function Feed() {
  const { data, size, setSize, isLoading } = useSWRInfinite(
    (index, prev) => {
      if (prev && !prev.nextCursor) return null        // 没有游标：终止
      return `/api/feed?cursor=${prev?.nextCursor ?? ''}`
    },
    fetcher
  )
  const pages = data ?? []
  const items = pages.flatMap(p => p.items)
  const hasMore = pages.length && pages[pages.length - 1].nextCursor

  return (
    <>
      <List items={items}/>
      {hasMore && <button onClick={() => setSize(size + 1)}>加载更多</button>}
      {isLoading && <Spinner/>}
    </>
  )
}
```
