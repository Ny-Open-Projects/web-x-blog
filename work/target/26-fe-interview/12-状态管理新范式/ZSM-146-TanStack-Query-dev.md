---
title: [ZSM-146] TanStack Query Devtools 能看到什么？线上排查缓存问题时的工作流是什么？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-146：TanStack Query Devtools 能看到什么？线上排查缓存问题时的工作流是什么？
**答**：
- 能看到：每个 query 的 key、data 快照、status/fetchStatus、dataUpdateCount、 observers 数量、成功/失败时间线；可手动 invalidate/refetch/remove 单个 query。
- 排查工作流：① 用 key 面板确认「到底缓存了几个 key」（参数顺序错误会裂成两个 key）；② 看 fetchStatus 与 dataUpdateCount 判断是否真的重取了；③ observers=0 却不回收 → 查 gcTime 配置；④ 手动 remove 后重放操作复现首取路径。
- 线上方案：devtools 按环境挂载（仅 dev/staging），或用 `process.env.NODE_ENV` 控制；更重的问题用「缓存快照上报」——把 keys + dataUpdateCount 序列化进错误上报。
- 面试要点：能说出 fetchStatus（idle/fetching/paused）和 status 的区别，devtools 里两列颜色不同正是这两维。

```javascript
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router/>
      {process.env.NODE_ENV !== 'production' &&
        <ReactQueryDevtools initialIsOpen={false} buttonPosition="bottom-left"/>}
    </QueryClientProvider>
  )
}

// 缓存快照上报：线上无 devtools 时的替代
export function reportCacheSnapshot(qc) {
  const snapshot = qc.getQueryCache().getAll().map(q => ({
    key: JSON.stringify(q.queryKey), status: q.state.status,
    fetchStatus: q.state.fetchStatus, updates: q.state.dataUpdateCount,
  }))
  report(JSON.stringify(snapshot))
}
```
