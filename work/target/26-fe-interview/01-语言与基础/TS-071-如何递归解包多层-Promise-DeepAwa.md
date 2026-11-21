---
title: [TS-071] 如何递归解包多层 Promise（DeepAwaited）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-071：如何递归解包多层 Promise（DeepAwaited）？
**答**：
- 内置 `Awaited<T>` 已经做了这件事（含 thenable），手写考察的是递归 infer。
- 模式：`T extends Promise<infer V> ? DeepAwaited<V> : T`，一层层剥到非 Promise 为止。
- 递归要有终止条件（不匹配 Promise 时直接返回 T），否则会无限递归报错。

```typescript
type DeepAwaited<T> = T extends Promise<infer V> ? DeepAwaited<V> : T;

type D1 = DeepAwaited<Promise<string>>;                     // string
type D2 = DeepAwaited<Promise<Promise<number[]>>>;          // number[]
type D3 = DeepAwaited<Promise<{ a: Promise<boolean> }>>;    // { a: Promise<boolean> }（属性内的不会展开，是浅层停止点）

// 与内置 Awaited 对照
type A1 = Awaited<Promise<Promise<string>>>; // string
```
