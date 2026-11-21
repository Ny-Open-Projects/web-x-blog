---
title: [V3-060] 动态路由匹配与 scrollBehavior、meta 怎么使用？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-060：动态路由匹配与 scrollBehavior、meta 怎么使用？
**答**：
- 动态参数 `:id` 通过 `route.params` 读取；可用正则约束如 `:id(\\d+)`。
- Vue Router4 移除 `*` 通配，兜底用 `/:pathMatch(.*)*`。
- meta 存放路由元信息（标题、权限），配合守卫与 afterEach 做鉴权和标题设置。
- scrollBehavior 支持保存位置、锚点定位、平滑滚动。

```typescript
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    // 动态参数：/user/123 -> params.id = "123"
    { path: "/user/:id", component: () => import("../views/User.vue") },
    // 正则约束：只有数字才匹配
    { path: "/post/:id(\\d+)", component: () => import("../views/Post.vue") },
    // 兜底路由（Router4 不再支持 * 通配）
    { path: "/:pathMatch(.*)*", component: () => import("../views/NotFound.vue") },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition; // 浏览器前进后退保持位置
    if (to.hash) return { el: to.hash, behavior: "smooth" }; // 锚点定位
    return { top: 0 };
  },
});

// meta 上存元信息，配合守卫做鉴权、埋点、标题设置
router.afterEach((to) => {
  document.title = (to.meta.title as string) ?? "默认标题";
});
```

## 第十六章 性能优化
