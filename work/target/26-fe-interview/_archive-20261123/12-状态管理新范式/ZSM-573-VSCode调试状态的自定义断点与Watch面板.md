---
title: [ZSM-573] 用 VSCode 调试状态：条件断点、Logpoint 与 Watch 的组合用法
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-573：用 VSCode 调试状态：条件断点、Logpoint 与 Watch 的组合用法

**答**：
- 状态 bug 的断点痛点：store 的 setState 每秒几十次，普通断点根本停不到目标变更。VSCode 的**条件断点**（右键行 → Edit Condition）在 `actionName === 'checkout'` 时才停——把「业务动作名」作为断点条件是状态调试的核心技巧。
- Logpoint（不打断的日志断点）：在 setState 行设 `{actionName, changedKeys}` 表达式直接输出，不用改代码加 console.log——适合「观察一整天操作里 checkout 相关的变更流」。
- Watch 面板 + Debug Console：`useCartApi.getState()` 作为 watch 表达式，断点暂停时实时看 store 全貌；Debug Console 里可以直接调用 action 驱动状态（`__stores.cart.getState().add(...)`）——断在半路手动改状态测试下游行为。
- 断点位置选择：断在中间件层（一次断点覆盖所有 store 变更）而不是业务 action 内部；配合 ` debugger` 语句（探针条件触发时自动断，ZSM-556 的 watch onHit 机制）做到「条件命中自动停」。
- 源映射前提：调打包产物要 sourcemap（`devtool: source-map`），断点才能落到业务代码行。

```javascript
// 条件断点写法（VSCode 行内条件，右键 Edit Condition 输入）
// 条件：actionName === 'cart/addItem' && payload.id === 'g1'
export const addItem = (id) => useCart.setState((s) => ({ items: [...s.items, id] }), false, 'cart/addItem')

// 探针自动断点（代码内条件触发）
const unsub = store.watch(
  (s) => s.balance < 0,
  { debugger: true, onHit: (s) => console.log('冻结现场', s) }   // 命中即停，调用栈完整
)

// launch.json： attaching 到 dev server
// {
//   "type": "chrome", "request": "attach",
//   "port": 9222, "webRoot": "${workspaceFolder}/src",
//   "sourceMapPathOverrides": { "webpack://app/*": "${webRoot}/*" }
// }

// Watch 表达式（断点暂停时在 Watch 面板添加）
// useCartApi.getState()          → store 全貌
// useCartApi.getState().items.length → 派生指标
```
