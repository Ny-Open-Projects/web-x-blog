---
title: [907] TanStack Query 时代还需要 Redux/Zustand 吗？边界怎么划
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 架构]
type: 面试题
---

## 907：TanStack Query 时代还需要 Redux/Zustand 吗？边界怎么划

**答**：
- 边界一句话：服务端状态（数据缓存）归 Query，客户端状态（UI 交互/主题/草稿）归轻量库——混放的典型事故：把服务端数据抄进 Redux（双源不一致），或把 UI 状态塞进 Query 缓存（被 gc 清掉 UI 崩）。
- 判断标准三问：数据的真相在服务端吗（是 -> Query）、多个无关联组件要改它吗（是 -> 全局库）、需要跨页面持久吗（UI 持久 -> 库 + storage）。
- 衔接模式：全局库存「选择状态」（当前选中 id），Query 存「数据」——useQuery 用全局 id 作参数，选中态与数据解耦不重复。
- 迁移策略：存量 Redux 不推倒——新功能全用 Query，旧 Redux 域逐个迁（数据类先迁，UI 类后迁或保留），防腐层过渡。

```ts
// 边界示例：选中态在 Zustand，数据在 Query
const selectedId = useUiStore(s => s.selectedUserId);
const { data: user } = useQuery({
  queryKey: userKeys.detail(selectedId),        // id 联动，数据不复制
  queryFn: () => fetchUser(selectedId),
  enabled: !!selectedId,
});
```

