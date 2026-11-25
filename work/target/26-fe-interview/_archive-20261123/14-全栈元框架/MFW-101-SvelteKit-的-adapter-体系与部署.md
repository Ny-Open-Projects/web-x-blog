---
title: [MFW-101] SvelteKit 的 adapter 体系是什么？各 adapter 适合什么场景？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-101：SvelteKit 的 adapter 体系是什么？各 adapter 适合什么场景？
**答**：
- adapter 是「产物适配层」：把 SvelteKit 编译出的中间表示转成目标平台的入口。与 Nuxt preset、Next 的 standalone/OpenNext 同类，但 SvelteKit 把它作为核心抽象暴露得更早更明确。
- `adapter-auto`（默认）：检测部署环境自动选；`adapter-node`：自托管/K8s/Docker；`adapter-static`：纯 SSG，要求全站可预渲染；`adapter-cloudflare/vercel/netlify`：对应 serverless/edge。
- 约束关系：用 `adapter-static` 时所有路由必须可 prerender（动态路由要给 `entries`），不能有依赖请求时机的 server load。
- 运行时差异：adapter-node 输出 `build/index.js` 直接 `node build`；serverless adapter 产出各平台函数格式，`prerender` 部分始终是纯静态文件。

```js
// svelte.config.js
import adapter from '@sveltejs/adapter-node';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

export default {
  preprocess: vitePreprocess(),
  kit: {
    adapter: adapter({
      // 环境变量在运行时通过 .env / env 动态读取（node adapter 支持）
      precompress: true,   // 生成 .br/.gz 预压缩文件
      polyfillNode: false,
    }),
    prerender: {
      handleHttpError: 'fail', // 预渲染期间遇到 404 链接直接构建失败
    },
  },
};
```

```dockerfile
# Dockerfile（adapter-node）
FROM node:20-alpine
WORKDIR /app
COPY build ./build          # adapter-node 产物是自包含 build/ 目录
COPY node_modules ./node_modules
ENV PORT=3000 ORIGIN=https://shop.example.com  # ORIGIN 必须设，防 form/host 校验失败
CMD ["node", "build"]
```
