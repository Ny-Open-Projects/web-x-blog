---
title: [901] TanStack Query 大型应用里，QueryKey 怎么做分层设计
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 架构]
type: 面试题
---

## 901：TanStack Query 大型应用里，QueryKey 怎么做分层设计

**答**：
- 三段式 Key：[域, 实体类型, 参数]——如 ['user', 'detail', userId]、['order', 'list', filters]；域在前支持按域整体失效（invalidateQueries({ queryKey: ['order'] })），参数在后支持精确失效。
- Key 的工厂函数：不用手写数组字面量——userKeys.detail(id) / userKeys.list(filters) 集中管理，拼装错误（字符串/数字不一致）是大型应用缓存失效失效的头号 bug 源。
- 分层失效策略：改用户资料只失效 ['user', 'detail', id] 精确键；改角色权限失效整个 ['user'] 域；登出失效全部——三层失效对应三种业务事件。
- 追问钩子：为什么 QueryKey 里不能放非序列化对象（函数/Class 实例）？——Key 做 hash 依赖结构化稳定性，函数每次引用不同导致缓存永不命中。

```ts
// QueryKey 工厂：集中定义防拼装错误
export const userKeys = {
  all: ['user'] as const,
  lists: () => [...userKeys.all, 'list'] as const,
  list: (f: Filters) => [...userKeys.lists(), f] as const,
  details: () => [...userKeys.all, 'detail'] as const,
  detail: (id: string) => [...userKeys.details(), id] as const,
};
// 三层失效
qc.invalidateQueries({ queryKey: userKeys.detail(id) }); // 精确
qc.invalidateQueries({ queryKey: userKeys.all });        // 整域
qc.clear();                                              // 登出全清
```

