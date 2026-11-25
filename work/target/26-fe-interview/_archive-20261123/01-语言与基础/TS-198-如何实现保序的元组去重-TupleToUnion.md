---
title: [TS-198] 如何实现保序的元组去重（TupleToUnion 的保序版）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-198：如何实现保序的元组去重（TupleToUnion 的保序版）？
**答**：
- Seen 累加器查重：命中重复丢弃、未命中保留在前，递归消费剩余，天然保序。
- 判等用 Equal（严格相等），避免子类型误伤；想"子类型算重复"可换成 `F extends Seen[number]` 判等。
- 复杂度 O(n²)（Seen 线性扫描），大元组建议控制规模或改用"先排布后过滤"的映射方案。

```typescript
type Equal<X, Y> = (<T>() => T extends X ? 1 : 2) extends <T>() => T extends Y ? 1 : 2 ? true : false;

type Includes<T extends unknown[], U> =
  T extends [infer F, ...infer R] ? (Equal<F, U> extends true ? true : Includes<R, U>) : false;

type Unique<T extends unknown[], Seen extends unknown[] = []> =
  T extends [infer F, ...infer R]
    ? Includes<Seen, F> extends true
      ? Unique<R, Seen>                        // 重复：丢弃，保序
      : [F, ...Unique<R, [...Seen, F]>]        // 首次：保留在前
    : [];

type U1 = Unique<[1, 2, 1, 3, 2]>;          // [1, 2, 3]（保序）
type U2 = Unique<[string, number, string]>; // [string, number]
type U3 = Unique<[true, 1, true]>;          // [true, 1]
// 对比：UnionToUnion 版（TS-197）不保序也无需保序，元组版必须保序
```
