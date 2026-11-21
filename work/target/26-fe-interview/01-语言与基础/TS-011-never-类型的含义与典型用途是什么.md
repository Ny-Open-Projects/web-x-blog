---
title: [TS-011] never 类型的含义与典型用途是什么？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-011：never 类型的含义与典型用途是什么？
**答**：
- `never` 是底层类型，表示"不可能有值"：抛错函数、死循环函数的返回值类型就是 never。
- never 可以赋给任何类型，但任何类型都不能赋给 never。
- 典型用途是穷尽性检查：联合类型收窄到 default 分支后剩余类型是 never，若漏处理某分支，赋值给 never 会编译报错。
- 条件类型中常用 `[T] extends [never]` 来检测 never。

```typescript
function fail(message: string): never {
  throw new Error(message);
}

function infinite(): never {
  while (true) {}
}

// never 可以赋值给任意类型，但任何值都不能赋给 never
let n: never;
let s: string = n; // OK
// n = "x"; // 报错
```
