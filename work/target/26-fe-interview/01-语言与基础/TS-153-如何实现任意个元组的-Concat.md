---
title: [TS-153] 如何实现任意个元组的 Concat？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-153：如何实现任意个元组的 Concat？
**答**：
- TS-105 是两参版；多元组版接收"元组的元组"，头部展开 + 递归尾部拼接。
- infer R 必须约束为 `unknown[][]`，否则展开时丢失元组性退化为数组。
- 尾递归形态，配合 TS 4.5 优化可扛长输入。

```typescript
type Concat<T extends unknown[][]> =
  T extends [infer F extends unknown[], ...infer R extends unknown[][]]
    ? [...F, ...Concat<R>]
    : [];

type A = [1, 2];
type B = [string];
type C = [true, false];

type Joined = Concat<[A, B, C]>; // [1, 2, string, true, false]
type Pair = Concat<[A, B]>;      // [1, 2, string] —— 两参版是其特化
type Empty = Concat<[A, [], C]>; // [1, 2, true, false] —— 空元组自然跳过
```
