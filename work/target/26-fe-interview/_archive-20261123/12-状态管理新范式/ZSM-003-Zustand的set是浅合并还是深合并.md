---
title: [ZSM-003] Zustand 的 set 是浅合并还是深合并？嵌套 state 该怎么更新？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-003：Zustand 的 set 是浅合并还是深合并？嵌套 state 该怎么更新？
**答**：
- 默认是**一层浅合并**：`set({ a: 1 })` 只替换顶层 key，等价于 `{...state, a: 1}`，不会递归合并嵌套对象。
- 嵌套结构必须自己展开：`set(s => ({ user: { ...s.user, name: 'x' } }))`，漏一层展开就会丢字段。
- 传 `replace: true`（第二参）则不做合并，直接整体替换，常用于 hydrate 或重置整个 store。
- set 内传函数形式 `set(s => next)` 可以拿到最新 state，避免闭包读到旧值；同步多次 set 会自动批量触发一次渲染（React 18 自动批处理）。
- 追问钩子：可以写一层 immer 中间件把深更新写法变 `state.user.name = 'x'`。

```javascript
const useStore = create(set => ({
  user: { name: 'a', address: { city: 'bj' } },
  list: [],
  // 浅合并：list 被替换，user 完全不受影响
  resetList: () => set({ list: [] }),
  // 嵌套更新：必须逐层展开，否则 address 会丢
  setCity: city => set(s => ({
    user: { ...s.user, address: { ...s.user.address, city } },
  })),
  // 整体替换：用于 SSR 数据落地或重置
  hydrate: data => set(data, true),
}))
```
