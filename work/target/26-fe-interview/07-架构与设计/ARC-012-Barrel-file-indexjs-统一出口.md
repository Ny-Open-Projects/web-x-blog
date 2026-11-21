---
title: [ARC-012] Barrel file（index.js 统一出口）有什么利弊？如何取舍？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-012：Barrel file（index.js 统一出口）有什么利弊？如何取舍？
**答**：
- 利：模块边界清晰，调用方不感知内部结构，重构内部目录不影响外部。
- 弊：大型库会拖慢构建（所有模块被编译进依赖图）、可能破坏 tree-shaking（有副作用声明时）、容易造成循环依赖。
- 取舍：业务代码 feature 用 barrel；高.payload性能敏感的 npm 包用显式深路径 + exports 映射，慎用 barrel。

```typescript
// src/features/cart/index.ts —— 只暴露公共 API，内部实现不外泄
export { CartProvider } from './provider';
export { useCart } from './hooks/useCart';
export type { CartItem } from './types';
// 禁止：export * —— 会把内部工具/未稳定 API 全部泄漏成"事实公共接口"

// 高性能 npm 包则放弃 barrel，用 exports 精确映射利于 tree-shaking：
// package.json
// "exports": {
//   "./button": { "types": "./es/button.d.ts", "import": "./es/button.js" },
//   "./table":  { "types": "./es/table.d.ts",  "import": "./es/table.js" }
// }
```
