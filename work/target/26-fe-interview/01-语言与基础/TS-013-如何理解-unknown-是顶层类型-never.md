---
title: [TS-013] 如何理解 unknown 是顶层类型、never 是底层类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-013：如何理解 unknown 是顶层类型、never 是底层类型？
**答**：
- 顶层类型：所有类型都可以赋给它，`unknown`（以及 `any`）就是顶层。
- 底层类型：它可以赋给所有类型，但没有任何运行时值属于它，`never` 是唯一代表。
- `object` 表示"非原始类型"，数组、函数也算 object。
- `{}` 表示"非 null/undefined 的任意值"，比 object 宽得多，容易误用。

```typescript
// unknown 是顶层类型：任何值都可以赋给它
let top: unknown = 123;
top = "anything";

// never 是底层类型：只能接收 never
let bottom: never;
// bottom = 123; // 报错

// object 表示非原始类型
let obj: object = { a: 1 };
obj = []; // OK，数组也是 object
// obj = 42; // 报错

// {} 表示非 null/undefined 的任意值
let almost: {} = "anything";
// almost = null; // 报错
```

## 第三章 接口、类型别名与联合交叉
