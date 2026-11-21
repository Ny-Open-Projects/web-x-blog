---
title: [TS-061] 如何手写 Required 工具类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-061：如何手写 Required 工具类型？
**答**：
- 映射类型加 `-?` 修饰符即可去掉每个属性的可选标记：`{ [K in keyof T]-?: T[K] }`。
- `-?` 的同时会把属性类型中的 `undefined` 一并移除（可缺省属性等价于可能为 undefined）。
- 递归版本 DeepRequired 需要先排除原始值与函数，再对子对象递归应用 `-?`。

```typescript
type MyRequired<T> = { [K in keyof T]-?: T[K] };

interface Options {
  a?: number;
  b?: string;
}

type R = MyRequired<Options>;
// { a: number; b: string }，可选标记被移除
const r: R = { a: 1, b: "x" }; // OK，两个键都必须提供
// const r2: R = { a: 1 }; // 报错：缺少 b

// 递归版：深层的可选也变成必填
type DeepRequired<T> = T extends object
  ? { [K in keyof T]-?: DeepRequired<T[K]> }
  : T;

type D = DeepRequired<{ a?: { b?: string } }>;
// { a: { b: string } }
```
