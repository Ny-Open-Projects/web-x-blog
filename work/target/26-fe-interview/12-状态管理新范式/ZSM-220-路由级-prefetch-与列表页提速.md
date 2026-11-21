---
title: [ZSM-220] 路由跳转前怎么 prefetch 下一页数据消除白屏
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-220：路由跳转前怎么 prefetch 下一页数据消除白屏

**答**：
- `queryClient.prefetchQuery({ queryKey, queryFn })` 在 hover/intersection 时预拉，进入路由时缓存已就绪，staleTime 内直接命中
- prefetch 与组件内 useQuery 用同一 key + 同一 queryFn（建议集中到 api 层的 queryOptions 工厂），保证缓存命中
- 列表页 hover 行卡片 → 详情页数据预取，是经典 PLP→PDP 链路优化；注意 prefetch 不能滥用（流量、后端压力），按意图分层（hover=高意图）
- prefetchQuery 失败静默不抛错，适合做「尽力而为」的优化；不要在 prefetch 里做关键路径依赖

```javascript
// api/product.ts：queryOptions 工厂，prefetch 与组件共用
export const productOptions = (id) => ({
  queryKey: ['product', id],
  queryFn: () => fetchProduct(id),
  staleTime: 60_000,
})

<Link onMouseEnter={() => queryClient.prefetchQuery(productOptions(id))}>...</Link>
// 详情页：useQuery(productOptions(id)) 直接命中缓存
```
