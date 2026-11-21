---
title: [TS-156] 如何实现类型版 FindIndex？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-156：如何实现类型版 FindIndex？
**答**：
- 递归解构 + Idx 计数器累加器（每层推一个 unknown），命中条件返回 `Idx["length"]`。
- 找不到返回 -1；判等用 `[F] extends [P]` 防 boolean 陷阱。
- 计数器走参数位是尾递归，天然兼容 TS 4.5 深度优化。

```typescript
type FindIndex<T extends unknown[], P, Idx extends unknown[] = []> =
  T extends [infer F, ...infer R]
    ? [F] extends [P]
      ? Idx["length"]
      : FindIndex<R, P, [...Idx, unknown]>
    : -1;

type Idx1 = FindIndex<[string, number, boolean], number>; // 1
type Idx2 = FindIndex<["a", "b"], "b">;                   // 1
type Idx3 = FindIndex<["a", "b"], "c">;                   // -1
type Idx4 = FindIndex<[true, false], boolean>;            // 0（boolean 分发被元组锁住）
```
