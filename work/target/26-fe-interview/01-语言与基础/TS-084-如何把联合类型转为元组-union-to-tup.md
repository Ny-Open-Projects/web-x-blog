---
title: [TS-084] 如何把联合类型转为元组（union to tuple）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-084：如何把联合类型转为元组（union to tuple）？
**答**：
- 依据：联合出现在**重载函数**的参数位置时，infer 只能读到"最后一个重载"的参数，反复读取再排除即可逐个取出成员。
- 步骤：构造 `(x: 联合) => void` 的交叉，infer 取出一个成员 R，用 `Exclude<T, R>` 缩小联合后递归，never 时终止返回 `[]`。
- 元组顺序依赖实现细节（规范不保证），仅作展示，业务代码慎用。

```typescript
type UnionToOverload<U> = U extends any ? (f: U) => void : never;

type UnionToTuple<T> = [T] extends [never]
  ? []
  : UnionToOverload<T> extends (f: infer R) => void
    ? [R, ...UnionToTuple<Exclude<T, R>>]
    : never;

type UT = UnionToTuple<"a" | "b" | "c">;
// ["c", "b", "a"]（每个成员都在，顺序由内部实现决定）

// 顺手复习：联合转交叉（详见 TS-068）
type UnionToIntersection<U> =
  (U extends any ? (arg: U) => void : never) extends (arg: infer I) => void ? I : never;
type UI = UnionToIntersection<{ a: 1 } | { b: 2 }>; // { a: 1 } & { b: 2 }
```
