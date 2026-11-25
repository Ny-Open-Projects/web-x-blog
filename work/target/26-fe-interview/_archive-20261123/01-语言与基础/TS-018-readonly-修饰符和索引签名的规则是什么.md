---
title: [TS-018] readonly 修饰符和索引签名的规则是什么？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-018：readonly 修饰符和索引签名的规则是什么？
**答**：
- `readonly` 只是编译期检查，运行时对象照样可以被修改，它不等于 const。
- 索引签名 `[key: string]: T` 允许任意字符串 key，其值类型必须兼容所有显式属性。
- number 索引是 string 索引的子集，两者并存时 number 索引值类型必须更窄或相等。
- `readonly number[]` 只读数组没有 push/splice 等变更方法。

```typescript
interface Config {
  readonly apiKey: string; // 编译期只读，运行时无保护
  [key: string]: string | number; // 字符串索引签名
}

const config: Config = { apiKey: "abc", timeout: 3000, extra: "ok" };
// config.apiKey = "x"; // 报错：只读属性

const fixed: readonly number[] = [1, 2, 3];
// fixed.push(4); // 报错：只读数组没有变更方法
```

## 第四章 字面量类型与 const 断言
