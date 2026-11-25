---
title: [R19-254] flushSync 与 Suspense/并发特性有什么冲突？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-254：flushSync 与 Suspense/并发特性的冲突？
**答**：
- flushSync 强制同步完成更新（跳过并发调度），内部若触发 Suspense 边界的 pending 会导致警告或行为不一致。
- 典型场景：拖拽、动画帧内需要「读 DOM 后立刻写」——flushSync 保证同步性，但代价是放弃并发能力。
- 规则：flushSync 只用于「同步 DOM 读写的极小范围」，不要包整棵树或包含异步数据的子树。
- 替代：多数「需要 flushSync」的场景其实能用 useLayoutEffect + 事务式更新解决。
- 面试表达：先答冲突原理（同步渲染 vs 可中断渲染互斥），再给替代方案。
