---
title: [V3-345] 编译器如何处理 v-for 中的模板 ref（收集 DOM 数组）？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-345：编译器如何处理 v-for 中的模板 ref（收集 DOM 数组）？
**答**：
- v-for 里 `:ref="setItemRef"` 传函数式 ref 是标准做法：渲染时每项调用 `setItemRef(el)`，卸载时以 null 再调用，由开发者维护数组/Map。
- 3.5 的 `useTemplateRef` 在 v-for 下配合函数 ref：可收集到 `ref([])`，顺序随渲染顺序，diff 重排后需要手动 reconcile（key → element 的 Map 更稳）。
- 编译层：函数 ref 会被 patchFlag 标记为动态 ref（`patchFlag | REF`），子节点更新时也会重新执行 ref 函数——注意函数体幂等。
- 动态组件场景：ref 在组件卸载/切换时会先后收到 null 与新实例，清理旧引用要用「先删后加」写法。
```javascript
const itemRefs = new Map()
const setItemRef = (el, id) => { el ? itemRefs.set(id, el) : itemRefs.delete(id) }
// <li v-for="i in items" :key="i.id" :ref="(el) => setItemRef(el, i.id)">
```
