---
title: [TS-102] 如何把嵌套对象拍平为点路径对象（FlattenObject）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-102：如何把嵌套对象拍平为点路径对象（FlattenObject）？
**答**：
- 与 Paths 相似的递归前缀拼接，但叶子返回的是 ` { [K in P]: T } ` 形式的对象，再用映射展开合并。
- 各叶子对象通过映射类型的索引访问展开成扁平结构，键是点路径字面量。
- 常用于把配置树展开成扁平的 `process.env` 风格键值。

```typescript
type FlattenObject<T, P extends string = ""> =
  T extends object
    ? { [K in keyof T & string]-?: FlattenObject<T[K], P extends "" ? K : `${P}.${K}`> }[keyof T & string]
    : { [K in P]: T };

type Flat = FlattenObject<{ a: { b: 1; c: 2 }, d: 3 }>;
// { "a.b": 1; "a.c": 2; d: 3 }

const f: Flat = { "a.b": 1, "a.c": 2, d: 3 };
```
