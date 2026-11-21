---
title: [TS-166] 第三方无类型资产（*.vue、图片、CSS Modules）如何快速补类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-166：第三方无类型资产（*.vue、图片、CSS Modules）如何快速补类型？
**答**：
- 通配符 ambient module：`declare module "*.png"` 一条声明覆盖一类文件。
- *.vue 用 DefineComponent 兜底；CSS Modules 用只读字符串索引签名。
- 注意 vite/client 已内置常见资产声明，重复声明反而冲突。

```typescript
// types/modules.d.ts
declare module "*.vue" {
  import type { DefineComponent } from "vue";
  const component: DefineComponent<Record<string, unknown>, Record<string, unknown>, unknown>;
  export default component;
}

declare module "*.png" {
  const src: string;
  export default src;
}

declare module "*.module.css" {
  const classes: { readonly [key: string]: string };
  export default classes;
}

// 用法：
// import logo from "./logo.png";        // logo: string
// import styles from "./a.module.css";  // styles.a: string（只读）
// Vite 项目优先 /// <reference types="vite/client" />，已内置大部分资产声明
```
