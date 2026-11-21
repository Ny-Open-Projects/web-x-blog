---
title: [TS-108] 如何实现嵌套数组拍平的类型 Flatten？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-108：如何实现嵌套数组拍平的类型 Flatten？
**答**：
- 递归：取头元素 F，若 F 还是数组就先递归拍平 F，再与剩余 R 的拍平结果拼接。
- 终止条件：空元组返回 `[]`；非元组分支不存在（外层已保证是元组）。
- 与 DeepReadonly 处理数组的思路一致：先判断元素是否为容器再决定递归。

```typescript
type Flatten<T extends any[]> =
  T extends [infer F, ...infer R]
    ? F extends any[]
      ? [...Flatten<F>, ...Flatten<R>]
      : [F, ...Flatten<R>]
    : [];

type FL1 = Flatten<[1, [2, [3, [4]]], 5]>; // [1, 2, 3, 4, 5]
type FL2 = Flatten<[string, [number, boolean]]>; // [string, number, boolean]

// 应用：把"列 + 嵌套列"的表头配置拍平
type Header = { key: string; children?: Header[] };
type FlatKeys<H extends Header[]> = H extends [infer F, ...infer R]
  ? R extends Header[]
    ? F extends Header
      ? F["children"] extends Header[] ? [...FlatKeys<F["children"]>, ...FlatKeys<R>] : FlatKeys<R>
      : never
    : never
  : [];
```
