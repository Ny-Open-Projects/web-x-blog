---
title: [TS-110] 如何实现类型版 Take 与 Drop（截取元组）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-110：如何实现类型版 Take 与 Drop（截取元组）？
**答**：
- 数量用 `1[]` 累加器计数（与 TS-096 同款技巧），比传数字字面量递减更简单。
- Take：计数未到 N 且还有元素时，把头元素收进结果并递归。
- Drop：计数未到 N 时丢弃头元素继续，到 N 后返回剩余全部。

```typescript
type Take<T extends any[], N extends number, Acc extends any[] = []> =
  Acc["length"] extends N
    ? []
    : T extends [infer F, ...infer R]
      ? [F, ...Take<R, N, [...Acc, any]>]
      : [];

type Drop<T extends any[], N extends number, Acc extends any[] = []> =
  Acc["length"] extends N
    ? T
    : T extends [any, ...infer R]
      ? Drop<R, N, [...Acc, any]>
      : [];

type TK1 = Take<[1, 2, 3, 4], 2>; // [1, 2]
type TK2 = Take<[1], 3>;          // [1]（不足 N 时给多少收多少）
type DP1 = Drop<[1, 2, 3, 4], 2>; // [3, 4]
type DP2 = Drop<[1, 2], 5>;       // []

type Paginate = Take<[1, 2, 3, 4, 5], 3>; // 模拟分页第一页取 3 条
```
