---
title: [MFW-126] React Router v7 是什么？framework mode 和 library mode 什么关系？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-126：React Router v7 是什么？framework mode 和 library mode 什么关系？
**答**：
- RRv7 把 Remix 吸收进 React Router：v7 = Remix 3 的内核。两种模式：**library mode**（`<BrowserRouter>` 老用法，v6 项目几乎无感升级）与 **framework mode**（Vite 插件 + `routes.ts` 配置 + loader/action + SSR/SSG 能力，即 Remix 的完整形态）。
- framework mode 的构成：`@react-router/dev` Vite 插件、路由模块约定（`loader`/`action`/`Component`/`ErrorBoundary`/`HydrateFallback`）、类型安全 typegen（`react-router typegen` 自动生成路由参数类型）。
- 与 Next 的定位差异：RRv7 不改 React 渲染模型（没有 RSC——截至当前版本），数据层是 loader/action + fetcher 的「web 标准」模式；Next 在往服务端组件化走。选择 RRv7 = 保留客户端 React 全量心智 + 框架级数据加载。
- 渐进升级路径是它的卖点：SPA 老项目可先升 v7 library mode，再逐步进 framework mode 拿 SSR。

```ts
// framework mode：react-router.config.ts
import type { Config } from '@react-router/dev/config';

export default {
  appDirectory: 'app',
  ssr: true,           // 可关掉变纯 SPA/SSG
  prerender: ['/about', '/pricing'], // 指定路径静态化
} satisfies Config;
```

```ts
// app/routes.ts —— 路由配置（代码化，替代文件约定）
import { type RouteConfig, index, route, layout } from '@react-router/dev/routes';

export default [
  index('routes/home.tsx'),
  route('products/:id', 'routes/product.tsx'),
  layout('routes/admin-layout.tsx', [
    route('admin/*', 'routes/admin.tsx'),
  ]),
] satisfies RouteConfig;
```
