---
title: [ZSM-079] TanStack Query 的 initialData 和 placeholderData 有什么区别？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-079：TanStack Query 的 initialData 和 placeholderData 有什么区别？
**答**：
- initialData：作为「真实的缓存初值」，带 dataUpdatedAt 时间戳，参与 staleTime 判定；适合「路由跳转时已知的列表项数据预填详情页」（PLOP 模式）。
- placeholderData：纯占位，不进缓存、没有时间戳，每次挂载都展示后立即重取；适合「切换 tab 时展示上一 tab 数据避免闪空」（keepPreviousData）。
- initialData 会阻止首次 fetch（若未 stale），placeholderData 不会。
- 风险：initialData 用错源（陈旧数据当真缓存）会让用户长时间看到旧值，配合 `initialDataUpdatedAt` 控制新鲜度。

```javascript
// PLOP：从列表缓存预填详情
const detail = useQuery({
  queryKey: ['goods', 'detail', id],
  queryFn: () => api.goods(id),
  initialData: () => qc.getQueryData(['goods'])?.find(g => g.id === id),
  initialDataUpdatedAt: /* 列表的更新时间，让 staleTime 正确计时 */,
})
// Tab 切换不闪空
useQuery({ queryKey: ['orders', tab], queryFn: ..., placeholderData: keepPreviousData })
```
