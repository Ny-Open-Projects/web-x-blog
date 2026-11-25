---
title: [MFW-524] App Router 文件约定：目录结构到编译产物的映射规则
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-524：App Router 文件约定：目录到产物的映射

**答**:
- 文件约定 = DSL：page/layout/route/loading/error/not-found/template/default——编译器把目录树转成「路由段树」：每段一个 bundle（段级代码分割 RBL-596 的目录版）+ 组件树（layout 嵌套包裹）；loading.js = 自动 Suspense 边界；error.js = 自动 error boundary。
- 段级 bundle 的意义：路由切换只加载新段（layout 复用——payload diff 只传变化的段 RBL-14 目录段级导航）；「段 = 缓存与加载的单元」。
- 私有约定：_folder（不路由）、(group)（路由分组不进 URL）、@slot（平行路由）——目录命名即配置（零配置 DSL 的极致 RBL-953）。
- 编译器的隐式行为清单（出错排查的关键）：page.js 缺失 → 该段只有布局无叶子（404）；route.js 与 page.js 同段冲突（编译错误）；layout 不重挂（导航保留状态）——template.js 才每次重挂。
- 追问钩子：为什么文件约定比配置式路由（routes 数组）更适合元框架？——文件系统即「意图的物理呈现」：目录树 = 路由树（可视化导航/移动即改路由）；配置式集中声明（大项目数百行 routes 文件——review 与冲突合并难）；「约定优于配置」的深层价值是「结构可发现性」——新人看目录即懂架构（与 RBL-677 共享配置的收敛哲学互补：约定收敛结构、preset 收敛行为）。

```javascript
// 目录树 → 路由段树
// app/
// ├── layout.tsx           → 根布局（所有段共享）
// ├── shop/
// │   ├── layout.tsx       → /shop/* 共享布局
// │   ├── page.tsx         → /shop
// │   ├── loading.tsx      → /shop 段级 Suspense
// │   ├── [id]/
// │   │   ├── page.tsx     → /shop/:id
// │   │   └── error.tsx    → 段级错误边界
// │   └── @modal/          → 平行路由（@slot 不进 URL）
// │       └── default.tsx
// └── api/
//     └── route.ts          → /api handler（无 UI 段）
// 编译产物：每段一个 bundle + 段树 payload
// 路由切换 /shop → /shop/123：只加载 [id] 段 bundle，layout 不重挂
```
