---
title: [V3-096] 路由懒加载如何做 hover 预取？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-096：路由懒加载如何做 hover 预取？
**答**：
- 懒加载组件首次导航才加载，网络慢时会白屏；hover 到导航项时预加载组件模块，点击时已就绪。
- 预取即提前调用组件的 import 函数，模块加载结果由浏览器缓存，真正导航时同一 promise 直接复用。
- 封装 usePrefetch：内部 Set 防重复，失败从 Set 移除允许重试。
- 菜单渲染时把“加载函数”与路径绑定，RouterLink 的 mouseenter 触发预取。

```typescript
// composables/usePrefetch.ts
const prefetched = new Set<string>();

export function createPrefetch(key: string, load: () => Promise<unknown>) {
  return () => {
    if (prefetched.has(key)) return; // 已预取过，跳过
    prefetched.add(key);
    load().catch(() => prefetched.delete(key)); // 失败允许下次重试
  };
}

// 菜单组件里配合 RouterLink 使用：
// <RouterLink
//   v-for="item in menu"
//   :key="item.path"
//   :to="item.path"
//   @mouseenter="createPrefetch(item.path, item.load)"
// >
//   {{ item.label }}
// </RouterLink>
//
// menu 数据来源示例：
// const menu = [
//   { path: "/order", label: "订单", load: () => import("@/views/Order.vue") },
//   { path: "/user", label: "用户", load: () => import("@/views/User.vue") },
// ];
//
// 也可在浏览器空闲时兜底全量预取：
// const idle = window.requestIdleCallback ?? ((cb) => setTimeout(cb, 200));
// idle(() => menu.forEach((m) => createPrefetch(m.path, m.load)()));
```
