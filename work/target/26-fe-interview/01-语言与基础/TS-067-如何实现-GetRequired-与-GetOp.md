---
title: [TS-067] 如何实现 GetRequired 与 GetOptional（挑出必填/可选字段组成新类型）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-067：如何实现 GetRequired 与 GetOptional（挑出必填/可选字段组成新类型）？
**答**：
- 复用 TS-065 的 `{} extends Pick<T, K>` 判定，但这次在键重映射里挑键并保留值。
- 命中的键映射为自身并取 `T[K]`，未命中的映射为 `never` 被丢弃。
- 与 RequiredKeys 的区别：一个只输出键的联合，一个输出完整的对象类型。

```typescript
type GetRequired<T> = {
  [K in keyof T as {} extends Pick<T, K> ? never : K]: T[K];
};

type GetOptional<T> = {
  [K in keyof T as {} extends Pick<T, K> ? K : never]: T[K];
};

interface Mixed {
  id: number;
  name?: string;
  email?: string;
}

type OnlyReq = GetRequired<Mixed>;
// { id: number }
type OnlyOpt = GetOptional<Mixed>;
// { name?: string; email?: string }
```
