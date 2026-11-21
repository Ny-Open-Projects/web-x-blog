---
title: [V3-121] 大型 Vue3 项目目录如何组织（feature-first）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-121：大型 Vue3 项目目录如何组织（feature-first）？
**答**：
- 按文件类型横切（components/ 全堆一起）的痛点：一个需求要跨五六个目录改文件，模块边界全靠约定。
- feature-first：每个业务域一个目录，组件、composables、api、store 内聚在一起，域内改动不外溢。
- shared 放与业务无关的通用层，pages 只做组装不写逻辑。
- 关键纪律：feature 之间只允许 import 对方 `index.ts` 公共入口，否则边界很快腐化。

```typescript
// feature-first 目录结构（约定以注释形式给出）
// src/
//   app/                 —— 应用骨架：router、pinia、根布局、全局 provider
//   shared/              —— 与业务无关：ui 封装、utils、http client、hooks
//   features/
//     order/             —— 订单域，自包含
//       components/      —— 域内专属组件
//       composables/     —— 域内逻辑（useOrderList 等）
//       api/             —— 域内接口与类型
//       stores/          —— 域内 store（可选，跨页面共享才建）
//       index.ts         —— 公共出口，唯一允许被外部 import 的文件
//     user/
//       index.ts
//   pages/               —— 只做组装：从 features 取组件拼页面
//
// 纪律：features/order 之外的文件只能写
// import { OrderTable } from "@/features/order"; // 走 index.ts 出口
// 而不能 import "@/features/order/components/OrderTable.vue" // 禁止深挖内部

export {};
```
