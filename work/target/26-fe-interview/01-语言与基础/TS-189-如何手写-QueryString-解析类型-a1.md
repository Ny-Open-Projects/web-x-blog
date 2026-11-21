---
title: [TS-189] 如何手写 QueryString 解析类型（a=1&b=2 → 对象）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-189：如何手写 QueryString 解析类型（a=1&b=2 → 对象）？
**答**：
- 递归按 "&" 切键值对，每对用 `${infer K}=${infer V}` 拆键值。
- 值的类型化：数字字面量用 `infer N extends number` 转换；无值段约定为布尔开关 true。
- 交叉累积 + Prettify 收束成最终对象类型。

```typescript
type Prettify<T> = { [K in keyof T]: T[K] } & {};

type ParseValue<V extends string> = V extends `${infer N extends number}` ? N : V;

type ParsePair<S extends string> =
  S extends `${infer K}=${infer V}` ? { [P in K]: ParseValue<V> } : { [P in S]: true };

type ParsePairs<S extends string> =
  S extends `${infer KV}&${infer Rest}`
    ? ParsePair<KV> & ParsePairs<Rest>
    : ParsePair<S>;

type Query<S extends string> = Prettify<ParsePairs<S>>;

type Q1 = Query<"a=1&b=hello&page=3">; // { a: 1; b: "hello"; page: 3 }
type Q2 = Query<"debug">;              // { debug: true }（无值开关约定）
type Q3 = Query<"">;                   // { "": true } —— 生产版需先判空
```
