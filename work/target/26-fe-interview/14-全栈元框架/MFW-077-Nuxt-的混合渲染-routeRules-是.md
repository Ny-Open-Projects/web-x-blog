---
title: [MFW-077] Nuxt 的混合渲染（hybrid rendering）和 routeRules 是怎么工作的？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-077：Nuxt 的混合渲染（hybrid rendering）和 routeRules 是怎么工作的？
**答**：
- routeRules 允许**同一应用按路由粒度选择渲染策略**：`ssr: false`（CSR）、`static`（构建期预渲染）、`isr`/`swr`（服务端缓存+再验证）、`prerender`、`headers`/`redirect`/`proxy`。这在 Next 里要靠每页 export 配置 + 中间件拼出来，Nuxt 是一张表搞定。
- `swr`：首个请求渲染后缓存，后续直接回缓存，过期后 stale-while-revalidate；`isr` 类似但带主动过期窗口。都由底层 Nitro 的缓存引擎实现，缓存层可插拔（内存/Redis/CDN）。
- 与 Nitro 的关系：routeRules 不只是 Next 层的约定，会下沉为 Nitro 路由层配置，所以无论部署到 Vercel/Cloudflare/Node 都有一致的语义——这是「一次配置，多端部署」的核心。
- 实战要点：后台路由 `ssr:false` 甩掉服务端成本；营销落地页 `prerender` 秒开；列表页 `swr` 挡洪峰。

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  routeRules: {
    '/':                    { prerender: true },            // 构建期出静态 HTML
    '/products/**':         { swr: 600, maxAge: 60 },       // 缓存 10min，SWR 再验证
    '/news/**':             { isr: 300 },                   // 定时增量再生
    '/account/**':          { ssr: false },                 // 登录后页面：纯 CSR
    '/old-promo':           { redirect: { to: '/promo', statusCode: 302 } },
    '/api/cdn-proxy/**':    { proxy: 'https://cdn.example.com/**' },
    '/downloads/**':        { headers: { 'cache-control': 'public, max-age=86400' } },
  },
});
```

```vue
<!-- app/pages/products/[id].vue —— 组件无需关心渲染策略，数据层自动适配 -->
<script setup lang="ts">
const route = useRoute();
const { data: product, error } = await useFetch(`/api/products/${route.params.id}`, {
  key: `product-${route.params.id}`, // 显式 key 保证去重与复水一致
});
if (error.value) throw createError({ statusCode: 404, statusMessage: '商品不存在' });
</script>

<template>
  <h1>{{ product?.name }}</h1>
  <p>¥{{ product?.price }}</p>
</template>
```
