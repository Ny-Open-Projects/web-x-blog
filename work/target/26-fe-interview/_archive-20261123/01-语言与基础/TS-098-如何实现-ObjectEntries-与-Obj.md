---
title: [TS-098] 如何实现 ObjectEntries 与 ObjectFromEntries？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-098：如何实现 ObjectEntries 与 ObjectFromEntries？
**答**：
- ObjectEntries：先用 `-?` 把属性全转必填（避免 `[K, T[K] | undefined]`），映射出 `[K, 值]` 元组再用索引访问取出元组联合。
- 值是对象时递归展开成嵌套 entries，与 `Object.entries` 行为对齐。
- ObjectFromEntries：`E[0]` 作为键的联合做映射，值用 `Extract<E, [K, any]>[1]` 按键提取。

```typescript
type ObjectEntries<T> = {
  [K in keyof T]-?: [K, T[K] extends object ? ObjectEntries<T[K]> : T[K]];
}[keyof T];

type ObjectFromEntries<E extends readonly [PropertyKey, any]> = {
  [K in E[0]]: Extract<E, [K, any]>[1];
};

type Entries = ObjectEntries<{ id: number; user: { name: string } }>;
// ["id", number] | ["user", ["name", string]]

type E = [["a", 1], ["b", "x"]] as const;
type Obj = ObjectFromEntries<E>;
// { a: 1; b: "x" }
```
