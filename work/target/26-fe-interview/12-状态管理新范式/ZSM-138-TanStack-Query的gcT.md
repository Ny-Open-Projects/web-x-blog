---
title: [ZSM-138] TanStack Query 的 gcTime 是怎么回收缓存的？ inactive observer 是什么概念？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-138：TanStack Query 的 gcTime 是怎么回收缓存的？ inactive observer 是什么概念？
**答**：
- observer 模型：每个 useQuery 是一个 observer，有组件订阅 = active；组件全部卸载后该 query 变 inactive，此时启动 gcTime（默认 5 分钟）倒计时。
- gcTime 倒计时结束才真正删除缓存条目；期间组件重新挂载会立即复用缓存并继续，倒计时取消——所以「返回列表页」通常不闪 loading。
- 和 staleTime 无关：staleTime 决定「数据新不新鲜」（是否需要重取），gcTime 决定「内存里还留不留」（要不要删），两者正交（070 已考语义区分，这里考回收机制）。
- 实战影响：gcTime: Infinity 可做「本会话永久缓存」；大对象查询要主动调小 gcTime；SSR dehydrate 前提是数据还在 gcTime 内。

```javascript
function GoodsDetail({ id }) {
  const { data } = useQuery({
    queryKey: ['goods', id],
    queryFn: () => api.goods(id),
    gcTime: 5 * 60_000,      // 默认：无 observer 5 分钟后删除
    staleTime: 60_000,       // 1 分钟内视为新鲜，不重取
  })
  return <Detail data={data}/>
}

// 会话级常驻：用户资料全程保留
const meQuery = { queryKey: ['me'], queryFn: api.me,
                  gcTime: Infinity, staleTime: 60_000 }
```
