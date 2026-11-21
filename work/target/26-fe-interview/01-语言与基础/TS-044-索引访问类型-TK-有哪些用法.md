---
title: [TS-044] 索引访问类型 T[K] 有哪些用法？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-044：索引访问类型 T[K] 有哪些用法？
**答**：
- `T[K]` 从类型 T 中取出 key K 对应的子类型，K 可以是联合，结果是各子类型的联合。
- 常与 typeof 组合：`typeof ARR[number]` 取数组元素类型、`typeof OBJ[keyof typeof OBJ]` 取值联合。
- 元组支持 `['length']` 取长度字面量类型。
- 可以链式深入：`Person['address']['city']`。

```typescript
const ROLES = ["admin", "editor", "viewer"] as const;
type Role = (typeof ROLES)[number]; // "admin" | "editor" | "viewer"

interface Address {
  city: string;
  zip: string;
}
interface Person {
  name: string;
  address: Address;
}

type City = Person["address"]["city"]; // string
type PersonFields = Person["name" | "address"]; // string | Address

type Pair = [string, number, boolean];
type PairLen = Pair["length"]; // 3（字面量类型）
```

## 第十章 条件类型与 infer

条件类型的求值可以看作一次编译期的分支判断，配合 infer 完成"解构"式的类型提取，整体流程如下。

```mermaid
flowchart TD
    IN[输入类型 T] --> Q{T extends U 是否成立}
    Q -- 成立 --> X[取 true 分支 并可用 infer 解构 U]
    Q -- 不成立 --> Y[取 false 分支]
    X --> D[T 为裸类型参数时逐成员分发]
    D --> OUT[各成员结果合并为联合类型]
    Y --> OUT
```
