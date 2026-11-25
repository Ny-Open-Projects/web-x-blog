---
title: [ZSM-627] QueryObserver 的 shouldFetch 决策：refetch 什么时候真的发生
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-627：QueryObserver 的 shouldFetch 决策：refetch 什么时候真的发生

**答**：
- Observer 的核心职责是「把 Query 的状态翻译成组件需要的最小切片 + 决定要不要 fetch」。每次挂载/依赖变化都会跑 `shouldFetchOnMount/updateResult` 决策：当前缓存是否有效（staleTime 内 fresh）、有没有在途请求、enabled 开关、stale 与 invalid 状态组合。
- 决策要点：1) **fresh**（staleTime 未过期且非 invalidated）→ 挂载不请求，直接用缓存；2) **stale** → 后台 refetch（data 先给旧值，fetchStatus 变 fetching）；3) **invalidated**（invalidateQueries 打标）→ 必定 refetch；4) **refetchOnWindowFocus/Reconnect** → 仅 stale 时触发；5) 同一 Query 已有在途 fetch → 复用该请求（observer 只加引用，不重复发请求）——这就是多组件同 key 不重复请求的机制。
- `enabled: false` 时 observer 不参与 fetch 决策，只镜像状态；`refetchOnMount: false` 则挂载时只在「无数据」时请求。
- placeholderData/isPlaceholderData：让 observer 在「真数据未到」时给占位（如切换分页用上一页数据），不写入 Query 状态——纯 observer 层的展示技巧。
- 追问钩子：`useQuery` 的第三个返回 `isFetching` 来自 fetchStatus，而 `isLoading = isPending && isFetching`——理解状态正交才能正确写 loading 逻辑。

```javascript
// Observer 决策骨架（v5 简化）
class QueryObserver {
  onQueryUpdate() {
    if (this.shouldFetchOnMountOrChange()) {
      this.client.getQueryCache().build(this.options).fetch({
        // 已有在途 fetch 会复用：fetchOptions cancellation
      })
    }
    this.notify()   // 只在选出的 slice 变化时通知组件
  }

  shouldFetchOnMountOrChange() {
    const q = this.currentQuery
    const opts = this.options
    if (opts.enabled === false) return false
    const isStale = q.isStaleByTime(opts.staleTime)   // dataUpdatedAt + staleTime
    const invalidated = q.state.isInvalidated
    const noData = q.state.data === undefined
    const refetchOnMount = opts.refetchOnMount ?? true

    if (invalidated) return true                      // 打标失效：必拉
    if (noData) return true                           // 无数据：必拉
    if (isStale && refetchOnMount) return true        // 过期且允许挂载拉：后台拉
    return false                                      // fresh：不拉
  }

  // staleTime 语义：0（默认）= 挂载即拉；Infinity = 永不自动拉
  isStaleByTime(staleTime) {
    return this.state.data === undefined ||
      (staleTime !== Infinity && Date.now() - this.state.dataUpdatedAt > (staleTime ?? 0))
  }
}
```
