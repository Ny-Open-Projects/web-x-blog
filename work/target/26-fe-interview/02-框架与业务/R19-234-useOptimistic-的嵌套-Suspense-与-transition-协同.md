---
title: [R19-234] useOptimistic 在并发渲染下为什么不会被「丢弃」？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-234：useOptimistic 在并发渲染下为什么不会被丢弃？
**答**：
- 乐观值存放在 React 内部的「队列 + 当前渲染上下文」，与 transition 无关：即使在 transition 渲染中，读 useOptimistic 拿到的也是折叠后的乐观状态。
- 对比错误做法：把乐观值放 useState 再在 transition 里改 state——并发中断时 state 可能被回退，乐观显示闪烁。
- 实现本质：useOptimistic 的值在每次 action pending 期间「附着」到渲染树，是渲染派生而非独立 state。
- 面试表达：一句话「乐观值是渲染期叠加层，不是持久 state，所以天然并发安全」。
