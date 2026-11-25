---
title: [FRP-216] Block Tree 与 diff 的配合：动态节点集合怎么用？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-216：Block Tree 与 diff 的配合？
**答**：
- Block：openBlock() 创建动态节点收集容器，render 期间所有带 patchFlag 的 vnode 按序压入 dynamicChildren。
- 更新时：不遍历整棵树，只遍历 dynamicChildren 数组按 flag 精准 patch——diff 被替换为「定点更新」。
- 边界：v-if/v-for 创建新 block（结构变化时集合重算）；slot 内容跨 block 需特殊处理。
- 与传统 diff 关系：动态结构（列表增删）仍走 diff；静态结构更新完全绕过 diff。
- 效果：大型表单页更新单个字段，从 O(全树) 降为 O(动态点数)。
