---
title: [MFW-180] RRv7 的 routes.ts 配置式路由和 Next 文件约定怎么对比？
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-180：RRv7 的 routes.ts 配置式路由和 Next 的文件约定路由怎么对比？
**答**：
- Next App Router：**目录即路由**，文件名约定（page/layout/loading/error/route）决定行为，零配置上手快；代价是路由结构被文件系统锁死，跨层调整目录会牵连 URL。
- RRv7 framework mode：`routes.ts` 显式声明路由树（可编程生成），文件放哪与 URL 解耦——一个 route module 可以挂到任意路径，路由树可以由代码/约定生成器批量产出。
- 配置式的优势：动态生成路由（读 CMS 目录生成 200 条路由）、路由分组重构不影响 URL、能对路由树做类型推导与权限矩阵集中声明。
- 文件约定的优势：新人零学习成本、约定即文档、框架对每段文件的编译期优化（Next 的段级缓存边界）依赖这一套。
- 实战折衷：大团队在 Next 里也常用 route group + 中间件模拟「路由树集中管理」；RRv7 团队则用 helper 函数生成 routes.ts 保持一致性。

```javascript
// RRv7 app/routes.ts —— 显式路由树，可编程生成
import { type RouteConfig, index, route, prefix } from '@react-router/dev/routes';

export default [
  index('home.tsx'),
  route('products/:id', 'product.tsx', [
    index('product-detail.tsx'),
    route('reviews', 'product-reviews.tsx'),
  ]),
  ...prefix('admin', [ // 批量生成后台路由
    route('dashboard', 'admin/dashboard.tsx', { middleware: [requireAdmin] }),
  ]),
] satisfies RouteConfig;
```