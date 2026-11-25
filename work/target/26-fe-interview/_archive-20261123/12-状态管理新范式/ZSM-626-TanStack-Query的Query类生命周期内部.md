---
title: [ZSM-626] TanStack Query 的 Query 实例生命周期：从创建到 GC 的内部状态
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-626：TanStack Query 的 Query 实例生命周期：从创建到 GC 的内部状态

**答**：
- 核心三层结构：`QueryClient` 持有 `QueryCache`（defaultQueryCache）与 `MutationCache`；`QueryCache` 按 **queryKey hash** 存 `Query` 实例；每个 Query 实例被多个 `QueryObserver`（组件层的 useQuery 就是创建 observer）订阅。**Query 存数据，Observer 存订阅**——同一 key 的多个组件共享一个 Query。
- Query 内部状态：`state = { status: 'pending'|'success'|'error', data, dataUpdatedAt, error, fetchStatus: 'idle'|'fetching' }`。status 与 fetchStatus 分离是关键——`isFetching` 反映网络活动，`isPending` 反映有无数据，两者正交（后台刷新时 success + fetching）。
- 生命周期：首次 useQuery → getOrCreateQuery → mount observer → fetch（retryer 包裹）→ 成功写 state → notify observers → 无 observer 挂载且超过 gcTime → QueryCache remove（GC，内存释放）。
- GC 细节：`gcTime` 计时从「最后一个 observer unmount」开始；计时期间若组件重新挂载，取消 GC 直接复用缓存数据；unmount 后 data 仍可被「预取/invalidate」路径读取。
- 追问钩子：queryKey 变化不会更新 Query，而是**创建新 Query 实例**——所以「依赖数组的每个值组合」都有独立缓存条目，key 空间爆炸是内存问题来源。

```javascript
// Query 生命周期骨架（v5 源码简化）
class Query {
  constructor(client, options, state) {
    this.state = state ?? {
      status: 'pending', fetchStatus: 'idle',
      data: undefined, dataUpdatedAt: 0, error: null,
    }
    this.options = options
    this.gcTimeout = -1
  }

  setData(data, options) {
    // structuralSharing：与旧数据结构共享减少引用变化
    const prev = this.state.data
    const next = options.structuralSharing !== false
      ? replaceEqualDeep(prev, data) : data
    this.state = {
      ...this.state,
      data: next, dataUpdatedAt: Date.now(),
      status: 'success', fetchStatus: 'idle', error: null,
    }
    this.observers.forEach((o) => o.onQueryUpdate())   // 通知全部 observer
  }

  scheduleGC() {
    // 最后一个 observer unmount 时启动 gcTime 倒计时
    clearTimeout(this.gcTimeout)
    this.gcTimeout = setTimeout(() => {
      this.cache.remove(this)   // gcTime 后从缓存移除
    }, this.options.gcTime)
  }

  cancelGC() { clearTimeout(this.gcTimeout) }   // observer 重新挂载取消 GC
}
```
