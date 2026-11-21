---
title: [V3-055] Vue Router4 相比 Vue Router3 有哪些变化？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-055：Vue Router4 相比 Vue Router3 有哪些变化？
**答**：
- 创建方式改为 `createRouter()` 工厂函数，history 模式用 `createWebHistory()`。
- 新增动态路由管理：`addRoute/removeRoute/hasRoute`，removeRoute 需要 name。
- 守卫第三参数 next 变为可选，可以直接 return false 或路由地址完成控制。
- `*` 通配路由被移除，改用 `/:pathMatch(.*)*` 自定义正则；所有导航返回 Promise。

```typescript
// router/index.ts
import { createRouter, createWebHistory, createWebHashHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";

const routes: RouteRecordRaw[] = [
  { path: "/", component: () => import("../views/Home.vue") },
  { path: "/about", component: () => import("../views/About.vue") },
];

// Vue3 用工厂函数创建，不再支持 new Router()
const router = createRouter({
  history: createWebHistory(), // hash 模式用 createWebHashHistory()
  routes,
});

// 动态增删路由
router.addRoute({
  path: "/dynamic",
  name: "Dynamic",
  component: () => import("../views/Dynamic.vue"),
});
router.removeRoute("Dynamic"); // 按 name 移除

export default router;
```
