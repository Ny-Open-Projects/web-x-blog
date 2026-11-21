---
title: [V3-316] Vapor 的 createIf 条件渲染是怎么编译和运行的？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-316：Vapor 的 createIf 条件渲染是怎么编译和运行的？
**答**：
- `v-if/v-else` 编译成 `createIf(() => cond.value, () => branchA, () => branchB)`：条件 effect 决定渲染哪个分支函数。
- 分支函数内部各自创建独立 block（含自己的动态点 effect），切换分支时旧 block 整体 unmount（停止其作用域），新 block mount。
- 与 VDOM 差异：不存在 vnode 树比对，分支就是函数，成本 = 分支的创建/销毁成本；所以「条件频繁切换 + 分支很重」时要自己加缓存层。
- 条件本身是响应式表达式：cond 变化 → effect 重跑 → 比较当前分支标记，相同分支不重建。
- v-show 在 Vapor 下照旧编译为 style.display 切换，保留 DOM，性能特点与 VDOM 模式一致。
```javascript
createIf(
  () => show.value,
  () => { const el = tA(); /* 动态点 */ return el },
  () => tB()
)
```
