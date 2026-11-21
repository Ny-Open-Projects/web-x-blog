---
title: [TS-052] 映射类型的修饰符 +? 与 -readonly 是怎么回事？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-052：映射类型的修饰符 +? 与 -readonly 是怎么回事？
**答**：
- 映射类型可以给属性加修饰符：`?`（可选）与 `readonly`。
- 默认是"+"（加上），用 `-` 可以移除：`-?` 去可选、`-readonly` 去只读。
- Required 的实现就是 `-?`，Mutable（可变）的实现就是 `-readonly`。
- 两者可以同时操作，比如"去掉可选又去掉只读"。

```typescript
type MyRequired<T> = {
  [K in keyof T]-?: T[K];
};

type Mutable<T> = {
  -readonly [K in keyof T]: T[K];
};

interface Draft {
  readonly id?: number;
  readonly name?: string;
}

type Editable = Mutable<MyRequired<Draft>>;
// { id: number; name: string }（可选与只读都被移除）

// 组合：把可选属性还原为必填并保持只读
type Complete = {
  [K in keyof Draft]-?: Draft[K];
};
// { readonly id: number; readonly name: string }
```

## 第十三章 装饰器
