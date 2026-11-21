---
title: [TS-035] 如何手写 Partial、Required 和 Readonly？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-035：如何手写 Partial、Required 和 Readonly？
**答**：
- 三者都是同态映射类型：遍历 `keyof T`，映射时修改可选性或 readonly 修饰符。
- Partial 用 `?` 把所有属性变可选，Required 用 `-?` 去掉可选性。
- Readonly 用 `readonly` 前缀加只读，常用于冻结配置与 props。
- 修饰符加减语法：`+?`/`-?`、`+readonly`/`-readonly`。

```typescript
type MyPartial<T> = {
  [K in keyof T]?: T[K];
};

type MyRequired<T> = {
  [K in keyof T]-?: T[K];
};

type MyReadonly<T> = {
  readonly [K in keyof T]: T[K];
};

interface User {
  id: number;
  name?: string;
}

type P = MyPartial<User>; // { id?: number; name?: string }
type R = MyRequired<P>; // { id: number; name: string }
type RO = MyReadonly<User>; // { readonly id: number; readonly name?: string }
```
