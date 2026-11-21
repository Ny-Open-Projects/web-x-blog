---
title: [TS-019] 什么是 const 断言 as const？它改变了什么？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-019：什么是 const 断言 as const？它改变了什么？
**答**：
- 默认推断下对象属性是宽类型且可写；`as const` 把整个字面量变成最深层的只读结构。
- 所有属性加 `readonly`，所有可变值收窄为字面量类型，数组变只读元组。
- 常用于替代 enum 定义常量表、配置项。
- as const 只能用在字面量上，不能用在普通变量表达式。

```typescript
const CONFIG = {
  host: "localhost",
  port: 8080,
  tags: ["a", "b"],
} as const;

// typeof CONFIG 为：
// { readonly host: "localhost"; readonly port: 8080; readonly tags: readonly ["a", "b"] }
// CONFIG.host = "x"; // 报错：只读

let mode = "dark"; // string
const mode2 = "dark"; // 字面量类型 "dark"
```
