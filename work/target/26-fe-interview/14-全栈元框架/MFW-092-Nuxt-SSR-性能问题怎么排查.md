---
title: [MFW-092] Nuxt SSR 的性能问题怎么排查和优化？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-092：Nuxt SSR 的性能问题怎么排查和优化？
**答**：
- 先分层定位：**TTFB 高**查服务端（数据请求慢、无缓存、组件重渲染）；**渲染完成晚**查组件树（同步阻塞组件、大列表）；**客户端慢**查 bundle 与水合成本。
- 服务端三板斧：数据层上缓存（Nitro storage + swr/isr 规则）；取数并行化（`Promise.all`，避免 setup 里串行 await）；把纯静态路由 `prerender` 或 `ssr: false` 减少每请求渲染。
- 组件层：大列表用 `vue` 的 `v-memo`/分页；重计算组件拆出去或 `lazy: true` 延后；服务端与客户端共用的组件避免依赖 window 逻辑分支。
- 量化闭环：Nitro 自带 `--profile` / OTel span；用 `autocannon` 压测对比优化前后 p95；关注 SSR 内存泄漏（每请求共享的模块级可变状态是头号嫌疑）。

```ts
// 性能敏感写法对照
<script setup lang="ts">
// ❌ 串行瀑布
// const a = await $fetch('/api/a'); const b = await $fetch('/api/b?a=' + a.x);

// ✅ 并行
const [a, b] = await Promise.all([
  $fetch('/api/products?page=1'),
  $fetch('/api/banners'),
]);

// ✅ 大列表：服务端只渲染首屏 20 条，其余客户端分页/虚拟滚动
const firstPage = a.slice(0, 20);
</script>
```

```ts
// server/plugins/trace.ts —— 每请求渲染计时（性能归因入口）
export default defineNitroPlugin((nitro) => {
  nitro.hooks.hook('request', async (event) => {
    const t0 = performance.now();
    event.$t0 = t0;
  });
  nitro.hooks.hook('afterResponse', async (event) => {
    const ms = performance.now() - (event as any).$t0;
    if (ms > 500) {
      console.warn(`[slow] ${event.path} ${ms.toFixed(0)}ms`);
      apm.histogram('ssr.render.ms', ms, { path: event.path });
    }
  });
});
```
