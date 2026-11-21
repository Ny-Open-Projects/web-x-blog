---
title: [TS-159] 递归深度限制与 TS 爆栈案例怎么处理？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-159：递归深度限制与 TS 爆栈案例怎么处理？
**答**：
- 报错 `Type instantiation is excessively deep and possibly infinite`（ts2589）：非尾递归深度上限约 50，超限即报。
- 手段一：改成尾递归（上限约 1000，见 TS-160）；手段二：分而治之降低单次深度。
- 手段三：给体操类型加"深度上限参数"，超限降级为宽类型（unknown）而不是整个报错。

```typescript
// 爆栈案例：Range<10000> 直接 ts2589
// type Range<N extends number, T extends unknown[] = []> =
//   T["length"] extends N ? T : Range<N, [...T, 0]>;

// 深度上限降级（保险丝）：超过 5 层直接给 unknown
type SafeJsonify<T, Depth extends unknown[] = []> =
  Depth["length"] extends 5
    ? unknown
    : T extends object
      ? { [K in keyof T]: SafeJsonify<T[K], [...Depth, unknown]> }
      : T;

type S = SafeJsonify<{ a: { b: { c: { d: { e: { f: 1 } } } } } }>;
// 前五层精确，f 处降级为 unknown，编译不报错
// 分而治之：Range 二分构造再拼接，深度 O(log n)
```
