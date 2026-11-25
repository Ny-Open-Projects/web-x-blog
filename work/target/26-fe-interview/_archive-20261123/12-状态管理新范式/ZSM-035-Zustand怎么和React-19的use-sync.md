---
title: [ZSM-035] Zustand 在 React 19（use API、compiler）下有什么新玩法或注意点？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-035：Zustand 在 React 19（use API、compiler）下有什么新玩法或注意点？
**答**：
- React 19 的 `use()` 可以在条件分支/循环里读 Context 和 Promise，但 Zustand 的 hook 仍需在顶层调用（它是 useSyncExternalStore，不是可暂停资源）。
- React Compiler 自动 memo 组件与表达式，能缓解「大对象 selector」的重渲染，但不能替代 selector 拆分——订阅粒度在 store 层，compiler 管不到订阅本身。
- form action / optimistic hook 与 Zustand 正交：乐观 UI 用 useOptimistic，持久化结果仍可写回 store。
- 迁移注意：Server Components 下不能创建订阅，store 创建与消费都要在 'use client' 边界内。

```javascript
'use client'
// RSC 边界内才能用 store
function Cart() {
  // React 19 compiler 会自动 memo，但订阅粒度仍由 selector 决定
  const count = useCart(s => s.items.length)
  return <b>{count}</b>
}
```
