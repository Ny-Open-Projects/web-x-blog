---
title: [TS-105] 如何实现类型版 Concat、Includes 与 TupleIndexOf？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-105：如何实现类型版 Concat、Includes 与 TupleIndexOf？
**答**：
- Concat：可变元组展开 `[...A, ...B]`，泛型约束为 `readonly any[]` 兼容只读元组。
- Includes：递归逐个元素，用严格 Equal（TS-080 写法二）比较，避免 `[1] extends [number]` 这类宽松匹配误判。
- TupleIndexOf：递归同时维护计数元组 `Idx extends 1[]`，命中时 `Idx["length"]` 即下标，找不到返回 -1。

```typescript
type Concat<A extends readonly any[], B extends readonly any[]> = [...A, ...B];
type C1 = Concat<[1, 2], [3, 4]>; // [1, 2, 3, 4]

type Includes<T extends readonly any[], U> =
  T extends readonly [infer F, ...infer R]
    ? Equal2<F, U> extends true ? true : Includes<R, U>
    : false;

type Equal2<X, Y> =
  (<T>() => T extends X ? 1 : 2) extends (<T>() => T extends Y ? 1 : 2) ? true : false;

type I1 = Includes<[1, 2, 3], 2>;          // true
type I2 = Includes<[1, 2, 3], 4>;          // false
type I3 = Includes<[1, 2, 3], true>;       // false
type I4 = Includes<[1 | 2], 1>;            // false（联合元素不等于 1，严格比较的价值）

type TupleIndexOf<T extends readonly any[], U, Idx extends 1[] = []> =
  T extends readonly [infer F, ...infer R]
    ? Equal2<F, U> extends true ? Idx["length"] : TupleIndexOf<R, U, [...Idx, 1]>
    : -1;

type X1 = TupleIndexOf<["a", "b", "c"], "b">; // 1
type X2 = TupleIndexOf<["a"], "z">;           // -1
```
