---
title: [MFW-148] TanStack Start 怎么部署？和 Nuxt 的 Nitro 什么关系？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-148：TanStack Start 怎么部署？和 Nuxt 的 Nitro 什么关系？
**答**：
- TanStack Start 的服务端层直接构建在 **Nitro** 之上（unjs 生态）：一份代码经 preset 编译到 Node/Cloudflare/Vercel/Netlify 等——和 Nuxt 共享同一部署引擎，这就是「元框架部署层趋同」的实例。
- 部署姿势：`vite.config` 里通过 `tanstackStart({ target: 'vercel' })` 或环境变量指定 preset；自托管 K8s 用 node preset + Docker。
- SSR 与 API：server functions 编译为 Nitro 路由；静态资源照常 CDN。`ssr: false` 时 server functions 仍保留（纯 API 服务）。
- 与 Next 部署对比：Next 自托管要 standalone/OpenNext 桥接，Nitro 系（Nuxt/Start）天生多目标——这是面试里「自托管选型」的实用论据。

```ts
// vite.config.ts
import { defineConfig } from 'vite';
import tsConfigPaths from 'vite-tsconfig-paths';
import { tanstackStart } from '@tanstack/react-start/plugin/vite';

export default defineConfig({
  plugins: [
    tsConfigPaths(),
    tanstackStart({
      target: process.env.DEPLOY_TARGET ?? 'cloudflare-module', // preset 切换
      customViteReactPlugin: true,
    }),
    viteReact(),
  ],
});
```

```toml
# wrangler.toml —— Cloudflare 部署示例（cloudflare-module preset）
name = "my-start-app"
main = "dist/_worker.js/index.js"
compatibility_date = "2026-01-01"

[vars]
DATABASE_URL = "https://db.example.com" # Edge 上用 HTTP 驱动
```
