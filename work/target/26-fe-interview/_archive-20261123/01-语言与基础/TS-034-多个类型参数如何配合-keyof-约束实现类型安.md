---
title: [TS-034] 多个类型参数如何配合 keyof 约束实现类型安全的取值？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-034：多个类型参数如何配合 keyof 约束实现类型安全的取值？
**答**：
- 经典模式：`<T, K extends keyof T>`，把第二个参数限制为第一个参数的 key。
- 返回值类型是索引访问 `T[K]`，与实际取到的属性精确对应。
- 适用于 pluck、groupBy 等集合工具函数。
- 联合 key 也支持：`K extends keyof T` 可以传入多个 key 的联合。

```typescript
function pluck<T, K extends keyof T>(items: T[], key: K): T[K][] {
  return items.map((item) => item[key]);
}

const people = [
  { name: "Tom", age: 18 },
  { name: "Jerry", age: 20 },
];

const names = pluck(people, "name"); // string[]
const ages = pluck(people, "age"); // number[]
// pluck(people, "email"); // 报错："email" 不在 keyof T 中
```

## 第八章 工具类型与手写实现
