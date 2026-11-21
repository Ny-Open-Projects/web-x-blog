---
title: [TS-152] 如何实现 All/Any 元组布尔聚合？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-152：如何实现 All/Any 元组布尔聚合？
**答**：
- All：逐位判断 `[F] extends [true]`，基线空元组返回 true（全称量词约定）。
- Any：逐位判断"不是 false 就算真"，基线返回 false。
- 关键细节：用 `[F] extends [X]` 包一层元组，阻止 boolean 被分发出错。

```typescript
type All<T extends unknown[]> = T extends [infer F, ...infer R]
  ? [F] extends [true]
    ? All<R>
    : false
  : true;

type Any<T extends unknown[]> = T extends [infer F, ...infer R]
  ? [F] extends [false]
    ? Any<R>
    : true
  : false;

type T1 = All<[true, true]>;        // true
type T2 = All<[true, false, true]>; // false
type T3 = Any<[false, false]>;      // false
type T4 = Any<[false, true]>;       // true
type T5 = All<[]>;                  // true（空集约定，与逻辑全称量词一致）
type T6 = Any<[]>;                  // false
```
