---
title: [ZSM-640] select 选项：把服务端缓存切成组件最小消费切片
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-640：select 选项：把服务端缓存切成组件最小消费切片

**答**：
- select 是 useQuery 的「读时转换」：`useQuery({ queryKey, queryFn, select: (data) => data.items.find(i => i.id === target) })`——组件只订阅 select 的结果，缓存里其他字段的变更不触发该组件重渲（前提 select 结果引用稳定或结构共享）。这是 TanStack Query 里对标 Zustand selector 的粒度控制手段。
- 引用稳定性：select 每次渲染都执行，返回新对象（filter/map）会破坏比较——两个手段：1) select 内部做 memo（TanStack 源码对 select 有 `memoOptions` 优化，稳定引用会缓存）；2) `structuralSharing` 机制对 select 结果同样生效（深比较复用旧引用）。保险写法：返回标量或 select 里自己 useMemo 化输入。
- select 与 observer 的关系：select 在 observer 层执行（不在 Query 层）——同一 Query 不同组件可以用不同 select，各自独立切片、独立更新粒度。
- 与结构性 anti-pattern 的对抗：不写 select 的 useQuery 返回整 data 是最常见的新手错误——「一个页面 20 个 useQuery 每个都订阅整个响应」导致数据任何字段变化全员重渲。
- 追问钩子：select 抛异常（如 data 结构不符）会怎样——observer 错误传播到 error boundary；select 里做防御性兜底而不是抛。

```javascript
// 同一 Query 三个组件、三种切片
const todoQuery = useQuery({ queryKey: ['todos'], queryFn: fetchTodos })

// 组件 A：只关心总数（标量：引用天然稳定）
const total = useQuery({ queryKey: ['todos'], queryFn: fetchTodos, select: (d) => d.length })

// 组件 B：只关心某一条（对象：依赖结构共享保引用）
const todo = useQuery({
  queryKey: ['todos'], queryFn: fetchTodos,
  select: (d) => d.items.find((i) => i.id === id),
})

// 组件 C：派生统计（引用不稳定 → memo 化）
const stats = useQuery({
  queryKey: ['todos'], queryFn: fetchTodos,
  select: (d) => ({
    done: d.items.filter((i) => i.done).length,
    overdue: d.items.filter((i) => i.overdue).length,
  }),
})
// select 每次执行会产新对象 → 依赖 TanStack 的 memoOptions 缓存：
// 输入 data 引用不变时 select 结果复用

// 复杂转换放 queryFn 之后的独立层（大转换别塞 select）
function useTodoTable(filters) {
  return useQuery({
    queryKey: ['todos', 'table', filters],
    queryFn: async () => {
      const raw = await fetchTodos()
      return shapeForTable(raw, filters)   // 复杂 shape 在数据层，缓存的就是成品
    },
  })
}
```
