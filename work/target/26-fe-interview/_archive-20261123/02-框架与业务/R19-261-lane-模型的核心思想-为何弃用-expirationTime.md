---
title: [R19-261] Lane 模型的核心思想：为什么弃用 expirationTime？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-261：Lane 模型的核心思想：为什么弃用 expirationTime？
**答**：
- expirationTime 是单一数值时间戳：只能表达「紧迫度」，无法同时表达「类型」（Sync/Transition/Suspense 等）与「批量组合」。
- Lane 用位掩码（31 位）：每位代表一个优先级通道，多个更新可叠加（lanes 按位或），调度器挑最高位优先处理。
- 优势一：批量合并——同 lane 的多个更新一次处理；优势二：中断恢复——被高优打断后记录 pendingLanes，回来继续。
- 类型表达：Transition lane / Retry lane / Sync lane 各自独立通道，Suspense 重试不会抢同步通道。
- 面试表达：「单一数值 → 位图多通道」是并发调度的地基，lane 让「优先级抢占」和「批量复用」同时成立。
