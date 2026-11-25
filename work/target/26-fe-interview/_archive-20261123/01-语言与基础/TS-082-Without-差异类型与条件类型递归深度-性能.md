---
title: [TS-082] Without 差异类型与条件类型递归深度、性能？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-082：Without 差异类型与条件类型递归深度、性能？
**答**：
- Without（差集对象）：保留 T 有而 U 没有的字段，其余字段以 `?: never` 占位堵住赋值，见 TS-081。
- 深度限制：条件类型递归深度上限约 1000 层，超限报 "Type instantiation is excessively deep"，递归体操（如长字符串 Split、大元组 Reverse）都会撞上。
- TS 4.5+ 对"尾递归形式"的条件类型做了尾调用优化，递归位置在末尾的（如 Split、Reverse）可处理更长输入；性能上尽量减少不必要的分发与交叉展开，超长数据考虑运行时而非类型层。

```typescript
// Without：T 相对 U 的差异对象
type Without2<T, U> = {
  [P in Exclude<keyof T, keyof U>]: T[P];
};
type All = { a: number; b: string; c: boolean };
type Common = { a: number };
type Diff = Without2<All, Common>; // { b: string; c: boolean }

// 递归深度压力示例：大元组 Reverse
type Reverse<T extends any[], R extends any[] = []> =
  T extends [infer F, ...infer Rest] ? Reverse<Rest, [F, ...R]> : R;

type Big = Reverse<[1, 2, 3]>; // [3, 2, 1]
// 1000+ 元素时可能报 excessively deep，4.5+ 尾递归优化可缓解
```

## 第二十二章 类型体操经典题
