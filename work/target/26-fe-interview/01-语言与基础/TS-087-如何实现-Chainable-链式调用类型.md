---
title: [TS-087] 如何实现 Chainable 链式调用类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-087：如何实现 Chainable 链式调用类型？
**答**：
- option 每次返回新的 Chainable，把新键值对交叉进去：`Chainable<T & { [K in Key]: V }>`。
- get() 返回累积的所有键值：`{ [P in keyof T]: T[P] }`（映射类型顺便拍平交叉）。
- Key 约束为 string，保证能做模板字面量与索引签名；这是 Kubb、Builder 模式类型的雏形。

```typescript
type Chainable<T = {}> = {
  option<K extends string, V>(key: K, value: V): Chainable<T & { [P in K]: V }>;
  get(): { [P in keyof T]: T[P] };
};

declare const chain: Chainable;

const result = chain
  .option("name", "foo")
  .option("age", 18)
  .option("active", true)
  .get();
// { name: string; age: number; active: boolean }

result.name;   // string，类型正确收窄
result.age;    // number
```
