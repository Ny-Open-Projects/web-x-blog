---
title: [MFW-216] TanStack Start 的同构数据层（loader 与 Query 的统一）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-216：TanStack Start 同构数据层

**答**:
- 核心设计：Router loader 内部用 queryClient.ensureQueryData（SSR 预取进 Query 缓存）→ 客户端组件 useQuery 直接命中（脱水复水同一缓存）——「一套数据 API 走完 SSR 与 CSR」
- 与 Next 的对比：Next 是 RSC fetch 体系（cache/revalidate 语义），客户端用 Query 是「两套体系桥接」（MFW-192 的脱水桥）；Start 是原生单一体系（无桥接成本）
- 失效统一：mutation 成功 → queryClient.invalidateQueries → 客户端缓存失效 + 下次导航 loader 重拉——失效语义只有一套
- 心智简化：学一套（Query），服务端客户端通吃——这是 Start 对「元框架复杂度」的直接回应

```javascript
// route.tsx（SSR 与客户端同一数据源）
export const Route = createFileRoute('/posts/$id')({
  loader: ({ params }) =>
    queryClient.ensureQueryData(postOptions(parseInt(params.id))),   // SSR 预取
  component: PostView,
})
function PostView() {
  const { data } = useQuery(postOptions(id))       // 直接命中 SSR 预取的缓存
}
```
