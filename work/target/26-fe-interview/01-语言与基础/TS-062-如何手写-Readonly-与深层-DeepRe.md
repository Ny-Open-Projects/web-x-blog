---
title: [TS-062] 如何手写 Readonly 与深层 DeepReadonly？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-062：如何手写 Readonly 与深层 DeepReadonly？
**答**：
- 浅层：映射类型加 `+readonly`（默认就是加）或显式写 `readonly`。
- 深层：递归条件类型，对象属性继续 DeepReadonly，数组返回 `readonly DeepReadonly<E>[]`。
- 与 DeepPartial 一样要排除函数与原始值，避免把函数签名也展开。

```typescript
type MyReadonly<T> = { +readonly [K in keyof T]: T[K] };

type DeepReadonly<T> = T extends Primitive
  ? T
  : T extends (...args: any[]) => any
    ? T
    : T extends Array<infer E>
      ? readonly DeepReadonly<E>[]
      : { readonly [K in keyof T]: DeepReadonly<T[K]> };

interface State {
  user: { name: string; tags: string[] };
  onSave: () => void;
}

type Frozen = DeepReadonly<State>;
// user.name 只读、user.tags 变为 readonly string[]、onSave 保持函数原样
const f: Frozen = {
  user: { name: "a", tags: ["x"] },
  onSave: () => {},
};
// f.user.name = "b"; // 报错：只读属性不可赋值
```
