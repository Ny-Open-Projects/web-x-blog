---
title: [TS-046] infer 关键字如何使用？有哪些经典应用？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-046：infer 关键字如何使用？有哪些经典应用？
**答**：
- infer 只能在条件类型的 extends 子句中使用，声明一个待推断的类型变量。
- 经典应用：UnwrapPromise、数组元素类型、函数第一个参数、构造函数实例类型。
- 推断位置决定策略：协变位置（返回值）多个候选取联合，逆变位置（参数）取交叉。
- infer 无法直接推断时可以通过两次条件类型"中转"实现。

```typescript
type UnwrapPromise<T> = T extends Promise<infer V> ? V : T;

type A = UnwrapPromise<Promise<string>>; // string
type B = UnwrapPromise<number>; // number

type ElementType<T> = T extends (infer E)[] ? E : never;
type C = ElementType<string[]>; // string

type FirstArg<T> = T extends (first: infer F, ...rest: any[]) => any ? F : never;
type D = FirstArg<(name: string, age: number) => void>; // string
```
