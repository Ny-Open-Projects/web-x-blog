---
title: [TS-148] Prettify 技巧如何优化编辑器里的类型显示？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-148：Prettify 技巧如何优化编辑器里的类型显示？
**答**：
- Matt Pocock 的 Prettify 与 Simplify 同源：`{ [K in keyof T]: T[K] } & {}`。
- 深层交叉组合（React Props 扩展、工具类型链）hover 时从一长串 `A & B & C` 变成展开的对象字面量。
- 不改变类型等价性，是"纯展示层"重构，可放心全局使用。

```typescript
type Prettify<T> = { [K in keyof T]: T[K] } & {};

type User = { id: number; name: string };
type WithAge = User & { age: number };
type ReadonlyUser = Readonly<User> & { age: number };

type Shown1 = WithAge;                 // hover：User & { age: number }
type Shown2 = Prettify<WithAge>;       // hover：{ id: number; name: string; age: number }
type Shown3 = Prettify<ReadonlyUser>;  // hover：{ readonly id: number; readonly name: string; age: number }

// 场景：组件 Props 继承原生属性时最痛
type ButtonProps = Prettify<React.ButtonHTMLAttributes<HTMLButtonElement> & { variant: "primary" | "ghost" }>;
```
