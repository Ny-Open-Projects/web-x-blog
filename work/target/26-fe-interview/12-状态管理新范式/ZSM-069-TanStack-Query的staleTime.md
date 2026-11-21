---
title: [ZSM-069] TanStack Query 的 staleTime 和 gcTime 有什么区别？各管什么？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-069：TanStack Query 的 staleTime 和 gcTime 有什么区别？各管什么？
**答**：
- staleTime（新鲜期）：数据在多久内算「新鲜」，新鲜期内**不会因挂载/聚焦/重连而重取**，直接用缓存；默认 0（立即 stale）。
- gcTime（缓存存活期）：**没有订阅者**后缓存保留多久再被垃圾回收；默认 5 分钟。期间重新挂载会先展示旧数据（视 staleTime 再决定是否重取）。
- 一个管「要不要重新请求」，一个管「缓存还活着吗」；两者独立计时，gcTime >= staleTime 才有意义（默认就满足）。
- 配置示例：高频变动的行情 staleTime 0 + refetchInterval；基本不变的配置 staleTime Infinity；偶尔回访的列表 staleTime 30s、gcTime 10min。

```javascript
useQuery({
  queryKey: ['goods', id],
  queryFn: () => api.goods(id),
  staleTime: 30_000,   // 30 秒内挂载/聚焦不重取
  gcTime: 10 * 60_000, // 无订阅后缓存再活 10 分钟
  refetchInterval: query => (data.hot ? 5000 : false), // 条件轮询
})
// gcTime: Infinity → 缓存永不回收（配合 persistQueryClient 做离线）
```
