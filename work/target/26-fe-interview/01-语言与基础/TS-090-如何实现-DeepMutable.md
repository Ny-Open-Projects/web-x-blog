---
title: [TS-090] 如何实现 DeepMutable？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-090：如何实现 DeepMutable？
**答**：
- 映射类型加 `-readonly`，并递归处理仍是 object 的属性值。
- 要排除函数与原始值：函数也是 object，直接递归会把函数签名展开出错误结果。
- 数组场景映射为 `DeepMutable<E>[]`，保持元素可变。

```typescript
type Primitive = string | number | boolean | bigint | symbol | null | undefined;

type DeepMutable<T> = T extends Primitive
  ? T
  : T extends (...args: any[]) => any
    ? T // 函数保持原样
    : T extends readonly (infer E)[]
      ? DeepMutable<E>[]
      : { -readonly [K in keyof T]: DeepMutable<T[K]> };

interface AppState {
  readonly user: {
    readonly name: string;
    readonly roles: readonly string[];
  };
  readonly version: number;
}

type Editable = DeepMutable<AppState>;
const s: Editable = { user: { name: "a", roles: ["admin"] }, version: 1 };
s.user.name = "b";        // OK
s.version = 2;            // OK
```

## 第二十三章 字符串类型体操
