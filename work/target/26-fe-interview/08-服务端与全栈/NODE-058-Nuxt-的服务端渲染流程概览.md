---
title: [NODE-058] Nuxt 的服务端渲染流程概览？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-058：Nuxt 的服务端渲染流程概览？
**答**：
- Nuxt（Vue 生态）SSR 流程：请求 → Nitro 服务端引擎路由匹配 → 执行 `setup`/`useAsyncData`/`useFetch`（服务端执行一次，payload 序列化）→ Vue `renderToString` 输出 HTML + payload 注入 → 客户端 hydrate 并**复用服务端已取的数据**（不重复请求）。
- 与 Next 差异：Next 18 后主推 RSC（服务端组件，数据在组件内直接 await）；Nuxt 是组合式 API + `useAsyncData` 显式声明数据依赖（key 化，跨端幂等）。Nitro 统一了 dev/SSR/SSG/边缘部署（可部署到 Vercel/CF Workers）。
- 服务端要点：`payload` 传输（防重复请求）、`routeRules` 按路由配置 SSR/ISR/CSR、错误页 `error.vue` 与 SSR 错误码。

```javascript
// nuxt.config.ts：按路由的渲染策略
export default defineNuxtConfig({
  routeRules: {
    '/':            { swr: 300 },               // 首页：stale-while-revalidate
    '/docs/**':     { isr: 600 },               // 文档：增量再生
    '/account/**':  { ssr: false },             // 个人中心：纯 CSR（个性化强）
    '/api/**':      { cors: true },             // Nitro 直接托管 API
  },
  nitro: { compressPublicAssets: true },
});
```

```vue
<!-- pages/products/[id].vue -->
<script setup>
const route = useRoute();
// useAsyncData：服务端执行一次，payload 序列化传给客户端，hydration 时不再请求
const { data: product, error } = await useAsyncData(
  `product-${route.params.id}`,                       // key：去重与缓存依据
  () => $fetch(`/api/product/${route.params.id}`),
  { server: true, lazy: false, timeout: 3000 },
);
if (error.value) throw createError({ statusCode: 404, statusMessage: '商品不存在' });
useHead({ title: () => product.value.title });        // SEO meta
</script>
```

---

## 九、工程与部署
