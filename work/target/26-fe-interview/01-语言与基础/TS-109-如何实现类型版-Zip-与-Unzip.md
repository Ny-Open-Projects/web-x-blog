---
title: [TS-109] 如何实现类型版 Zip 与 Unzip？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-109：如何实现类型版 Zip 与 Unzip？
**答**：
- Zip：两个元组同时用 `[infer AF, ...infer AR]` 消费，各取一个拼成 `[AF, BF]` 后递归，任一耗尽即返回 `[]`。
- Unzip：取头元组解构成 [A, B]，对剩余部分递归 Unzip 后分别展开拼接。
- 用 `infer R extends [any[], any[]]` 带约束捕获可减少一层判空。

```typescript
type Zip<A extends any[], B extends any[]> =
  A extends [infer AF, ...infer AR]
    ? B extends [infer BF, ...infer BR]
      ? [[AF, BF], ...Zip<AR, BR>]
      : []
    : [];

type Z1 = Zip<[1, 2, 3], ["a", "b"]>; // [[1, "a"], [2, "b"]]（短的一方决定长度）
type Z2 = Zip<[], [1]>;               // []

type Unzip<T extends [any, any][]> =
  T extends [[infer A, infer B], ...infer R]
    ? R extends [any, any][]
      ? Unzip<R> extends [infer RA extends any[], infer RB extends any[]]
        ? [[A, ...RA], [B, ...RB]]
        : never
      : never
    : [[], []];

type U1 = Unzip<[[1, "a"], [2, "b"]]>; // [[1, 2], ["a", "b"]]
```
