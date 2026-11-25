---
title: [MFW-076] Nuxt 4 是什么？目录结构相比 Nuxt 3 有什么变化？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-076：Nuxt 4 是什么？目录结构相比 Nuxt 3 有什么变化？
**答**：
- Nuxt 4 是 Vue 生态的全栈元框架（Nuxt 3 架构的延续优化），核心能力同源：文件路由、SSR/SSG/混合渲染、auto-import、Nitro 服务端、`useFetch` 数据层。
- 最大变化是**新的 `app/` 源码目录**：`pages/`、`components/`、`composables/`、`layouts/` 等全部收进 `app/`，与 `server/`（Nitro 服务端）、`public/`、`content/` 平级，IDE 类型感知更快、职责更清晰。
- 数据层升级：`useFetch/useAsyncData` 默认共享 payload 去重，类型推断更严格；`app.config.ts` 与运行时 config 分离更明确。
- 兼容性：Nuxt 3 目录结构在 4 中向后兼容（可配置 `future.compatibilityVersion` 渐进迁移），不是推倒重来。

```
nuxt4-app/
├── app/                 # 新：浏览器 + SSR 共享的源码目录
│   ├── pages/           # 文件路由
│   ├── components/
│   ├── composables/
│   ├── layouts/
│   └── app.vue
├── server/              # Nitro 服务端：API、middleware、tasks
│   ├── api/
│   └── middleware/
├── public/
├── content/             # Nuxt Content 内容目录
├── nuxt.config.ts
└── shared/              # 新：SSR 与 server 两侧共享的类型/工具
```

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  future: { compatibilityVersion: 4 }, // Nuxt 3.12+ 开启 4 行为
  ssr: true,
  routeRules: {                        // 混合渲染：每条路由独立策略
    '/': { isr: 600 },                 // ISR
    '/admin/**': { ssr: false },       // 后台走 CSR
    '/api/**': { cors: true },
  },
});
```
