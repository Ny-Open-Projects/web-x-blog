---
title: [TS-143] utility-types 库的 SetDifference/Subtract/Override 是怎么实现的？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-143：utility-types 库的 SetDifference/Subtract/Override 是怎么实现的？
**答**：
- 集合运算四件套全部建立在分布式条件类型上：SetDifference=差集、SetIntersection=交集、SetComplement=补集。
- Subtract 基于"键集合差 + Pick"挖掉子集字段；Overwrite 用映射类型做"同名字段覆盖"。
- 面试价值：这些是 Pick/Omit 的组合应用，能讲清"键级运算"与"值级运算"的分层。

```typescript
// utility-types 精选实现
type SetDifference<A, B> = A extends B ? never : A;    // A - B
type SetIntersection<A, B> = A extends B ? A : never;  // A ∩ B
type SetComplement<A, A1 extends A> = SetDifference<A, A1>;          // 全集中的补集
type Subtract<T extends T1, T1> = Pick<T, SetDifference<keyof T, keyof T1>>; // 挖掉 T1 覆盖的键
type Overwrite<T, U> = { [K in keyof T]: K extends keyof U ? U[K] : T[K] };

interface Base { id: number; name: string; email: string }
interface Patch { email: string; level: "vip" }

type OnlyMine = Subtract<Base, Patch>;   // Pick<Base, "id" | "name">
type Merged = Overwrite<Base, Patch>;    // email 类型来自 Patch，id/name 保留，level 不进（只覆盖不新增）
```
