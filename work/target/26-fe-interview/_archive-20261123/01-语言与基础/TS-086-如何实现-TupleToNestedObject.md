---
title: [TS-086] 如何实现 TupleToNestedObject？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-086：如何实现 TupleToNestedObject？
**答**：
- 递归取出首元素作为键、剩余元组作为值递归构建：`{ [K in F]: TupleToNestedObject<R, U> }`。
- 元组取空时返回叶子类型 U，这是递归的终止条件。
- 键要求是 string，用 `infer F extends string` 带约束捕获。

```typescript
type TupleToNestedObject<T extends readonly string[], U> =
  T extends readonly [infer F extends string, ...infer R extends readonly string[]]
    ? { [K in F]: TupleToNestedObject<R, U> }
    : U;

type N1 = TupleToNestedObject<["a", "b", "c"], number>;
// { a: { b: { c: number } } }
type N2 = TupleToNestedObject<["key"], string>;
// { key: string }

const v: N1 = { a: { b: { c: 123 } } }; // OK
```
