---
title: [TS-007] 类型断言 as 和非空断言 ! 的作用与风险是什么？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-007：类型断言 as 和非空断言 ! 的作用与风险是什么？
**答**：
- `as` 是主观的类型转换，仅编译期生效，运行时没有任何保护。
- 断言要求两个类型存在可赋值关系之一，完全不重叠时需要双重断言 `as unknown as T`。
- 非空断言 `!` 用于去掉 `null | undefined`，判断失误会直接导致运行时错误。
- 能用类型守卫收窄就不要用断言，断言是"绕过检查"而不是"证明正确"。

```typescript
const el = document.getElementById("app") as HTMLInputElement;
// el.value; // HTMLElement 上没有 value，需要断言后访问

const maybe = document.querySelector(".box")!; // 非空断言，去掉 null | undefined

// 双重断言绕过检查（尽量避免）
const risky = "hello" as unknown as { code: number };
```
