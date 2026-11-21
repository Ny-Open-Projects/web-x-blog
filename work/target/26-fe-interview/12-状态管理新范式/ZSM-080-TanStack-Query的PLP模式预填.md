---
title: [ZSM-080] 列表页点进详情页「零 loading」怎么做（PLOP 模式）？数据过期怎么兜底？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-080：列表页点进详情页「零 loading」怎么做（PLOP 模式）？数据过期怎么兜底？
**答**：
- PLOP（Prefetching with Layout 渲染前的 PlaceHolder）：列表缓存里已有该项，详情查询用 initialData 函数从列表缓存取初值，首帧直出、无 loading。
- 兜底过期：initialData 会让 Query 认为数据「已存在」，用 initialDataUpdatedAt 传入列表数据的更新时间，让 staleTime 从那时起算——数据太旧则挂载即后台刷新。
- 若列表数据只有部分字段（列表瘦身版），initialData 要补默认字段或换 placeholderData（纯占位，必定重取）。
- 极致版：列表 hover/预渲染时 prefetchQuery 详情，点击即秒开。

```javascript
const listUpdatedAt = qc.getQueryState(['goods'])?.dataUpdatedAt

useQuery({
  queryKey: ['goods', 'detail', id],
  queryFn: () => api.goodsDetail(id),
  initialData: () => qc.getQueryData(['goods'])?.items?.find(g => g.id === id),
  initialDataUpdatedAt: listUpdatedAt, // 关键：新鲜度跟随列表
})
// 悬停预取
<div onMouseEnter={() => qc.prefetchQuery({ queryKey: ['goods','detail',id], queryFn: ... })}>
```
