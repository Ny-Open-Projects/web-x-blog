---
title: [ZSM-089] TanStack Query 刷新后 data 引用会变吗？结构共享的局限（新数组、深层对象）在哪？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-089：TanStack Query 刷新后 data 引用会变吗？结构共享的局限（新数组、深层对象）在哪？
**答**：
- 内容未变：结构共享让 data 保持旧引用，组件不重渲染——这是「后台刷新不闪动」的机制基础。
- 局限一：服务端每次返回新构建的 JSON 但内容相同时，Query 逐层比较后仍能复用（这正是不变引用的来源），但比较本身是深度递归，超大响应有 CPU 成本（可关 structuralSharing）。
- 局限二：结构共享只对「缓存数据本体」生效；select 派生的新对象（filter/map 结果）每次渲染是新引用，要靠 select 的结果比较或外部 useMemo。
- 局限三：值相同但类型/键序变化（如新增可选字段）算「变了」，引用更新并触发渲染——这是正确行为。

```javascript
// select 派生的引用问题与解法
const { data } = useQuery({
  queryKey: ['goods'], queryFn: api.goods,
  select: d => d.filter(x => x.on), // 内容不变时 Query 结果比较兜底不触发
})
// 更稳：派生结果抽组件 + React.memo，或 select 只挑原始值
```
