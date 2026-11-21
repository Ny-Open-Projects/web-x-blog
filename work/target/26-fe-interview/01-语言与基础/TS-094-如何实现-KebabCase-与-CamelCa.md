---
title: [TS-094] 如何实现 KebabCase 与 CamelCase 互转？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-094：如何实现 KebabCase 与 CamelCase 互转？
**答**：
- KebabCase：逐字符递归，遇到大写字母（`C extends Uppercase<C>`）就在前面插 `-` 并转小写。
- 注意首个字符为大写时会产生前导 `-`，严格实现需判断是否在串首。
- CamelCase：匹配 `-` 后的字符，把该字符转大写拼回去，`-` 本身丢弃。

```typescript
type KebabCase<S extends string> =
  S extends `${infer C}${infer R}`
    ? C extends Uppercase<C>
      ? C extends Lowercase<C> // 非字母（数字等）不处理
        ? `${C}${KebabCase<R>}`
        : `-${Lowercase<C>}${KebabCase<R>}`
      : `${C}${KebabCase<R>}`
    : S;

type K1 = KebabCase<"getUserNameById">; // "get-user-name-by-id"
type K2 = KebabCase<"userId2Name">;     // "user-id2-name"

type CamelCase<S extends string> =
  S extends `${infer F}-${infer R}`
    ? `${F}${Capitalize<CamelCase<R>>}` // '-' 丢弃，其后首字母大写
    : S;

type C1 = CamelCase<"get-user-name">; // "getUserName"
type C2 = CamelCase<"user-id-2">;     // "userId2"
```
