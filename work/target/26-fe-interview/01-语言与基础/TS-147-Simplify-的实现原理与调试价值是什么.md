---
title: [TS-147] Simplify 的实现原理与调试价值是什么？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-147：Simplify 的实现原理与调试价值是什么？
**答**：
- 同态映射类型（`K in keyof T`）本身就是一次"重新声明"，编辑器会展开显示其结果。
- 调试价值一：组合多个工具类型后给"最终态"拍平，review 时肉眼可读。
- 调试价值二：交叉类型参与后续条件类型时常出现"整块匹配"的意外，拍平后语义更可预测。

```typescript
type Simplify<T> = { [K in keyof T]: T[K] } & {};

type Base = { id: number };
type Titled = { title: string };

type Model = Simplify<Readonly<Base> & Partial<Titled>>;
// hover 直接显示 { readonly id: number; readonly title?: string }
// 而不是 Readonly<Base> & Partial<Titled>

// 常用位置：公共 API 的返回类型、React Hook 返回值、工具类型库的"门面类型"
// 团队规范：工具类型出口处一律包一层 Simplify，代码评审成本大幅下降
```
