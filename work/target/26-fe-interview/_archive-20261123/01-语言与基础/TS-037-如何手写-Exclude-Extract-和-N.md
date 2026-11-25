---
title: [TS-037] 如何手写 Exclude、Extract 和 NonNullable？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-037：如何手写 Exclude、Extract 和 NonNullable？
**答**：
- 三者都基于分布式条件类型：对联合的每个成员判断 `extends`，按分支保留或丢弃。
- Exclude 保留不满足 U 的成员；Extract 保留满足 U 的成员。
- NonNullable = Exclude<T, null | undefined>，即过滤掉空值成员。
- 记忆方式：Exclude 减法、Extract 加法（交集）、NonNullable 专删空值。

```typescript
type MyExclude<T, U> = T extends U ? never : T;
type MyExtract<T, U> = T extends U ? T : never;
type MyNonNullable<T> = T extends null | undefined ? never : T;

type Status = "loading" | "success" | "error";

type Done = MyExclude<Status, "loading">; // "success" | "error"
type OnlyError = MyExtract<Status, "error" | "success">; // "success" | "error"

type Maybe = string | null | undefined;
type Sure = MyNonNullable<Maybe>; // string
```
