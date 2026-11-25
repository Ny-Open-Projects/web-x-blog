---
title: [MFW-078] Nuxt 的 useFetch 和 useAsyncData 有什么区别，payload 怎么复水？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-078：Nuxt 的 useFetch 和 useAsyncData 有什么区别，payload 怎么复水？
**答**：
- `useAsyncData` 是底层原语：包装任意异步函数，负责 key、SSR 脱水、客户端复水、缓存去重。`useFetch` 是它的 fetch 快捷方式（自动生成 URL key + 响应解析）。能自己封装 SDK 时用 useAsyncData，快速取数用 useFetch。
- 复水机制：SSR 阶段数据被序列化进 `window.__NUXT__` payload，客户端 hydration 时按 key 直接取用**不再发请求**——这正是「SSR 首屏有数据且客户端不重复 fetch」的关键；key 必须稳定（同一个 key 两侧才能对上）。
- 状态字段：`data / error / status / refresh`，默认 `immediate: true`；SSR 失败要 `throw createError` 才能进错误页而不是静默 null。
- 注意点：key 不稳定 → 客户端复水失败重新请求（双请求）；循环内动态 key 要保证首次渲染 key 与后续一致；`lazy: true` 可退化为不阻塞导航。

```vue
<script setup lang="ts">
const route = useRoute();

// useFetch：URL 即 key（内部规范化），SSR 获取 + 客户端复水一步到位
const { data: product, error, refresh, status } = await useFetch(
  () => `/api/products/${route.params.id}`,
  { key: `product:${route.params.id}` }, // 显式 key 更稳（URL 含变化参数时）
);

// useAsyncData：包装自研 SDK
const { data: recos } = await useAsyncData(
  `recos:${route.params.id}`,
  () => sdk.getRecommendations(route.params.id as string),
  { server: true, lazy: false },
);

watch(error, (e) => {
  if (e) throw createError({ statusCode: 404, fatal: true });
});
</script>
```

```ts
// 服务端手写等价物（理解机制用）：脱水
// server 渲染时 useAsyncData 结果被收集进 nuxtApp.payload.data[key]
// HTML 末尾注入：<script>window.__NUXT__ = { data: { 'product:1001': {...} } }</script>
// 客户端 useAsyncData('product:1001') 先查 payload.data['product:1001']，命中则跳过执行
```
