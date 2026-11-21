---
title: [TS-146] type-fest 的 Primitive 与 Simplify 是什么？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-146：type-fest 的 Primitive 与 Simplify 是什么？
**答**：
- Primitive 是全原始类型联合，常用于约束"标量字段"与内置类型短路判断。
- Simplify 用同态映射类型把交叉/映射类型"拍平"成单一对象类型，专治编辑器 hover 显示。
- `& {}` 尾巴是展示层的规范化技巧，不改变结构语义。

```typescript
// type-fest Primitive
type Primitive = string | number | bigint | boolean | symbol | null | undefined;

// type-fest Simplify
type Simplify<T> = { [K in keyof T]: T[K] } & {};

type A = { a: string };
type B = { b: number };

type Merged = A & B;              // hover 显示 A & B
type MergedFlat = Simplify<A & B>; // hover 显示 { a: string; b: number }
```
