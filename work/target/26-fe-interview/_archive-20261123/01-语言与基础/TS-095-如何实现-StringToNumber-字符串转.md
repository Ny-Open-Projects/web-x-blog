---
title: [TS-095] 如何实现 StringToNumber（字符串转数字类型）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-095：如何实现 StringToNumber（字符串转数字类型）？
**答**：
- TS 4.8+ 模板字面量 infer 支持 `infer N extends number`，字符串形如数字时自动转换为数字字面量类型。
- 这是 `infer 约束` 最经典的应用，也是 LengthOfString 之外的字符串"算术"基础。
- 不匹配数字的串返回 never 或按需报错。

```typescript
type StringToNumber<S extends string> = S extends `${infer N extends number}`
  ? N
  : never;

type T1 = StringToNumber<"42">;   // 42（数字字面量，不再是字符串）
type T2 = StringToNumber<"-3.5">; // -3.5
type T3 = StringToNumber<"abc">;  // never

// 应用：动态索引取元组元素（字符串下标转数字）
type At<T extends readonly any[], I extends string> =
  StringToNumber<I> extends infer Idx extends number
    ? T[Idx]
    : never;
type A = At<["x", "y", "z"], "1">; // "y"
```
