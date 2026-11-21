---
title: [TS-038] 如何用 infer 手写 ReturnType、Parameters 和 InstanceType？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-038：如何用 infer 手写 ReturnType、Parameters 和 InstanceType？
**答**：
- infer 在 extends 条件类型中"占位"推断函数签名的某一部分。
- ReturnType 推断返回值：`T extends (...args: any) => infer R ? R : never`。
- Parameters 推断参数元组：`T extends (...args: infer P) => any ? P : never`。
- InstanceType 推断构造函数实例类型：`T extends new (...args: any) => infer I ? I : never`。

```typescript
type MyReturnType<T extends (...args: any) => any> = T extends (
  ...args: any
) => infer R
  ? R
  : never;

type MyParameters<T extends (...args: any) => any> = T extends (
  ...args: infer P
) => any
  ? P
  : never;

type MyInstanceType<T extends abstract new (...args: any) => any> = T extends
  abstract new (...args: any) => infer I
  ? I
  : never;

function createUser(name: string, age: number) {
  return { name, age, id: 1 };
}

type CreateResult = MyReturnType<typeof createUser>; // { name: string; age: number; id: number }
type CreateArgs = MyParameters<typeof createUser>; // [name: string, age: number]

class Car {
  drive() {}
}
type CarInstance = MyInstanceType<typeof Car>; // Car
```
