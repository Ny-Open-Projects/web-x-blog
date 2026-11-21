---
title: [V3-119] Nuxt3 的目录约定与渲染模式切换（ssr:false 路由）怎么做？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-119：Nuxt3 的目录约定与渲染模式切换（ssr:false 路由）怎么做？
**答**：
- 约定即配置：pages 文件路由、composables/ 自动导入、components/ 自动注册、server/api 服务端接口、middleware/ 路由中间件。
- 渲染模式用 routeRules 按路由粒度声明：`ssr: false` 纯客户端、`prerender` 构建期预渲染、`swr` 边缘缓存再生成。
- 后台管理这类无 SEO 需求的页面设 ssr: false，免掉 hydration 与服务端兼容成本。
- 单个组件也可用 `<ClientOnly>` 局部关闭服务端渲染。

```typescript
// nuxt.config.ts —— 按路由粒度声明渲染模式
export default defineNuxtConfig({
  routeRules: {
    "/": { prerender: true }, // 首页：构建期预渲染成静态 HTML
    "/products/**": { swr: 600 }, // 商品页：缓存 600 秒，过期后台再生
    "/admin/**": { ssr: false }, // 后台管理：纯客户端渲染，无 SEO 需求
    "/api/**": { cors: true }, // server/api 接口
  },
});

// 目录约定（约定即配置，无需手写路由表）：
// pages/index.vue           ->  /
// pages/products/[id].vue   ->  /products/:id（动态路由）
// composables/useXxx.ts     ->  自动导入
// components/BaseButton.vue ->  模板直接用 <BaseButton />
// server/api/hello.get.ts   ->  GET /api/hello
// middleware/auth.ts        ->  路由中间件
```
