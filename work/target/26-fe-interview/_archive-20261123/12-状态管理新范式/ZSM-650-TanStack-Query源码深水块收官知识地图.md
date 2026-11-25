---
title: [ZSM-650] TanStack Query 内部机制深水收官：三层结构的完整心智模型
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-650：TanStack Query 内部机制深水收官：三层结构的完整心智模型

**答**：
- 完整心智模型（可默画的架构图）：**QueryClient**（配置聚合根 + defaultOptions 三层合并）→ **QueryCache / MutationCache**（hashKey 寻址的条目存储 + 事件总线）→ **Query / Mutation**（状态机 + retryer 引擎 + AbortSignal）→ **QueryObserver**（决策层：shouldFetch、select 切片、结果比较闸门、通知）→ hook 层（useQuery/useSuspenseQuery/useInfiniteQuery/useMutation）。
- 关键决策点的数据流：挂载 → observer.shouldFetch（staleTime/invalidated/enabled）→ query.fetch（去重 or cancelRefetch）→ retryer（retry/backoff/networkMode pause）→ setData（structuralSharing）→ observer.updateResult（select + 比较）→ React setState（只通知结果变化的组件）。
- 周边子系统：focusManager/onlineManager（环境事件源）、invalidate 的前缀匹配传播、dehydrate/hydrate（SSR）、persistQueryClient（持久化）、WS 桥（推拉结合）。
- 排障速查：重复请求 → 去重/key 稳定性；不请求 → staleTime/enabled/invalidated 判定；旧数据闪烁 → placeholderData；内存增长 → gcTime/key 空间爆炸；竞态 → signal 接线；渲染风暴 → select 粒度 + 扇出诊断。
- 面试答题框架：先讲三层职责分离，再讲一条数据流的完整路径，最后按排障速查给 2 个实战例子——比背 API 高两个层级。

```javascript
// 心智模型速写（伪码架构图）
const architecture = {
  QueryClient: { config: 'defaultOptions 三层合并', caches: ['QueryCache', 'MutationCache'], control: 'cancel/invalidate/refetch/resume' },
  QueryCache: { addressing: 'hashKey（对象键序无关）', events: 'subscribe（devtools/invalidate 用）' },
  Query: {
    state: 'status × fetchStatus 正交',
    engine: 'retryer（retry/退避/AbortSignal/networkMode pause）',
    write: 'setData + structuralSharing',
  },
  QueryObserver: {
    decide: 'shouldFetch（staleTime/invalidated/enabled/refetchOn*）',
    slice: 'select（读时转换，observer 层）',
    gate: '结果比较 → 才通知 React',
  },
  hooks: { useQuery: '常规', useSuspenseQuery: '抛 promise', useInfiniteQuery: 'pages+pageParams', useMutation: '独立实例+scope 串行' },
}
console.log(architecture)   // 每项在前面的卡都有独立展开
```
