---
title: [ZSM-092] refetchOnWindowFocus / refetchOnReconnect / refetchOnMount 三个开关的行为与组合策略
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-092：refetchOnWindowFocus / refetchOnReconnect / refetchOnMount 三个开关的行为与组合策略
**答**：
- 三者都是「stale 时才重取」的门控：mount（组件挂载）、windowFocus（标签页聚焦）、reconnect（断网恢复）。数据新鲜（staleTime 内）时都不触发。
- 默认全 true：适合通用后台数据——回到页面/恢复网络都自动对齐服务端。
- 组合策略：实时性敏感（库存、行情）全 true + refetchInterval；编辑中的表单数据 focus 改 false（防打字中闪变）；依赖 SW 离线缓存的 offlineFirst 场景 reconnect 保留。
- 全局设默认、单查询覆写：`defaultOptions.queries.refetchOnWindowFocus` 级别要按业务定，不要一刀切。

```javascript
new QueryClient({ defaultOptions: { queries: {
  refetchOnWindowFocus: true,
  refetchOnReconnect: true,
  refetchOnMount: true,
  staleTime: 30_000, // 新鲜期内三者全部静默
}}})
// 单查询覆写：编辑器草稿不因聚焦刷新
useQuery({ queryKey: ['draft', id], queryFn: ..., refetchOnWindowFocus: false })
```
