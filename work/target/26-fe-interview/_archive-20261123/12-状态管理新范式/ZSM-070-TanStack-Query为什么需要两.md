---
title: [ZSM-070] 为什么 TanStack Query 需要两个时间参数？只用 gcTime 或只用 staleTime 会出什么问题？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-070：为什么 TanStack Query 需要两个时间参数？只用 gcTime 或只用 staleTime 会出什么问题？
**答**：
- 两个时钟回答两个不同问题：staleTime 管「数据新鲜度→是否发起网络请求」，gcTime 管「内存/缓存占用→无订阅数据何时删除」。
- 只有 staleTime、没有 gcTime：用户离开列表页后缓存立刻删除，回来即使数据新鲜也要重新请求——浪费带宽、闪 loading。
- 只有 gcTime、没有 staleTime（默认 staleTime 0）：数据「永久保留但永远不新鲜」，每次挂载/聚焦都重取，缓存退化为「加载期占位图」，失去 stale-while-revalidate 的顺滑。
- 组合出行为：staleTime 5min + gcTime 30min = 5 分钟内回访零请求，5~30 分钟回访先显旧数据后台刷新，30 分钟后缓存重建。
- 这套机制等价于 HTTP 缓存的 max-age（新鲜期）+ 保留策略（不驱逐），Query 把它搬到了 JS 内存层。

```javascript
// 时序演示
useQuery({ queryKey: ['feed'], queryFn: getFeed, staleTime: 5 * 60_000, gcTime: 30 * 60_000 })
// t=0 挂载：请求
// t=3min 卸载：缓存仍在（gcTime 未到）
// t=4min 重新挂载：命中缓存且新鲜 → 零请求零 loading
// t=10min 重新挂载：缓存仍在但已 stale → 先渲染旧数据 + 后台刷新
// t=40min 重新挂载：缓存已回收 → 重新请求，loading 出现
```
