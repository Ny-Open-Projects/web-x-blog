---
title: [TS-085] 如何获取元组的长度类型（TupleLength）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-085：如何获取元组的长度类型（TupleLength）？
**答**：
- 直接索引访问 `T["length"]`，对元组返回字面量数字类型（元组长度是类型的一部分）。
- 对普通数组返回 number，对 unknown 长度的只读数组同理。
- 结合上一章的计数技巧，`1[]` 数组累加也能"造"出字面量数字类型，用于递归计数。

```typescript
type TupleLength<T extends readonly any[]> = T["length"];

type L1 = TupleLength<[string, number, boolean]>; // 3（字面量）
type L2 = TupleLength<[]>;                        // 0
type L3 = TupleLength<string[]>;                  // number（普通数组失去字面量）

// 递归计数造字面量数字：加一个元素就把长度 +1
type Count<Arr extends any[], Acc extends 1[] = []> =
  Arr extends [any, ...infer R] ? Count<R, [...Acc, 1]> : Acc["length"];
type C = Count<[1, 2, 3]>; // 3
```
