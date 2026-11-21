---
title: [TS-107] 如何实现类型版 First、Last 与 Reverse？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-107：如何实现类型版 First、Last 与 Reverse？
**答**：
- First：`[infer F, ...any[]]` 取头；Last：`[...any[], infer L]` 取尾，注意空元组返回 never 的处理。
- Reverse：经典递归——取头 F，递归反转剩余 R，再把 F 追加到结果尾部。
- Reverse 是 FlipArguments（TS-089）等更多体操的地基，务必熟练。

```typescript
type First<T extends any[]> = T extends [infer F, ...any[]] ? F : never;
type Last<T extends any[]> = T extends [...any[], infer L] ? L : never;

type F1 = First<[1, 2, 3]>; // 1
type F2 = Last<[1, 2, 3]>;  // 3
type F3 = First<[]>;        // never
type F4 = Last<[]>;         // never

type Reverse<T extends any[], Acc extends any[] = []> =
  T extends [infer F, ...infer R]
    ? Reverse<R, [F, ...Acc]>
    : Acc;

type R1 = Reverse<[1, 2, 3]>;       // [3, 2, 1]
type R2 = Reverse<["a", "b"]>;      // ["b", "a"]
```
