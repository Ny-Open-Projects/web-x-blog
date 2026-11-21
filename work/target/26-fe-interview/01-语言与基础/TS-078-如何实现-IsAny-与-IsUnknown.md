---
title: [TS-078] 如何实现 IsAny 与 IsUnknown？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-078：如何实现 IsAny 与 IsUnknown？
**答**：
- IsAny 利用"any 与任何类型交叉等于 any"的特性：`0 extends 1 & T`，只有 T 为 any 时 `1 & T` 才兼容 0。
- IsUnknown：unknown 是所有类型的父类型，用 `unknown extends T` 且排除 any/never 即可判定。
- 两者在类型守卫工具库、精确的 Overload 选择场景常见。

```typescript
type IsAny<T> = 0 extends 1 & T ? true : false;

type A1 = IsAny<any>;        // true
type A2 = IsAny<unknown>;    // false
type A3 = IsAny<number>;     // false

type IsUnknown<T> =
  IsAny<T> extends true ? false
  : [T] extends [never] ? false
  : unknown extends T ? true : false;

type U1 = IsUnknown<unknown>;         // true
type U2 = IsUnknown<any>;             // false（已排除）
type U3 = IsUnknown<string>;          // false
type U4 = IsUnknown<{}>;              // false（{} 比 unknown 窄）
```
