---
title: [TS-079] 如何实现 IsUnion？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-079：如何实现 IsUnion？
**答**：
- 思路：引入第二个类型参数 `C = T`，让 C 作为裸类型参数分发到 T 的每个成员。
- 对每个成员判定 `[T] extends [C]`：成员是联合的一部分但整体又不等于该成员时，说明 T 是联合。
- 单一类型分发后 C 与 T 相同，走 false 分支；never 仍要先排除。

```typescript
type IsUnion<T, C = T> =
  [T] extends [never] ? false
  : C extends T
    ? [T] extends [C] ? false : true
    : false;

type I1 = IsUnion<"a" | "b">;  // true
type I2 = IsUnion<string>;     // false
type I3 = IsUnion<never>;      // false
type I4 = IsUnion<1 | 2 | 3>;  // true

// 过程拆解（T = "a" | "b"）：
// C = "a" 时："a" extends "a"|"b" 成立 → ["a"|"b"] extends ["a"] 不成立 → true
// C = "b" 时：同理 → true
// true | true = true
```
