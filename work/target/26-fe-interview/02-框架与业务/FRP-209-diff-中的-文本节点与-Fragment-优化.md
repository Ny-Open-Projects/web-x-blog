---
title: [FRP-209] diff 对文本节点和 Fragment 有哪些特殊优化路径？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-209：diff 对文本节点与 Fragment 的特殊优化？
**答**：
- 文本节点：React/Vue 都走「快速路径」——同类型文本直接 setText，跳过属性遍历；相邻文本合并（静态拼接编译期完成）。
- Fragment：无真实 DOM，patch 只处理 children 与 key（React 的 key fragment 用于列表头部插入优化）。
- Vue 编译期：纯静态文本被提升为常量字符串，运行时连 vnode 都不创建；插值文本标 patchFlag TEXT 只比文本。
- React 编译优化（React Compiler/RSC）：静态文本内联到 children 字符串，减少 fiber 数量。
- 本质：文本是 diff 中最高频最廉价的节点，快速路径收益占比最大。
