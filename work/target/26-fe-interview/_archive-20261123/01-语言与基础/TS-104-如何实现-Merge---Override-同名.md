---
title: [TS-104] 如何实现 Merge / Override（同名字段覆盖规则）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-104：如何实现 Merge / Override（同名字段覆盖规则）？
**答**：
- Merge：后类型 S 的字段优先——先 `Omit<F, keyof S>` 剔除 F 中的重复键，再与 S 交叉。
- 更规整的写法：遍历 `keyof F | keyof S`，S 有该键取 S，否则取 F，得到单一扁平对象（推荐，避免交叉形式的嵌套显示）。
- Override 语义相反（F 覆盖 S）时交换优先级即可。

```typescript
type Merge<F, S> = {
  [K in keyof F | keyof S]: K extends keyof S ? S[K] : K extends keyof F ? F[K] : never;
};

type A = { id: number; name: string; extra: boolean };
type B = { name: string; age: number };

type M = Merge<A, B>;
// { id: number; name: string; extra: boolean; age: number }（name 以 B 为准，仍是 string）

type C = { name: null };
type M2 = Merge<A, C>;
// name 变为 null，S 的同名键覆盖 F
declare const m2: M2;
// m2.name = "x"; // 报错：null
```

## 第二十五章 数组与元组体操
