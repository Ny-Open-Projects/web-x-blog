---
title: [TS-089] 如何实现 FlipArguments（翻转函数参数类型）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-089：如何实现 FlipArguments（翻转函数参数类型）？
**答**：
- 先用 infer 拆出参数元组 P 与返回值 R，把 P 递归反转后重新拼成函数类型。
- 反转套路：`[infer F, ...infer R]` 取首递归 `...Reverse<R>, F`，把首元素不断追加到结果尾部。
- 依赖 TS-107 的 Reverse，本题把它内联使用。

```typescript
type Reverse<T extends any[]> = T extends [infer F, ...infer R]
  ? [...Reverse<R>, F]
  : [];

type FlipArguments<T extends (...args: any[]) => any> =
  T extends (...args: infer P) => infer R
    ? (...args: Reverse<P>) => R
    : never;

function compare(a: number, b: string): boolean { return true; }

type Flipped = FlipArguments<typeof compare>;
// (b: string, a: number) => boolean
declare const flipped: Flipped;
flipped("x", 1); // OK，参数顺序已翻转
```
