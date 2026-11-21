---
title: [R19-273] Suspense resolve 后的重试走什么优先级通道？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-273：Suspense resolve 后的重试走什么优先级通道？
**答**：
- RetryLanes：promise resolve 后 React 以 Retry 优先级调度重渲染——低于用户交互，高于空闲。
- 设计意图：数据到达的刷新不应打断正在进行的输入/点击；若同时有高优更新，重试延后。
- 嵌套边界：内层边界 resolve 的重试只影响该子树（lane 限定）。
- 可感知行为：后台加载完成的内容「安静地」出现，不抢占交互——这正是「不打断打字」的机制层保障。
- 面试表达：RetryLane 是「数据到货不插队」的调度通道。
