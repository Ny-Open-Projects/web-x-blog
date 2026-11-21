---
title: [ZSM-099] 笔试：手写迷你 useInfiniteQuery（pages 累积 + 游标推进）
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-099：手写迷你 useInfiniteQuery（pages 累积 + 游标推进）

**题目要求**：
- 实现 `useInfiniteQuery({ key, fn, initialPageParam, getNextPageParam })`。
- data 结构 `{ pages: [], pageParams: [] }`；fetchNextPage 用上一页响应的 getNextPageParam 结果作为下一页 pageParam；返回 undefined 停止。
- 缓存按 key；hasNextPage、isFetchingNextPage 状态正确。

```javascript
function useInfiniteQuery({ key, fn, initialPageParam, getNextPageParam }) {
  const kstr = JSON.stringify(key)
  const [state, setState] = useState(() =>
    cache.get(kstr) ?? { pages: [], pageParams: [], loading: false })

  const loadPage = async (pageParam, append) => {
    setState(s => ({ ...s, loading: true }))
    const page = await fn({ pageParam })
    cache.set(kstr, next => append
      ? { pages: [...next.pages, page], pageParams: [...next.pageParams, pageParam], loading: false }
      : { pages: [page], pageParams: [pageParam], loading: false })
    setState(cache.get(kstr))
  }

  useEffect(() => { if (!state.pages.length) loadPage(initialPageParam, false) }, [kstr])

  const last = state.pages[state.pages.length - 1]
  return {
    data: { pages: state.pages, pageParams: state.pageParams },
    hasNextPage: getNextPageParam(last, state.pages, state.pageParams) !== undefined,
    isFetchingNextPage: state.loading,
    fetchNextPage: async () => {
      const cursor = getNextPageParam(last, state.pages, state.pageParams)
      if (cursor !== undefined) await loadPage(cursor, true) // append 而非替换
    },
  }
}
```

**评分点**：
- pages/pageParams 双数组累积，fetchNextPage 是 append 不是覆盖（最常见丢分点）。
- getNextPageParam 返回 undefined 判定到底。
- pageParam 传递链：首参 initialPageParam，后续取自上一页响应。
- 缓存按 key 存完整 infinite 结构，卸载重挂不从头滚。
- 防重复触发（滚动连点）：loading 中拒绝再次 fetchNextPage（答出加分）。
