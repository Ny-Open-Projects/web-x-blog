---
title: [R19-237] useOptimistic 的底层实现与普通 hook 有什么不同？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-237：useOptimistic 的底层实现与普通 hook 有什么不同？
**答**：
- 普通 useState：值存在 fiber hook 链上，更新走「setState → 调度重渲染」。
- useOptimistic：读值时把「action pending 期间的乐观队列」折叠到 serverState 上再返回——返回值是渲染期计算结果。
- action settled（成功/失败）时 React 清空队列并触发一次基于 serverState 的重渲染，乐观层自然消失。
- 不需要手动清理：与 action 生命周期绑定是它最大的设计优点，也是「必须配 action 用」的原因。
- 细节：useOptimistic 的 reducer 在每次渲染都会执行（队列条目数决定），reducer 复杂度直接影响渲染开销。
