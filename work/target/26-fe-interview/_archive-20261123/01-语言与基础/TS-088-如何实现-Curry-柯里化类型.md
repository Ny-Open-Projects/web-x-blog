---
title: [TS-088] 如何实现 Curry 柯里化类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-088：如何实现 Curry 柯里化类型？
**答**：
- 核心是递归条件类型：参数元组每消费一个，返回 `(arg: 下一个) => Curry<剩余, R>`。
- 元组取空时返回最终返回值 R，形成终止分支。
- 剩余参数为空时可直接调用，实战中还需处理可选参数与剩余参数（`...args`），面试给出核心版即可。

```typescript
type Curry<P extends any[], R> =
  P extends [infer F, ...infer Rest]
    ? Rest extends []
      ? (arg: F) => R                    // 最后一个参数，直接返回结果
      : (arg: F) => Curry<Rest, R>       // 还有剩余，继续柯里化
    : R;

declare function curry<P extends any[], R>(fn: (...args: P) => R): Curry<P, R>;

const add = (a: number, b: string, c: boolean) => `${a}${b}${c}`;
const curried = curry(add);
// (arg: number) => (arg: string) => (arg: boolean) => string

const step1 = curried(1);      // (arg: string) => (arg: boolean) => string
const step2 = step1("x");      // (arg: boolean) => string
const final = step2(true);     // string
```
