---
title: [V3-258] Nuxt 的路由、layouts 与中间件机制是怎样的？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-258：Nuxt 的路由、layouts 与中间件机制是怎样的？
**答**：
- 文件路由：`pages/` 目录结构直接生成 vue-router 路由表（动态 `[id].vue`、嵌套目录、`definePageMeta` 补充配置），构建期生成 `.nuxt/routes`。
- layouts：`layouts/default.vue` 放公共骨架（header/footer），页面用 `definePageMeta({ layout: 'admin' })` 切换；`<NuxtLayout>` 包 `<NuxtPage>`。
- 中间件：`middleware/` 下命名中间件 + 页面级 `definePageMeta({ middleware: 'auth' })`，执行时机在路由切换前（SSR 与客户端都会跑），可返回 `navigateTo` 重定向。
- 路由规则：`routeRules` 按 path 配置渲染模式/重定向/缓存，与文件路由互补。
- 与 vue-router 关系：Nuxt 是 Router4 的上层封装，守卫能力有限，复杂守卫逻辑放中间件或插件里注册原生 beforeEach。

```typescript
// middleware/auth.global.ts
export default defineNuxtRouteMiddleware((to) => {
  const user = useUserStore();
  if (to.path.startsWith('/admin') && !user.token) {
    return navigateTo('/login?redirect=' + encodeURIComponent(to.fullPath));
  }
});
// pages/admin/[id].vue
definePageMeta({ layout: 'admin', middleware: ['audit-log'], keepalive: true });
// plugins/router.ts：需要原生守卫时
// nuxtApp.hook('vue-router:beforeEach', (to, from) => {...})
```
