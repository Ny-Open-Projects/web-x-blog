---
title: [TS-051] 映射类型的 as 重映射是什么？有什么用？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-051：映射类型的 as 重映射是什么？有什么用？
**答**：
- 语法 `{ [K in keyof T as NewKey]: T[K] }`，as 后面的表达式决定新 key。
- as 后得到 never 的 key 会被直接过滤，可以实现"键过滤"。
- 配合模板字面量可以改写 key（加前缀、改变大小写）。
- 同态映射会保留原属性的 readonly 和 ? 修饰符。

```typescript
interface User {
  id: number;
  name: string;
  kind: string;
}

// 过滤掉 kind 字段
type NoKind = {
  [K in keyof User as K extends "kind" ? never : K]: User[K];
};
// { id: number; name: string }

// 改写 key：加 _ 前缀
type Prefixed = {
  [K in keyof User as `_${string & K}`]: User[K];
};
// { _id: number; _name: string; _kind: string }
```
