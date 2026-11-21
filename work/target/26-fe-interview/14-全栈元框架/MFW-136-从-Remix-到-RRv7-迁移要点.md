---
title: [MFW-136] 从 Remix v2 迁移到 React Router v7 的要点有哪些？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-136：从 Remix v2 迁移到 React Router v7 的要点有哪些？
**答**：
- 官方路径：`npx codemod remix/2->react-router/7` 自动迁移大部分——包名换成 `react-router`（单包），`@remix-run/node` 的工具进 `react-router`，Vite 插件换 `@react-router/dev/vite`。
- 配置变化：`remix.config.js` 并入 `react-router.config.ts`（更精简，ssr/prerender 等顶层）；文件路由变成 `routes.ts` 代码化配置（可选，保留 flatRoutes 约定有 helper）。
- 数据 API：`useLoaderData` 泛型写法换成 typegen 类型（`Route.ComponentProps`）；`json()`/`defer()` 工具废弃——直接返回对象/promise，框架自动处理。
- 风险点：`future` flags 开关依赖（v2 里提前开启的 flag 越多迁移越顺）；自定义 server 与 SSR 手动接管的部分要按新入口改写；测试里 mock 的 `@remix-run/*` 导入路径全要更新。

```ts
// 迁移前后对照（核心 diff）
// remix.config.js  ->  react-router.config.ts
//   { ssr: true }      { ssr: true } satisfies Config

// package.json
//   - "@remix-run/react" "@remix-run/node" "@remix-run/serve"
//   + "react-router" "@react-router/dev" "@react-router/serve"

// routes
//   app/routes/$productId.tsx          （文件约定）
//   -> routes.ts: route('products/:id', 'routes/product.tsx')（代码配置，可选保留约定）

// 数据
//   export const loader = () => json({ data })     // v2
//   export const loader = () => ({ data })         // v7：直接返回对象
//   const { data } = useLoaderData<typeof loader>()
//   -> ({ loaderData }: Route.ComponentProps)      // v7：typegen 类型
```
