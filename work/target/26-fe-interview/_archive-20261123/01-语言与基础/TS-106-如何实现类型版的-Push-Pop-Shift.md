---
title: [TS-106] 如何实现类型版的 Push、Pop、Shift、Unshift？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-106：如何实现类型版的 Push、Pop、Shift、Unshift？
**答**：
- 全部基于可变元组展开：Push 尾插 `[...T, V]`、Unshift 头插 `[V, ...T]`。
- Pop/Shift 用展开模式捕获"除一个之外"的剩余元组：Pop 取 `[...Rest, any]` 的 Rest，Shift 取 `[any, ...Rest]`。
- 加 `as const` 或 readonly 约束时注意先把元组转成可变形式。

```typescript
type Push<T extends any[], V> = [...T, V];
type Unshift<T extends any[], V> = [V, ...T];
type Pop<T extends any[]> = T extends [...infer Rest, any] ? Rest : [];
type Shift<T extends any[]> = T extends [any, ...infer Rest] ? Rest : [];

type P1 = Push<[1, 2], 3>;       // [1, 2, 3]
type P2 = Unshift<[2, 3], 1>;    // [1, 2, 3]
type P3 = Pop<[1, 2, 3]>;        // [1, 2]
type P4 = Shift<[1, 2, 3]>;      // [2, 3]
type P5 = Pop<[]>;               // []

// 应用：向 reducer 的动作栈追加类型
type ActionTypes = ["init", "start", "done"];
type NextActions = Push<ActionTypes, "reset">; // ["init", "start", "done", "reset"]
```
