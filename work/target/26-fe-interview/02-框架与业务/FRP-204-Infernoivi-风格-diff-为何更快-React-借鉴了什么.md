---
title: [FRP-204] Inferno/ivi 风格 diff 为什么快？React 借鉴了什么？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-204：Inferno/ivi 风格 diff 为什么快？
**答**：
- 核心：避免 Map 分配——用 Int32Array 位图记录 key 槽位，key 可转数字索引时 O(1) 查找且无 GC 压力。
- 复用判定用「位图标记 + 剩余节点遍历」替代哈希表；key 数值连续时性能远超 Map。
- LIS 变体：ivi 直接在位图上算最长递增序列，减少中间数组。
- React 的借鉴：React 在节点数量少（≤4）时用线性扫描替代 Map 构建；React 19 优化了 move 判定的数组分配。
- 启示：diff 的性能瓶颈常在「对象分配」而非比较次数——池化与位图是通用优化。
