---
title: [ZSM-204] 组件卸载后缓存多久被 GC，gcTime 的边界在哪
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-204：组件卸载后缓存多久被 GC，gcTime 的边界在哪

**答**：
- 缓存条目没有观察者（订阅组件）时才启动 gcTime 倒计时（默认 5 分钟）；有组件在用就永不过期，只受 staleTime 控制「新鲜度」
- staleTime 管「数据多久内不重新请求」，gcTime 管「没人用了多久后从内存删除」，两个时钟互相独立
- gcTime 归零后条目删除，下次挂载重新请求，之前的 data/error 都没了；想跨页面保留就提升 gcTime 或用 persister 落盘
- 边界：SSR 下 `dehydrate` 会把 gcTime 重置；`refetchOnMount` 默认 true，过期但未删除的缓存挂载时会后台刷新

```javascript
const queryClient = new QueryClient({
  defaultOptions: { queries: { gcTime: 1000 * 60 * 30 } }  // 全局 30 分钟
})

// 列表页跳详情再返回：只要 30 分钟内回来，数据还在且立即显示
useQuery({ queryKey: ['list'], queryFn: fetchList, gcTime: Infinity })  // 永不 GC（慎用，内存泄漏面）
// 动态 key 的搜索页：key 换一个旧条目就开始倒计时，堆内存可控
useQuery({ queryKey: ['search', kw], queryFn: search, gcTime: 30_000 }) // 30 秒即可
```
