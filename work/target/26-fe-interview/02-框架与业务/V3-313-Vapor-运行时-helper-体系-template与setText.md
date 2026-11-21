---
title: [V3-313] Vapor 模式的运行时 helper 体系（template / setText / insert）是怎样协作的？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-313：Vapor 模式的运行时 helper 体系（template / setText / insert）是怎样协作的？
**答**：
- Vapor 编译产物不经过 VDOM：编译期把模板拆成静态片段 + 动态点，运行时用 helper 直接操作 DOM。
- `template()`：用 `<template>` 元素 cloneNode 复制静态结构，克隆比逐个 createElement 快且省内存。
- `setText(el, () => expr)` / `insert(el, () => expr)`：为每个动态点绑定一个轻量 effect，表达式依赖变化时直接改 DOM 属性/内容，不走 patch。
- 组件 setup 返回的不是 vnode 而是 DOM 节点 + 清理函数，挂载就是 `parent.appendChild`。
- 收益：省去 createVnode/diff 两层；代价：动态点粒度固定在编译期，运行时灵活性换成了性能。
```javascript
// Vapor 编译产物示意
const t0 = _template('<div><span> </span></div>')
export function App() {
  const count = ref(0)
  const el = t0()
  const [n0] = _setText(el.firstChild, () => count.value) // 动态点直接绑定
  return el
}
```
