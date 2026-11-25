---
title: [MFW-094] Nuxt 应用怎么部署到不同目标？preset 机制是什么？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-094：Nuxt 应用怎么部署到不同目标？preset 机制是什么？
**答**：
- Nitro 按 preset 把同一份代码编译成不同目标的产物：`node-server`（默认，自托管）、`static`（纯静态）、`vercel`/`netlify`/`cloudflare`/`aws-lambda` 等，通过环境变量 `NITRO_PRESET` 或配置切换——业务代码零修改。
- 自托管 K8s：用 node-server preset + 容器化，产物是普通 Node 服务，健康检查走 `/api/_health`（自定义）。
- 静态托管：`ssr: false` 或全 prerender 时用 static preset，产物直接扔 CDN/OSS。
- 环境差异点要显式处理：Edge preset 下不能依赖 Node API；storage 驱动按目标换（本地 FS → Redis/S3）；cookie/签名密钥走运行时 env。

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  nitro: {
    preset: process.env.NITRO_PRESET ?? 'node-server',
    storage: {
      cache: process.env.REDIS_URL
        ? { driver: 'redis', url: process.env.REDIS_URL }   // 线上：Redis 缓存层
        : { driver: 'memory' },                              // 本地：内存
    },
  },
  routeRules: { '/**': { swr: 600 } },
});
```

```dockerfile
# Dockerfile（node-server preset）
FROM node:20-alpine AS build
WORKDIR /app
COPY . .
RUN npm ci && npm run build   # 产出 .output/（自包含，含 node_modules 最小集）

FROM node:20-alpine
WORKDIR /app
COPY --from=build /app/.output ./.output
ENV PORT=3000
EXPOSE 3000
CMD ["node", ".output/server/index.mjs"]
```
