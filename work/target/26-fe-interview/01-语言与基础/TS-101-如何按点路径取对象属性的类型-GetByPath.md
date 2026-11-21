---
title: [TS-101] 如何按点路径取对象属性的类型（GetByPath）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-101：如何按点路径取对象属性的类型（GetByPath）？
**答**：
- 递归两段式：`Path extends \`${infer K}.${infer Rest}\`` 时先取 K 的值再递归 Rest。
- 终止分支：Path 本身就是键，直接索引访问 `T[Path]`。
- 路径越界返回 never（或用重载给出友好报错），配合 TS-100 的 Paths 约束可提前报错。

```typescript
type GetByPath<T, Path extends string> =
  Path extends `${infer K}.${infer Rest}`
    ? K extends keyof T
      ? GetByPath<T[K], Rest>
      : never
    : Path extends keyof T
      ? T[Path]
      : never;

interface Store {
  cart: { items: { id: number }[]; total: number };
  user: { name: string };
}

type G1 = GetByPath<Store, "cart.total">;   // number
type G2 = GetByPath<Store, "user.name">;    // string
type G3 = GetByPath<Store, "cart.items">;   // { id: number }[]
type G4 = GetByPath<Store, "cart.missing">; // never

declare function getValue<T, P extends string>(obj: T, path: P): GetByPath<T, P>;
const store = { cart: { total: 99 }, user: { name: "a" } };
getValue(store, "cart.total"); // 推导为 number
```
