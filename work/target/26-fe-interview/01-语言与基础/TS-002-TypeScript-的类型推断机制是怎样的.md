---
title: [TS-002] TypeScript 的类型推断机制是怎样的？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-002：TypeScript 的类型推断机制是怎样的？
**答**：
- 声明时不写注解，TS 会根据初始化值推断类型；`let` 推断为宽类型，`const` 推断为字面量类型。
- 函数返回值会根据 return 语句自动推断，无需显式标注。
- 存在"上下文类型"：回调参数会根据目标位置的函数签名反向推断。
- 最佳公共类型：`let x = cond ? "a" : "b"` 推断为 `string` 而不是字面量联合，这是类型拓宽。

```typescript
let n = 42; // 推断为 number
const s = "hello"; // 推断为字面量类型 "hello"
let mix = Math.random() > 0.5 ? "a" : "b"; // let 会拓宽为 string

function sum(a: number, b: number) {
  return a + b; // 返回值自动推断为 number
}

// 上下文类型：根据目标位置推断回调参数
const names = ["Tom", "Jerry"];
names.map((item) => item.toUpperCase()); // item 自动推断为 string
```
