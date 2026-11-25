---
title: [R19-381] RSC 序列化边界与 Flight 协议
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, SSR]
type: 面试题
---

## R19-381：RSC 序列化边界与 Flight 协议

**答**：
- Flight 协议：服务端组件输出「流式序列化 UI 描述」——组件引用（client ref）、props、children 树；不是 HTML（那是 SSR 层），是「可恢复的 UI 蓝图」
- 序列化能力：字符串/数字/数组/对象/Promise/Map/Set/Date/BigInt/循环引用——不支持：函数（除 server fn 引用）/类实例/DOM/事件处理器——client/server 边界的 API 设计约束
- client ref 机制：服务端树中出现的客户端组件只传「引用（模块路径 + 导出名）」——客户端按需加载 chunk 后组装
- 流式与 partial：Flight 流允许「引用后置」（数据未就绪时占位 promise 槽位）——长任务数据不阻塞整棵树传输
- 实战约束：props 可序列化决定组件拆分边界——「大对象/复杂类」要拆到 client 侧构造

```text
Flight 输出:
  0: ["$@1", "div", null, {"className": "card"}]     // vnode 描述
  1: {"name": "ProductCard", "chunk": "static/chunks/123.js"}  // client ref
  2: Promise 槽位 (数据后到)
客户端: 解析流 → 引用回填 → 可交互树
```
