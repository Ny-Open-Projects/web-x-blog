---
title: [TS-103] 如何实现"指定深度"的 PartialDeep？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-103：如何实现"指定深度"的 PartialDeep？
**答**：
- 用递减计数器控制深度：`Prev` 元组 `[never, 0, 1, 2, ...]`，当前层 D 通过 `Prev[D]` 得到上一层。
- D 为 0 时停止递归，剩余层保持原样；为 number 上限时等价于无限递归。
- 这是"递归深度参数"的通用模板，DeepReadonly、DeepOmit 都能套用。

```typescript
type Prev = [never, 0, 1, 2, 3, 4, 5];

type PartialAtDepth<T, D extends number = 1> =
  D extends 0
    ? T // 深度用尽，保持原样
    : T extends object
      ? { [K in keyof T]?: PartialAtDepth<T[K], Prev[D]> }
      : T;

interface Profile {
  user: { name: string; addr: { city: string } };
  version: number;
}

type P1 = PartialAtDepth<Profile, 1>;
// { user?: Profile["user"]; version?: number }（user 内部保持完整）

type P2 = PartialAtDepth<Profile, 2>;
// { user?: { name?: string; addr?: Profile["user"]["addr"] } ... }

type P3 = PartialAtDepth<Profile>;
// 默认深度 1，同 P1
```
