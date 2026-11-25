---
title: [TS-154] 如何实现元组转置 Transpose？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-154：如何实现元组转置 Transpose？
**答**：
- 用同态映射类型替代显式递归：外层映射遍历第一行的列索引，内层映射遍历每一行取同列元素。
- 同态映射（`K in keyof 元组`）天然保持元组形状，是本题的关键（显式递归版要处理行列不对齐）。
- 基线：空矩阵返回 []。

```typescript
type Transpose<M extends number[][]> =
  M extends [infer First extends unknown[], ...infer Rest extends unknown[][]]
    ? { [K in keyof First]: { [R in keyof M]: M[R][K & number] } }
    : [];

type Mat = [
  [1, "a", true],
  [2, "b", false],
];

type T = Transpose<Mat>;
// [[1, 2], ["a", "b"], [true, false]]

// 原理拆解：K 依次是第一行的 "0"/"1"/"2"，
// 内层 { [R in keyof M]: M[R][K] } 对每行取同列 → 三列各自变成一个元组
type Empty = Transpose<[]>; // []
```
