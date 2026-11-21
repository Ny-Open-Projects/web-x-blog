---
title: [FRP-228] Svelte 的 block 树：if/each 如何编译与切换？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-228：Svelte 的 block 树：if/each 怎么编译？
**答**：
- if 编译成 if_block：条件变化时 destroy 旧块 + create 新块；每个块持有自己的 DOM 与 dirty 状态。
- each 编译成 each_block：key 存在时内部维护 key 映射做 reconcile（类似 mini diff，但只动 DOM 不建 vnode）。
- 块之间有父子/兄弟关系，销毁级联；嵌套块形成 block 树。
- 更新传播：变量 dirty 位图沿块树向下广播，块内按位判断是否重渲染对应表达式。
- 对比 Vue Vapor createFor/createIf：结构同源——编译期框架殊途同归。
