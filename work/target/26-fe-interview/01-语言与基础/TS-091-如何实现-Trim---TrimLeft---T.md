---
title: [TS-091] 如何实现 Trim / TrimLeft / TrimRight？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-091：如何实现 Trim / TrimLeft / TrimRight？
**答**：
- 定义空白字符联合 `Whitespace = " " | "\t" | "\n"`，模板字面量两侧匹配。
- 递归：匹配到 `${Whitespace}${infer R}` 就继续处理 R，匹配不上时返回，即终止条件。
- Whitespace 是联合，模板字面量会对每个成员尝试匹配，天然覆盖多种空白。

```typescript
type Whitespace = " " | "\t" | "\n";

type TrimLeft<S extends string> =
  S extends `${Whitespace}${infer R}` ? TrimLeft<R> : S;

type TrimRight<S extends string> =
  S extends `${infer R}${Whitespace}` ? TrimRight<R> : S;

type Trim<S extends string> = TrimLeft<TrimRight<S>>;

type A = TrimLeft<"   hello">;        // "hello"
type B = TrimRight<"hello   ">;       // "hello"
type C = Trim<"  hello world  ">;     // "hello world"
```
