---
title: [TS-001] TypeScript 有哪些基础类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-001：TypeScript 有哪些基础类型？
**答**：
- 原始类型：`boolean`、`number`、`string`、`symbol`、`bigint`，以及 `null`、`undefined`。
- 特殊类型：`void`（无返回值）、`never`（永不存在的值）、`any`/`unknown`（任意值）。
- 结构类型：数组 `number[]`、元组 `[string, number]`、对象、函数类型。
- 还有 `enum` 枚举与字面量类型，它们是 TypeScript 对 JS 类型系统的扩展。

```typescript
let isOpen: boolean = true;
let count: number = 42;
let message: string = "hello";
let ids: number[] = [1, 2, 3];
let pair: [string, number] = ["age", 18]; // 元组
let bag: unknown = "任意值";
let empty: void = undefined;
let absent: null = null;
let missing: undefined = undefined;
function throwError(): never {
  throw new Error("boom");
}
```
