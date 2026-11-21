---
title: [TS-199] 如何用 Apply 类型收束递归体操全家桶？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-199：如何用 Apply 类型收束递归体操全家桶？
**答**：
- Apply：把函数类型"应用"到参数元组得到返回类型，条件类型 + infer 的最纯形态。
- 收束记忆：全章递归共享一个骨架——"解构头部 + 累加器生长 + 基线返回"。
- 面试策略：先讲骨架与终止条件，再落笔写具体题（Len/Chunk/Reverse/Transpose 都是同一模式的变体）。

```typescript
// Apply：函数类型应用到参数元组
type Apply<F extends (...args: never[]) => unknown, A extends unknown[]> =
  F extends (...args: A) => infer R ? R : never;

type Fn = (a: string, b: number) => boolean;
type R1 = Apply<Fn, [string, number]>;  // boolean
type R2 = Apply<Fn, [number, number]>;  // never：参数不匹配

// 递归全家桶的共同骨架（一句话模板）
type Pattern<T extends unknown[], Acc extends unknown[] = []> =
  T extends [infer F, ...infer R] ? Pattern<R, [F, ...Acc]> : Acc;

type Reversed = Pattern<[1, 2, 3]>; // [3, 2, 1]
// 变体对照：
// Len     → Acc 计数取 length
// Chunk   → Acc 攒批满 N 产出
// Unique  → Acc 作 Seen 查重
// FindIndex → Acc 计数在命中处返回
// Transpose → 同态映射替代显式递归
```
