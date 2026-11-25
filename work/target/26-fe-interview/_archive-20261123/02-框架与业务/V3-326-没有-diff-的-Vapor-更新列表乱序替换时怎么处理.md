---
title: [V3-326] Vapor 没有 diff，那复杂列表更新（过滤、乱序、批量）怎么处理？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-326：Vapor 没有 diff，那复杂列表更新（过滤、乱序、批量）怎么处理？
**答**：
- createFor 基于 key 映射做「集合式 reconcile」：能对上的复用块并重排，对不上的增删，本质仍是 diff 但对象是 DOM block 而非 vnode——省了 vnode 中间层。
- 批量更新在同一个 flush 周期内合并，避免逐条增删；深层 source 是响应式数组，长度/元素变化都会触发对应 reconcile。
- 过滤场景推荐 computed 派生新数组，createFor 按派生数组 reconcile，被过滤掉的项会被正确卸载。
- 乱序 + 大量替换：如果新旧集合重叠率低，直接换 key 触发整体重建有时反而更快（省去逐项重排），用 benchmark 决定。
- 与 VDOM diff 的差别总结：算法思想相同（key 复用 + 最少移动），少了 vnode 分配与比较的开销。
