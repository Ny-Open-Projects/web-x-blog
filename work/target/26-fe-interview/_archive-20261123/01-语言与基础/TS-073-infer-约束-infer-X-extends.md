---
title: [TS-073] infer 约束 `infer X extends Y` 有什么用？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-073：infer 约束 `infer X extends Y` 有什么用？
**答**：
- TS 4.8 引入：infer 的类型参数可以直接带 extends 约束，不满足约束时整个分支匹配失败（而不是得到 unknown）。
- 典型用途一：过滤——只让满足约束的解包成功，否则落到 else 分支得到 never。
- 典型用途二：字面量转换——``infer N extends number`` 配合模板字面量把字符串数字转 number（见 TS-095）。

```typescript
// 用途一：约束过滤
type UnwrapNumber<T> = T extends Promise<infer V extends number> ? V : never;

type U1 = UnwrapNumber<Promise<42>>;     // 42
type U2 = UnwrapNumber<Promise<string>>; // never，约束不满足直接匹配失败

// 用途二：捕获字面量而非宽类型
type FirstStr<T extends any[]> = T extends [infer F extends string, ...any[]] ? F : never;
type FS = FirstStr<[`abc`, 1]>; // "abc"（带引号的字面量，而非 string）
```
