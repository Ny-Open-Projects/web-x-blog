---
title: [V3-335] 静态提升与 cacheHandlers 的收益怎么实测？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-335：静态提升与 cacheHandlers 的收益怎么实测？
**答**：
- 静态提升：纯静态节点提升到 render 函数外（`const _hoisted_1 = createVnode(...)`），重渲染时跳过 vnode 创建与 diff 比较；连续静态节点超过阈值还会合并成静态 vnode 整体提升。
- cacheHandlers：`@click` 内联函数放进 `_cache` 数组，首次创建后复用，子组件 memo 比较时函数引用稳定，避免子树无效重渲染。
- 实测方法一：diff 产物——开/关 cacheHandlers 看 render 代码里 `_cache[0] || (...)` 是否出现。
- 实测方法二：性能面板渲染同一大列表组件 1000 次重渲染，对比脚本耗时（patch 阶段）。
- 边界：提升的 vnode 是共享引用，里面不能含动态内容；缓存的事件闭包里若依赖会变化的外部变量，编译器会改用内联 props 传递（`withMemo`）兜底。
```javascript
const _hoisted_1 = /* hoisted */ createElementVNode('span', null, '静态文本', -1 /* HOISTED */)
```
