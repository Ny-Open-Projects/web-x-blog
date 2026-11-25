---
title: [FRP-201] React 同层 diff 的三轮遍历策略是什么？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-201：React 同层 diff 的三轮遍历策略是什么？
**答**：
- 第一轮：按位置逐个比较（old[i] vs new[i]），key 相同复用 fiber、不同则跳出——处理「前缀未变」的常见情况。
- 第二轮：把剩余 old 子节点建 Map(key→fiber)，遍历剩余 new：key 命中则复用（记录 oldIndex 用于移动判定），无 key 或 miss 则标记插入。
- 第三轮：收集所有需要移动的 fiber，用「最大递增 oldIndex」判定：比 lastPlacedIndex 小的需要 move，其余原地。
- 复杂度：整体 O(n)，移动判定 O(n log n)（用 LIS 优化时）或 O(n²)（朴素）。
- 对比 Vue3：Vue 用双端 + LIS，React 用单轮 Map + LIS，思想同源——key 复用 + 最少移动。
