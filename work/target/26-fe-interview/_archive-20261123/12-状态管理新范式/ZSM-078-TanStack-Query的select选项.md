---
title: [ZSM-078] TanStack Query 的 select 选项有什么用？结构共享（structural sharing）是什么？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-078：TanStack Query 的 select 选项有什么用？结构共享（structural sharing）是什么？
**答**：
- select：在 useQuery 里对缓存数据做派生（过滤/映射），并配 memoization——只有派生结果变化才触发组件重渲染，等价「Query 内置的 selector + 缓存」。
- 结构共享：新响应与旧响应**值相等时复用旧对象引用**（深度比较、共享未变分支），让下游 React.memo/依赖数组的比较不失效。
- 组合效果：后台刷新拿到内容相同的新 JSON → 结构共享保证 data 引用不变 → 组件不重渲染。
- 注意：select 里的对象/数组派生结果每次新引用时，Query 用「结果比较」兜底；但重计算本身每次渲染都会跑，昂贵派生放 useMemo 或 select 的稳定写法。

```javascript
const { data: cheap } = useQuery({
  queryKey: ['goods'],
  queryFn: api.goods,
  select: data => data.filter(g => g.stock > 0), // 只订阅「有货列表」
})
// 后台刷新后 stock 未变 → 结构共享 → data 引用不变 → 不渲染
```
