---
title: [TS-111] Permutations 全排列类型的实现思想与复杂度是什么？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-111：Permutations 全排列类型的实现思想与复杂度是什么？
**答**：
- 思路：对联合 T 的每个成员 U，把 U 固定在首位，对 `Exclude<T, U>` 递归求全排列后拼接 `[U, ...Permutations<排除 U>]`。
- 终止：T 排空（为 never）返回 `[]`；本质是把 `n!` 排列搬进类型层。
- 复杂度：成员数为 n 时结果类型数量是 n!，n=8 就是 40320 个类型节点，编译器会明显变慢——面试要点是"知道怎么写，更要知道别在生产写"。

```typescript
type Permutations<T, U = T> =
  [T] extends [never]
    ? []
    : U extends U
      ? [U, ...Permutations<Exclude<T, U>>]
      : never;

type PM = Permutations<"a" | "b">;
// ["a", "b"] | ["b", "a"]，共 2! 种

type PM3 = Permutations<"a" | "b" | "c">;
// 3! = 6 种元组的联合

// 成员超过 8 个时 n! 爆炸，编译期性能急剧下降，慎用
```

## 第二十六章 泛型组件与业务类型设计
