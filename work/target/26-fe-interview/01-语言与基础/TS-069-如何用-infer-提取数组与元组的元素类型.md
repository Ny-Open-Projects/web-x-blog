---
title: [TS-069] 如何用 infer 提取数组与元组的元素类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-069：如何用 infer 提取数组与元组的元素类型？
**答**：
- 数组：`T extends (infer E)[] ? E : never`，联合数组会分发到每个元素再联合。
- 元组：用展开模式 `[infer F, ...infer R]` 可同时拿到首个元素和剩余元组，是递归体操的基础。
- 只读数组要写 `readonly (infer E)[]`，否则匹配不上。

```typescript
type ElementType<T> = T extends readonly (infer E)[] ? E : never;

type E1 = ElementType<string[]>;            // string
type E2 = ElementType<number[] | boolean[]>; // number | boolean
type E3 = ElementType<readonly [1, 2, 3]>;   // 1 | 2 | 3

type FirstOfTuple<T extends any[]> = T extends [infer F, ...any[]] ? F : never;
type F1 = FirstOfTuple<["a", "b", "c"]>; // "a"
```
