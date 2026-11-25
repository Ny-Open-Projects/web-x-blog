---
title: [R19-402] 并发渲染边界：Server Component 与并发渲染的交互
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, SSR]
type: 面试题
---

## R19-402：并发渲染边界：Server Component 与并发渲染的交互

**答**：
- RSC 的渲染在服务端（同步流式），并发渲染只作用于 client 树——但两者通过 Flight 流衔接：server chunk 未到 → client 侧 Suspense 占位（可打断等待）
- server fn 在 transition 中调用：表单 action 包 transition——提交期间 UI 保持 + pending；server 响应到达 → Flight 流增量更新
- 撕裂不跨边界：server 渲染的数据是「请求时快照」（进入 props 后不可变）——client 树内并发重渲染读的是同一 props 快照，天然一致
- 部分水合与并发：未水合的 client chunk 到达前——用户交互由 React 记录重放（R19-373）；server 树不存在水合问题
- 设计含义：把「天然稳定的数据」留在 server 侧渲染——client 并发的内存/CPU 预算留给真正交互的区域

```text
Server: 渲染一次, 数据快照, 流式输出
Client: 并发可打断, props 为不可变快照
衔接: chunk 未到 → Suspense 占位; server fn → transition 包裹提交
```
