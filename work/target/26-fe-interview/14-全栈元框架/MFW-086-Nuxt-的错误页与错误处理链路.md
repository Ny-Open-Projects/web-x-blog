---
title: [MFW-086] Nuxt 的错误处理链路是什么？createError 和 error 页怎么配合？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-086：Nuxt 的错误处理链路是什么？createError 和 error 页怎么配合？
**答**：
- 两个来源：**SSR 期错误**（组件 setup、useFetch 后手动 throw createError fatal）直接渲染 `error.vue`；**客户端运行时错误**先经 Vue onErrorCaptured/Nuxt 的 `vue:error` 钩子，未捕获则同样落到 error.vue。
- `createError({ statusCode, statusMessage, fatal })`：fatal=true 才整页切换错误视图；非 fatal 可在页面内局部消化。SSR 抛 4xx/5xx 会设置真实 HTTP 状态码（SEO 和监控都依赖这一点）。
- 服务端 API 错误：`server/api` 里 throw createError 会变成带 status 的响应体；前端要检查 `error.value` 再决定局部提示还是整页 404。
- 兜底三件套：`nuxt.config` 的 `nitro.onError`/`devErrorHandler` 上报 APM；error.vue 里给「回首页」按钮并上报；全局 `onError` 打日志防止静默白屏。

```vue
<!-- app/error.vue —— 必须放在 pages 之外；处理完给逃生通道 -->
<script setup lang="ts">
import type { NuxtError } from '#app';
const props = defineProps<{ error: NuxtError }>();

// 上报后提供重置入口：跳转或清错误重渲染
const goHome = () => clearError({ redirect: '/' });
</script>

<template>
  <div>
    <h1>{{ error.statusCode === 404 ? '页面不存在' : '服务开小差了' }}</h1>
    <p>{{ error.statusMessage }}</p>
    <button @click="goHome">回首页</button>
  </div>
</template>
```

```ts
// server/api/products/[id].get.ts —— 服务端错误标准化
export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id');
  const product = await db.product.findUnique({ where: { id } });
  if (!product) {
    throw createError({ statusCode: 404, statusMessage: 'Product Not Found', fatal: true });
  }
  return product;
});
```

```ts
// nuxt.config.ts —— 全局钩子
export default defineNuxtConfig({
  hooks: {
    'nitro:error': (error, { event }) => apm.capture(error, { path: event.path }),
  },
});
```
