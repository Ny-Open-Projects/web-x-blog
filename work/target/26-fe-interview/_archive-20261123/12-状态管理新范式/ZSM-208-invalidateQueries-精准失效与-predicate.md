---
title: [ZSM-208] invalidateQueries 怎么精准失效而不是一把梭
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-208：invalidateQueries 怎么精准失效而不是一把梭

**答**：
- invalidateQueries 的第一个参数是过滤器，前缀匹配：`['orders']` 会匹配 `['orders', 1, 'detail']` 全部子树
- 加 `exact: true` 只匹配完整 key；`type: 'all' | 'active' | 'inactive'` 控制失效范围（active=当前有组件订阅）
- 复杂条件用 `predicate` 函数：可按 queryKey 内容、meta、state.error 自由过滤
- 失效 = 标记 stale + refetch active 查询；inactive 只标 stale 等下次挂载刷新，这是「低成本失效」的关键认知

```javascript
// 精准只失效当前商品详情
await queryClient.invalidateQueries({
  queryKey: ['product', id],
  exact: true,
})
// predicate：失效所有带 refresh meta 的查询
await queryClient.invalidateQueries({
  predicate: (q) => q.meta?.refreshable === true,
})
// 只失效 active 的订单列表页缓存
await queryClient.invalidateQueries({ queryKey: ['orders'], type: 'active' })
```
