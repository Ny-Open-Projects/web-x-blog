---
title: [TS-014] interface 和 type 的区别是什么？如何选择？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-014：interface 和 type 的区别是什么？如何选择？
**答**：
- interface 只能描述对象/函数形状；type 可以表达联合、元组、映射类型、条件类型。
- interface 支持声明合并（同名自动合并），type 重名直接报错。
- 扩展方式不同：interface 用 extends，type 用交叉 `&`；交叉冲突时属性变 never 不报错，interface 扩展冲突则报错。
- 官方建议：能用 interface 描述对象就用 interface，其余场景用 type。

```typescript
interface Animal {
  name: string;
}
interface Animal {
  age: number; // 声明合并：两个同名 interface 自动合并
}
const a: Animal = { name: "Tom", age: 3 };

type Pet = Animal & { owner: string }; // type 可以用交叉扩展

// interface 只能描述对象形状，type 能表达联合、元组等
type Status = "loading" | "done";
type Pair = [string, number];

// 冲突行为不同
interface Conf1 {
  x: string;
}
// interface Conf1 { x: number } // 报错：同名属性类型不一致
type Conf2 = { x: string };
type Merged = Conf2 & { x: number }; // x 变成 never，不报错但不可用
```
