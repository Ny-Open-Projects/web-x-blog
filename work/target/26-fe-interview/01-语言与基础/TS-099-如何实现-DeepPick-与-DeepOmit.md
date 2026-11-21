---
title: [TS-099] 如何实现 DeepPick 与 DeepOmit（递归路径）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-099：如何实现 DeepPick 与 DeepOmit（递归路径）？
**答**：
- DeepPick：路径拆成 `K.Rest` 两段，首段作为对象键、值对剩余路径递归，终止时直接取 `T[Path]`。
- DeepOmit：路径命中的属性保留外壳但值递归剔除，最后一段用键重映射剔除该键。
- 两者都要求 Path 是字符串字面量（点分路径），泛型参数约束 `extends string` 提示补全。

```typescript
type DeepPick<T, Path extends string> =
  Path extends `${infer K}.${infer Rest}`
    ? K extends keyof T
      ? { [P in K]: DeepPick<T[P], Rest> }
      : never
    : Path extends keyof T
      ? { [P in Path]: T[Path] }
      : never;

type DeepOmit<T, Path extends string> =
  Path extends `${infer K}.${infer Rest}`
    ? K extends keyof T
      ? { [P in keyof T]: P extends K ? DeepOmit<T[P], Rest> : T[P] }
      : T
    : { [P in keyof T as P extends Path ? never : P]: T[P] };

interface Org {
  id: number;
  owner: { name: string; secret: string; contact: { email: string } };
}

type Picked = DeepPick<Org, "owner.name" | "owner.contact.email">;
// { owner: { name: string; contact: { email: string } } }

type Safe = DeepOmit<Org, "owner.secret">;
// { id: number; owner: { name: string; contact: { email: string } } }
```
