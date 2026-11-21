---
title: [TS-096] 如何递归统计字符串长度（LengthOfString）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-096：如何递归统计字符串长度（LengthOfString）？
**答**：
- 递归 + 累加器：每消费一个字符就往元组 Acc 里 push 一个 1，串空时 `Acc["length"]` 即长度。
- 为什么不直接 `S["length"]`？string 的 length 是 number，不是字面量，必须靠元组计数"造"出字面量。
- 长字符串会逼近递归深度限制（1000 层），超长串编译报错是预期行为。

```typescript
type LengthOfString<S extends string, Acc extends any[] = []> =
  S extends `${string}${infer Rest}`
    ? LengthOfString<Rest, [...Acc, 1]>
    : Acc["length"];

type L1 = LengthOfString<"abc">;    // 3
type L2 = LengthOfString<"">;       // 0
type L3 = LengthOfString<"你好">;   // 2（按码元，BMP 内中文为 1）

// 应用：约束参数必须是固定长度
declare function fixedLen<S extends string>(s: S & (LengthOfString<S> extends 4 ? unknown : never)): S;
fixedLen("abcd");  // OK
// fixedLen("abc"); // 报错：长度不是 4
```
