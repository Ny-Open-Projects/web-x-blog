---
title: [V3-093] 路由元信息 meta 有哪些工程化用法？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-093：路由元信息 meta 有哪些工程化用法？
**答**：
- 三大高频用途：设置 document.title、声明权限角色、标记 keep-alive 缓存白名单。
- 先做 `RouteMeta` 接口扩充，meta 字段获得类型提示，避免裸操作 any。
- 逻辑集中在全局守卫统一消费 meta，路由配置保持纯声明。
- keep-alive 的 include 缓存池由 meta.keepAlive 驱动：进入时加入缓存名单，关闭 tab 时移除。

```typescript
// router/meta.d.ts —— 先扩充 meta 类型，获得编译期检查
import "vue-router";

declare module "vue-router" {
  interface RouteMeta {
    title?: string;
    roles?: string[]; // 允许访问的角色
    keepAlive?: boolean; // 是否进入缓存池
    requiresAuth?: boolean;
  }
}

// router/guards.ts —— 守卫统一消费 meta
import { router } from "./index";
import { useUserStore } from "@/stores/modules/user";
import { useTabsStore } from "@/stores/modules/tabs";

router.beforeEach((to) => {
  // 1. 页面标题
  document.title = to.meta.title ? `${to.meta.title} - 管理后台` : "管理后台";

  // 2. 角色权限
  if (to.meta.roles && !to.meta.roles.includes(useUserStore().role)) {
    return { name: "403" };
  }

  // 3. 进入缓存池：KeepAlive 的 include 由 tabs store 维护
  if (to.meta.keepAlive && to.name) {
    useTabsStore().add({ name: String(to.name), path: to.path, title: to.meta.title ?? "" });
  }
});

// 路由声明示例：
// { path: "/order", name: "Order", component: () => import("@/views/Order.vue"),
//   meta: { title: "订单管理", roles: ["admin", "operator"], keepAlive: true } }
```
