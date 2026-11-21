---
title: [V3-088] Pinia 如何与路由联动实现登录态守卫？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-088：Pinia 如何与路由联动实现登录态守卫？
**答**：
- 全局守卫 beforeEach 里调用 `useUserStore()`：必须在 pinia 安装之后执行，守卫函数运行时调用即天然满足时序。
- 未登录访问受保护页：重定向登录页并携带 redirect 参数，登录成功后跳回原页面。
- 已登录但 profile 为空：先拉取用户信息再放行，防止刷新后身份信息缺失。
- 防死循环：登录页本身 requiresAuth 必须为 false。

```typescript
// router/guards.ts —— 登录态守卫
import { router } from "./index";
import { useUserStore } from "@/stores/modules/user";

router.beforeEach(async (to) => {
  const user = useUserStore(); // 守卫执行时 pinia 已安装，可安全调用

  // 1. 未登录访问受保护页面
  if (to.meta.requiresAuth && !user.token) {
    return { path: "/login", query: { redirect: to.fullPath } };
  }

  // 2. 已登录但刷新后缺少用户信息，先补拉
  if (user.token && !user.profile) {
    try {
      await user.fetchProfile();
    } catch {
      user.logout(); // token 失效则登出并回登录页
      return { path: "/login", query: { redirect: to.fullPath } };
    }
  }
  // 返回 undefined 或 true 表示放行
});

// 登录成功后的跳回逻辑（登录页里）：
// const redirect = route.query.redirect as string | undefined;
// router.replace(redirect ?? "/");
```
