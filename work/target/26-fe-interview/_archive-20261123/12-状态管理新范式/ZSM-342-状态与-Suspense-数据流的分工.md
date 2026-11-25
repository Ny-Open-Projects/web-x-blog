---
title: [ZSM-342] Suspense 数据流与传统 store 数据流怎么分工不打架
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-342：Suspense 数据流与传统 store 数据流怎么分工不打架

**答**:
- 分工原则：路由/页面级「进入前的关键数据」走 Suspense（promise 抛出、loader 缓存），交互产生的「过程态数据」走 store/Query——两套数据流按「生命周期归属」切分
- Suspense 的缓存语义：promise 必须有外部缓存（不随组件卸载丢弃），这正是 Query/Jotai 异步 atom 的价值——裸传 promise 给 use() 会请求风暴
- 协同模式：Suspense 负责「有没有」，store 负责「变化」——Suspense 加载完成后数据落入 Query 缓存，后续更新走 invalidate（不再 throw）
- 避免混战：同一数据只选一条主数据流，另一条只读派生；双流写入同一份数据必出竞态

```javascript
// Suspense：首屏关键数据（loader 层缓存 promise）
const resource = queryOptions({ queryKey: ['home'], queryFn: fetchHome })   // 缓存 promise
const data = useSuspenseQuery(resource)     // throw promise → Suspense
// 后续更新走缓存失效，不再进入 throw 路径
queryClient.invalidateQueries({ queryKey: ['home'] })
```
