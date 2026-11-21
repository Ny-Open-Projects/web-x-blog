---
title: [TS-081] XOR 异或类型（两对象互斥字段）如何实现？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-081：XOR 异或类型（两对象互斥字段）如何实现？
**答**：
- 目标：`A | B` 只能整体选 A 或整体选 B，混写字段要报错。
- 套路：`Without<T, U> | Without<U, T>`——Without 把对方拥有的字段在本方映射为可选 never（`?: never`）。
- 赋值时只要出现对方的字段，类型就是 never 冲突，TS 立即报错；这是"互斥登录方式、支付方式"类业务的标准写法。

```typescript
type Without<T, U> = {
  [P in Exclude<keyof T, keyof U>]?: never;
} & Pick<T, Exclude<keyof T, keyof U>>;

type XOR<T, U> = Without<T, U> | Without<U, T>;

type Login = XOR<
  { username: string; password: string },
  { token: string }
>;

const a: Login = { username: "u", password: "p" }; // OK，走账号密码分支
const b: Login = { token: "t" };                   // OK，走 token 分支
// const c: Login = { username: "u", token: "t" };
// 报错：token 不能赋给 never（两个分支都不满足）
```
