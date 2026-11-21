---
title: [TS-197] 如何实现 union 去重类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-197：如何实现 union 去重类型？
**答**：
- 联合本身无序且 TS 会合并完全相同的成员；真正需要去重的是"结构相等但声明不同"的体操中间产物（如 boolean 与 true|false 混入）。
- 方案：联合 → 元组（LastOf 递归收集）→ 元组去重 → 回联合。
- LastOf 利用"函数重载推断取最后一个重载"的特性，是联合转元组的标准技巧。

```typescript
type Equal<X, Y> = (<T>() => T extends X ? 1 : 2) extends <T>() => T extends Y ? 1 : 2 ? true : false;

type UnionToIntersection<U> = (U extends unknown ? (k: U) => void : never) extends (k: infer I) => void ? I : never;
type LastOf<U> = UnionToIntersection<U extends unknown ? () => U : never> extends () => infer L ? L : never;
type UnionToTuple<U> = [U] extends [never]
  ? []
  : [...UnionToTuple<Exclude<U, LastOf<U>>>, LastOf<U>];

type Has<T extends unknown[], U> =
  T extends [infer F, ...infer R] ? (Equal<F, U> extends true ? true : Has<R, U>) : false;

type Unique<T extends unknown[], Seen extends unknown[] = []> =
  T extends [infer F, ...infer R]
    ? Has<Seen, F> extends true ? Unique<R, Seen> : [F, ...Unique<R, [...Seen, F]>]
    : [];

type DedupUnion<U> = Unique<UnionToTuple<U>>[number];

type D1 = DedupUnion<"a" | "b" | 1>; // "a" | "b" | 1
type D2 = DedupUnion<boolean | true>; // boolean（true 被判等剔除）
```
