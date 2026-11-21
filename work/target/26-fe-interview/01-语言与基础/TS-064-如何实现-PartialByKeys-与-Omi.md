---
title: [TS-064] 如何实现 PartialByKeys 与 OmitByKeys？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-064：如何实现 PartialByKeys 与 OmitByKeys？
**答**：
- PartialByKeys：把指定键改可选、其余保持原样，用键重映射 `as` 配合条件判断。
- 两组属性交叉后类型是交叉形式，可用 `Omit<T, never>` 或 `Merge` 技巧拍平成单一对象类型。
- OmitByKeys：排除指定键，等价于 `Pick<T, Exclude<keyof T, K>>`，可用映射类型手写。

```typescript
type PartialByKeys<T, K extends keyof T = keyof T> = Omit<
  { [P in K]?: T[P] } & { [P in Exclude<keyof T, K>]: T[P] },
  never
>; // Omit<..., never> 把交叉拍平成单一对象

interface User {
  id: number;
  name: string;
  age: number;
}

type Patch = PartialByKeys<User, "name" | "age">;
// { id: number; name?: string; age?: number }
const p: Patch = { id: 1, name: "a" }; // OK，name/age 可省略
// const p2: Patch = {}; // 报错：缺少 id

type OmitByKeys<T, K extends keyof T> = {
  [P in Exclude<keyof T, K>]: T[P];
};
type NoAge = OmitByKeys<User, "age">; // { id: number; name: string }
```
