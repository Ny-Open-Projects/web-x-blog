---
title: [TS-043] typeof 在类型世界的作用是什么？与 JS 的 typeof 有何不同？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-043：typeof 在类型世界的作用是什么？与 JS 的 typeof 有何不同？
**答**：
- TS 的 `typeof` 是类型查询操作符：从"值的世界"取类型，JS 的 typeof 是运行时运算符。
- 对 const 变量取类型后可配合索引访问、keyof 派生更多类型。
- 对函数取类型得到其签名，可用于声明回调参数类型。
- typeof 只能用于标识符或属性访问，不能用于任意表达式。

```typescript
const config = {
  api: "https://api.example.com",
  retry: 3,
  features: ["login", "pay"],
};

type Config = typeof config;
// { api: string; retry: number; features: string[] }

type ConfigKeys = keyof Config; // "api" | "retry" | "features"

function request(path: string, options?: typeof config) {}

function handler() {
  return "done";
}
type Handler = typeof handler; // () => string
```
