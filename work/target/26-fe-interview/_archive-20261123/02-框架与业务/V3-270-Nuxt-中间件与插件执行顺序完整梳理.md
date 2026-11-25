---
title: [V3-270] Nuxt 中间件、插件与生命周期的执行顺序完整梳理
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-270：Nuxt 中间件、插件与生命周期的执行顺序完整梳理
**答**：
- 服务端一次请求的顺序：Nitro 收请求 → server middleware（Nitro 层，`server/middleware/`）→ Nuxt 插件（plugins/，SSR 先跑）→ 全局路由中间件 → 页面中间件 → async setup（useAsyncData）→ renderToString → payload 注入。
- 客户端首次：payload 恢复 → 插件（client）→ 路由中间件 → hydration（不重跑 async setup）→ mounted。
- 插件顺序：文件名数字前缀（`01.auth.ts`），`.server.ts/.client.ts` 限定端；插件里可 `provide` 注入 NuxtApp。
- 容易答错的点：全局中间件在插件**之后**执行；async setup 在中间件**之后**、渲染之前执行；mounted 只在客户端。
- 排错应用：鉴权逻辑放中间件（可重定向），全局错误上报放插件（最早且两端都跑），DOM 相关只能 onMounted。

```typescript
// 顺序验证用例（vconsole 输出）
// plugins/01.log.ts
export default defineNuxtPlugin((nuxtApp) => {
  console.log('[1] plugin');
  nuxtApp.hook('app:created', () => console.log('[2] app:created'));
  nuxtApp.hook('page:finish', () => console.log('[6] page:finish'));
});
// middleware/log.global.ts
export default defineNuxtRouteMiddleware(() => console.log('[3] middleware'));
// pages/index.vue
// await useAsyncData(() => console.log('[4] async setup (SSR 执行/客户端跳过)'))
// onMounted(() => console.log('[5] mounted (仅客户端)'))
```
