---
title: [TS-012] 为什么裸类型参数的条件类型遇到 never 会直接得到 never？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-012：为什么裸类型参数的条件类型遇到 never 会直接得到 never？
**答**：
- 条件类型中的裸类型参数具有分布式特性，会对联合类型逐成员求值。
- `never` 可理解为"空的联合类型"，逐成员分发时没有成员可遍历，整个条件类型直接退化为 `never`。
- 想判断某类型"是不是 never"，必须用元组包裹阻止分发：`[T] extends [never]`。
- 该特性也常用于在联合类型中过滤成员。

```typescript
type IsNever<T> = [T] extends [never] ? true : false;

type A = IsNever<never>; // true
type B = IsNever<string>; // false

// 裸类型参数遇到 never 会直接"蒸发"整个条件类型
type WithoutString<T> = T extends string ? never : T;
type C = WithoutString<string | number>; // number
type D = WithoutString<never>; // never（没有成员可分发）
```
