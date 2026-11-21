---
title: [TS-169] export type / export type * 等导出策略有什么讲究？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-169：export type / export type * 等导出策略有什么讲究？
**答**：
- isolatedModules 下 `export { SomeType }` 报错 1205：转译器无法判断它是类型，必须 `export type`。
- `export *` 会把类型一并转发；只转发类型用 `export type *`（TS 5.0+）。
- `export * from` 保留模块的运行时副作用（顶层注册代码），纯类型模块用 export type * 避免误引入。

```typescript
// types.ts
export interface User { id: number }
export const makeUser = (): User => ({ id: 1 });

// index.ts —— 导出策略
// ❌ export { User };              // isolatedModules 报错 1205
export type { User };              // ✅ 显式声明"这是类型"
export { makeUser } from "./types";

export type * from "./types";      // 只转发类型（TS 5.0+）
export * from "./utils";           // 值 + 类型一起转发

// 副作用提示：export * from "./side-effect" 会保留顶层注册代码（如组件注册、polyfill），
// 摇树优化不保证剔除；纯类型入口务必 export type *
```

## 第三十五章 类型安全的状态与路由（TS-170 ~ TS-175）
