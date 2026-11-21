---
title: [TS-070] 如何手写 Parameters、ReturnType 与 ConstructorParameters？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-070：如何手写 Parameters、ReturnType 与 ConstructorParameters？
**答**：
- 三者都是"extends 函数签名 + infer 捕获"的固定套路。
- Parameters 捕获参数元组 `(...args: infer P)`；ReturnType 捕获返回值 `=> infer R`。
- ConstructorParameters 针对**构造函数签名** `abstract new (...args: infer P) => any`，加 `abstract` 是为了兼容抽象类。

```typescript
type MyParameters<T extends (...args: any) => any> =
  T extends (...args: infer P) => any ? P : never;

type MyReturnType<T extends (...args: any) => any> =
  T extends (...args: any) => infer R ? R : never;

type MyConstructorParameters<T extends abstract new (...args: any) => any> =
  T extends abstract new (...args: infer P) => any ? P : never;

function createUser(name: string, age: number) {
  return { name, age };
}
type Args = MyParameters<typeof createUser>;  // [name: string, age: number]
type Ret = MyReturnType<typeof createUser>;   // { name: string; age: number }

class Person {
  constructor(name: string, age: number) {}
}
type CArgs = MyConstructorParameters<typeof Person>; // [string, number]
```
