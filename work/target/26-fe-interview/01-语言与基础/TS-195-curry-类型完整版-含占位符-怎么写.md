---
title: [TS-195] curry 类型完整版（含占位符）怎么写？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-195：curry 类型完整版（含占位符）怎么写？
**答**：
- 占位符用 unique symbol；已传参数与原参数"逐位合并"，占位符位置保留原参数类型。
- 完成判定：每个参数位都被非占位符实参覆盖才返回结果类型，否则返回"继续传参"的函数。
- 面试讲清合并与判定两个子类型即可；下一次调用参数的精确收窄（Ramda 级别）可作为加分讨论。

```typescript
declare const __: unique symbol;
type Ph = typeof __;

// 已传参数逐位合并：占位符位置保留原参数类型
type Fill<Args extends unknown[], Given extends unknown[]> = {
  [K in keyof Args]: K extends keyof Given
    ? [Given[K]] extends [Ph] ? Args[K] : Given[K]
    : Args[K];
};

// 完成判定：每个位置都有非占位符实参
type Done<Args extends unknown[], Given extends unknown[]> =
  Args extends [unknown, ...infer R]
    ? Given extends [infer G, ...infer GR]
      ? [G] extends [Ph] ? false : Done<R, GR>
      : false
    : true;

type Curry<Args extends unknown[], Ret, Given extends unknown[] = []> =
  Done<Args, Given> extends true
    ? Ret
    : <T extends unknown[]>(...args: T) => Curry<Args, Ret, Fill<Args, [...Given, ...T]>>;

declare function curry<F extends (...args: any[]) => any>(fn: F): Curry<Parameters<F>, ReturnType<F>>;

const fn = (a: string, b: number, c: boolean) => `${a}${b}${c}`;
const c1 = curry(fn);
c1("a")(2)(true);      // 逐个传
c1(__, 2)("a", true);  // 首位占位后补
c1("a", __, true)(2);  // 中间占位
```
