---
title: [TS-036] 如何手写 Pick、Omit 和 Record？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-036：如何手写 Pick、Omit 和 Record？
**答**：
- Pick 用 `K extends keyof T` 约束后按 K 重新映射，保留指定属性。
- Omit = Pick 反向操作：先用 Exclude 从 keyof T 里剔除 K，再 Pick。
- Record 用 `K extends keyof any`（即 string | number | symbol）生成键集合到 V 的映射。
- Omit 是"先过滤 key 再构造"的两步思路，是面试高频手写题。

```typescript
type MyPick<T, K extends keyof T> = {
  [P in K]: T[P];
};

type MyOmit<T, K extends keyof T> = {
  [P in Exclude<keyof T, K>]: T[P];
};

type MyRecord<K extends keyof any, V> = {
  [P in K]: V;
};

interface User {
  id: number;
  name: string;
  age: number;
}

type UserBrief = MyPick<User, "id" | "name">; // { id: number; name: string }
type UserNoAge = MyOmit<User, "age">; // { id: number; name: string }
type Roles = MyRecord<"admin" | "user", string[]>; // { admin: string[]; user: string[] }
```
