---
title: [R19-243] use API 为什么能在条件/循环里调用而普通 Hook 不行？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-243：use API 为什么能在条件分支里调用？
**答**：
- 普通 Hook 的限制根源是「按调用顺序在 fiber hook 链表上分配槽位」，条件调用会让槽位错位。
- use 不走 hook 链：它是「读取上下文资源的运行时指令」，返回值参与数据流（可 throw promise 触发 Suspense），不依赖调用顺序。
- 合法用法：`if (shouldFetch) { const data = use(promise) }`、在 try/catch 中 use、在组件内任何位置调用。
- 限制仍在：只能在组件或 Hook 的渲染过程中调用；不能在事件处理器/异步回调里 use。
- 面试表达：一句话「use 是资源读取不是状态槽位，所以无顺序约束，但有渲染期约束」。
