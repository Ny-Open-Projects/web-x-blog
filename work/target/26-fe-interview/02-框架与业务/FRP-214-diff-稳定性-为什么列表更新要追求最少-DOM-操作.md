---
title: [FRP-214] 为什么列表 diff 追求「最少 DOM 操作」而不仅是「正确」？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-214：为什么追求最少 DOM 操作？
**答**：
- 每次 DOM 变更都可能触发：样式失效重算（style invalidation）、layout（重排）、paint——操作次数直接关联帧预算。
- 移动/重建还打断浏览器优化（节点缓存、contain 隔离）；大量移动导致滚动条跳动与动画中断。
- diff 正确性有多个解（不同移动序列都能得到结果），LIS 保证移动最少 = 触发重排区域最小。
- 工程含义：列表容器加 contain: layout/paint 隔离失效范围；动画元素用 transform 避开 layout。
- 面试表达：diff 算法的「最优」定义为最小化 DOM 变更，而非最小化比较次数。
