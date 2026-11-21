---
title: [V3-268] Nuxt 部署 preset（Node/Serverless/Edge）各有什么差异与限制？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-268：Nuxt 部署 preset（Node/Serverless/Edge）各有什么差异与限制？
**答**：
- node-server：传统部署，能力最全（长连接、文件系统、连接池、大内存），适合自建 K8s。
- serverless（Vercel/Netlify）：函数级扩缩容，冷启动敏感；限制：无持久文件系统、执行时长/内存上限、数据库连接池失效（用 HTTP DB 或连接器）。
- edge（Cloudflare Workers）：全球低延迟，但**运行时不是 Node**——不能用的 API：fs、部分 node:crypto、动态 require（Nuxt 的 unenv/nitropack 做了 polyfill 映射）。
- 选型依据：SSR 吞吐要求高/重接口聚合选 Node；内容站全球分发选 edge；突发流量选 serverless。
- 迁移检查清单：动态 import、原生模块、环境变量读取方式（`useRuntimeConfig` 统一）、缓存（内存 LRU 在无状态函数下失效，改 KV/Redis）。

```typescript
export default defineNuxtConfig({
  nitro: {
    preset: 'cloudflare-pages',                  // 或 'node-server' / 'vercel'
    storage: { cache: { driver: 'cloudflare-kv' } }, // 边缘无内存缓存，用 KV
  },
  runtimeConfig: {
    apiBase: '',            // 服务端私有：process.env.NUXT_API_BASE 注入
    public: { cdn: 'https://cdn.example.com' },
  },
});
// edge 不兼容示例：import { readFileSync } from 'node:fs' ❌ → 改 HTTP 资源或构建期内联
```
