---
title: [V3-255] Nuxt 3 的整体架构是怎样的？Nitro 引擎负责什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-255：Nuxt 3 的整体架构是怎样的？Nitro 引擎负责什么？
**答**：
- 三层：应用层（Vue 组件 + Nuxt composables）→ 引擎层（Nitro + Vite 构建编排）→ 平台层（Node/serverless/edge 部署目标）。
- Nitro 职责：服务器端运行时——聚合 server/api、server/routes、中间件，编译为可部署的 server bundle，支持多 preset（node/vercel/cloudflare/edge）。
- 渲染职责：Nitro 内嵌 Vue SSR 渲染器，处理 SSR/SSG/ISR/路由规则（routeRules 按 path 指定渲染模式与缓存）。
- 构建编排：Vite 负责客户端 bundle；Nitro 用 rollup 打服务端 bundle，两者由 Nuxt CLI 统一编排、共享 virtual modules（.nuxt 目录）。
- 面试钩子：能说出"routeRules 里 ssr:false / prerender / swr 缓存"的组合用法，说明真正用过。

```typescript
// nuxt.config.ts：同一项目混合渲染
export default defineNuxtConfig({
  routeRules: {
    '/': { prerender: true },              // 构建期静态生成
    '/products/**': { swr: 600 },          // ISR：600s 后台再生
    '/admin/**': { ssr: false },           // 纯 SPA
    '/api/**': { cors: true, headers: { 'cache-control': 's-maxage=60' } },
  },
  nitro: { preset: 'node-server' },        // 或 'vercel'/'cloudflare-pages'
});
// server/api/hello.get.ts → Nitro 自动注册 GET /api/hello
export default defineEventHandler((event) => ({ hello: 'world' }));
```
