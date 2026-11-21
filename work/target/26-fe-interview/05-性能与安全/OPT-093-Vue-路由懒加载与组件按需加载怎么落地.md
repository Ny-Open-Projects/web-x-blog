---
title: [OPT-093] Vue 路由懒加载与组件按需加载怎么落地？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-093：Vue 路由懒加载与组件按需加载怎么落地？

**答**：
- 路由懒加载是代码分割的第一刀：`() => import('...')` 让每条路由独立 chunk，首屏只下载当前路由代码。
- 按需加载的三个层次：路由级（必做）、重型组件级（图表/富文本/地图，配合 `defineAsyncComponent`）、依赖级（大库按入口拆，echarts 按需注册）。
- 打包配合：`manualChunks` 把 node_modules 稳定依赖（vue/router/pinia）拆 vendor chunk，提升 HTTP 缓存命中与并行下载。
- 配合 `defineAsyncComponent` 的 loading/error 组件，重型组件加载期间有占位，避免布局跳动。

```javascript
// 一一对应：Vue Router 懒加载 + 异步组件 + manualChunks 三层分割
import { createRouter, createWebHistory } from 'vue-router';
import { defineAsyncComponent } from 'vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: () => import('@/views/Home.vue') },      // 路由级分割
    { path: '/report', component: () => import('@/views/Report.vue') },
    // 首页的模块也可预加载控制：登录后空闲时预热高频路由
  ],
});
// 空闲预热次级路由，用户跳转时 chunk 已就绪
const warmup = () => import('@/views/Report.vue');
if ('requestIdleCallback' in window) requestIdleCallback(warmup, { timeout: 5000 });
else setTimeout(warmup, 3000);

// 组件级：重型图表异步化，带占位与失败重试
const HeavyChart = defineAsyncComponent({
  loader: () => import('@/components/HeavyChart.vue'),
  loadingComponent: ChartSkeleton,      // 加载占位，防 CLS
  errorComponent: ChartError,
  delay: 200,                           // 快速加载不闪 loading
  timeout: 10_000,
});

// vite.config.js —— 稳定 vendor 拆分，提升缓存命中
// export default defineConfig({
//   build: {
//     rollupOptions: {
//       output: {
//         manualChunks: {
//           vue: ['vue', 'vue-router', 'pinia'],            // 框架稳定不变
//           echarts: ['echarts'],                            // 重型库独立
//         },
//       },
//     },
//   },
// });
export { router, HeavyChart };
```
