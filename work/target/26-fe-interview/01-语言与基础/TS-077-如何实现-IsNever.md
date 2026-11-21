---
title: [TS-077] 如何实现 IsNever？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-077：如何实现 IsNever？
**答**：
- 直接写 `T extends never ? true : false` 永远得到 never（TS-076 的 never 分发陷阱）。
- 正确做法：`[T] extends [never]` 用元组包裹抑制分发，让 never 整体参与比较。
- 这是所有 "is xxx" 判定类工具类型的标准开场。

```typescript
type IsNever<T> = [T] extends [never] ? true : false;

type N1 = IsNever<never>;            // true
type N2 = IsNever<string>;           // false
type N3 = IsNever<never | string>;   // false（never 被联合吸收，等价于 string）

// 错误示范
type WrongIsNever<T> = T extends never ? true : false;
type W = WrongIsNever<never>; // never，而不是 true
```
