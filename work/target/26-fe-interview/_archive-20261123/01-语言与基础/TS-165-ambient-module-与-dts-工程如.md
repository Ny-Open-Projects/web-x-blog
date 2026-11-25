---
title: [TS-165] ambient module 与 d.ts 工程如何组织 types 目录？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-165：ambient module 与 d.ts 工程如何组织 types 目录？
**答**：
- 分层：global.d.ts（全局环境）、modules.d.ts（通配符资产）、vendor/（第三方补丁）、index.d.ts（barrel 汇总）。
- barrel 用三斜线引用串起来，tsconfig include 收进编译范围。
- `types: []` 清空 @types 自动加载后，所需三方全局类型要显式 reference。

```typescript
// types/index.d.ts —— barrel 汇总
/// <reference path="./global.d.ts" />
/// <reference path="./modules.d.ts" />
/// <reference path="./vendor/vue-router.d.ts" />

// tsconfig.json 配合
// {
//   "compilerOptions": { "types": [] },
//   "include": ["src", "types"]
// }

// 组织原则：
// 1. 全局声明文件内不得有 import/export（否则变模块私有，失去全局合并能力）
// 2. vendor 补丁集中管理并注明上游版本，升级依赖时逐一核对
// 3. 业务类型不放全局，走模块导入，避免命名污染
```
