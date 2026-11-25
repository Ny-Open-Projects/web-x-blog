---
title: [MFW-082] Nuxt 的 route middleware 和 Vue Router 导航守卫有什么区别？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-082：Nuxt 的 route middleware 和 Vue Router 导航守卫有什么区别？
**答**：
- Nuxt route middleware 本质上基于 Vue Router 守卫实现，但补充了 SSR 语境：守卫代码在**服务端渲染时也要执行**（跳转用 `navigateTo` 而不是 `router.push`），并且能访问 `useRequestEvent`、`setResponseStatus` 等服务端能力。
- 三种放置方式：`middleware/*.ts` 命名式（defineNuxtRouteMiddleware）、页面内 `definePageMeta({ middleware })` 内联、`app.vue` 级全局。全局命名式无需注册自动生效。
- 与 Nitro server middleware 分工：route middleware 管「页面导航」（登录态、权限、埋点），Nitro middleware 管「所有进入 server 的请求」（API 鉴权、CORS）——两层都在，别搞混。
- 语义约定：直接 return（放行）、`return navigateTo('/login')` 重定向、`return abortNavigation()` 中止（可带错误）。

```ts
// middleware/auth.global.ts —— 全局：未登录访问受限页跳登录
export default defineNuxtRouteMiddleware((to, from) => {
  const user = useUserState(); // SSR 安全的登录态（cookie 复水）
  const PUBLIC = new Set(['/login', '/register', '/']);

  if (PUBLIC.has(to.path)) return;

  if (!user.value) {
    // SSR 里是 302 响应，客户端是路由跳转——同一个 API 两种语义
    return navigateTo(`/login?redirect=${encodeURIComponent(to.fullPath)}`);
  }
  if (to.path.startsWith('/admin') && !user.value.isAdmin) {
    return abortNavigation(createError({ statusCode: 403, statusMessage: '无权限' }));
  }
});
```

```vue
<!-- 页面级：内联中间件 + 页面元信息 -->
<script setup lang="ts">
definePageMeta({
  middleware: [
    function (to) {
      if (!to.params.id) return abortNavigation('缺少商品 id');
    },
  ],
  layout: 'product',
});
</script>
```
