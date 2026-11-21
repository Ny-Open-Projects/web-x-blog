---
title: [V3-244] 路由级异步组件与 Suspense 组合的完整方案是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-244：路由级异步组件与 Suspense 组合的完整方案是什么？
**答**：
- 两层异步：路由懒加载（`() => import()`，chunk 级）+ 页面 async setup（数据级），Suspense 统一兜底两者。
- 拆分策略：路由 chunk 用 Suspense 的 loadingComponent 显示"页面加载中"；数据请求放 async setup 并配合 defineAsyncComponent 的 delay 区分快慢。
- 与路由守卫协作：beforeEach 鉴权先于组件加载，避免"先渲染骨架再被踢回登录"的闪跳；数据预取可在守卫里 startTransition 式预热缓存。
- key 管理：`:key="route.fullPath"` 让同组件不同参数的页面重新走 Suspense pending（如详情页 id 切换）。
- 降级路径：异步 setup 抛错时用 onErrorCaptured 转 error 页面，并保留 retry 按钮重置 key。

```javascript
// router/index.ts
const routes = [
  {
    path: '/product/:id',
    component: () => import('./views/Product.vue'),   // chunk 懒加载
    props: (route) => ({ id: route.params.id }),
  },
];
// views/Product.vue（页面级 async setup）
export default defineComponent({
  props: ['id'],
  async setup(props) {
    const detail = ref(null);
    detail.value = await api.getProduct(props.id);    // Suspense 等待
    return () => h(ProductView, { detail: detail.value });
  },
});
// App.vue：<RouterView v-slot="{ Component }"><Suspense :key="routeKey"><component :is="Component"/></Suspense></RouterView>
```
