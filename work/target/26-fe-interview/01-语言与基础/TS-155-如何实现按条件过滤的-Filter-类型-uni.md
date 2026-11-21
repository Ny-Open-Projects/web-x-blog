---
title: [TS-155] 如何实现按条件过滤的 Filter 类型（union 与 tuple 两个版本）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-155：如何实现按条件过滤的 Filter 类型（union 与 tuple 两个版本）？
**答**：
- 元组版：递归解构头部，满足条件则保留进结果元组，否则丢弃，基线 []。
- 联合版：分布式条件类型天然逐成员处理，但 boolean 会被拆成 true|false 两半，必须用 `[T] extends [U]` 锁住再判断。
- 场景：从事件名联合中剔除内部事件、从参数元组中剔除标记类型。

```typescript
// 元组版过滤
type TupleFilter<T extends unknown[], P> = T extends [infer F, ...infer R]
  ? [...([F] extends [P] ? [F] : []), ...TupleFilter<R, P>]
  : [];

type Kept = TupleFilter<[1, "a", 2, "b"], number>; // [1, 2]

// 联合版过滤（防 boolean 分发陷阱）
type UnionFilter<T, U> = T extends unknown ? ([T] extends [U] ? never : T) : never;
type Clean = UnionFilter<string | number | boolean, boolean>; // string | number

// 反例：T extends U ? never : T 直接判断时，
// boolean 拆成 true/false 分别分发，判断错位导致 boolean 残留
```
