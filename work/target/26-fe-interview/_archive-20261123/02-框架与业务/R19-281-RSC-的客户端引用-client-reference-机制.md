---
title: [R19-281] RSC 的客户端引用（client reference）机制是什么？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-281：RSC 的客户端引用（client reference）机制是什么？
**答**：
- 'use client' 文件的导出在服务端编译成 client reference（模块 id + 导出名占位对象），RSC 树里以「引用」形式出现而非实际渲染。
- Flight 序列化时引用变成 `$L1`/`$F1` 形式的标记，客户端 chunk manifest 据此加载对应模块并实例化。
- 服务端可以直接把 props 传给客户端组件（可序列化部分），也可以把 server action 作为 prop 传下去（函数引用）。
- 边界规则：客户端组件 import 服务端组件只能通过 children/props 传递（组合模式），不能直接 import。
- 面试表达：'use client' 不是「变成客户端渲染」，而是「标记边界，服务端渲染其引用」。
