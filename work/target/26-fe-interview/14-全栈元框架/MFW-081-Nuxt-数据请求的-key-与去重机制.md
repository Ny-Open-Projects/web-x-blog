---
title: [MFW-081] Nuxt 数据请求的 key 为什么重要，去重是怎么发生的？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-081：Nuxt 数据请求的 key 为什么重要，去重是怎么发生的？
**答**：
- key 是数据在 `nuxtApp.payload.data` 中的唯一坐标，同时承担三件事：SSR 脱水→复水对齐、同 key 请求去重、`refreshNuxtData(key)` 精准刷新。key 不稳 = 复水失败 = 客户端二次请求（最常见双请求病根）。
- 去重发生在 `useAsyncData` 内部：同一 key 的调用共享同一个 pending Promise（dedupe: 'defer'/'immediate' 控制），同一渲染周期内多处组件用同一 key 只发一次网络请求。
- key 必须含全部影响结果的参数（id、筛选条件），否则会出现「A 页数据缓到 key 里被 B 页读走」的串数据事故；也要避免把时间戳塞进 key，那样缓存永远不命中。
- 与 React 生态对照：key ≈ React Query 的 queryKey + React.cache 的参数指纹，但 Nuxt 里它还兼管复水，权重更高。

```ts
// composables/useProduct.ts
export function useProduct(id: string, opts?: { currency?: string }) {
  // key 必须覆盖所有参数：少带 currency 就会串数据
  return useFetch('/api/products/' + id, {
    key: `product:${id}:${opts?.currency ?? 'CNY'}`,
    // dedupe: 'defer' 默认：同 key 并发调用合并为一次
    getCacheData(key) { // 可接入自定义缓存（Nitro storage）
      return nuxtApp.payload.data[key]; // 复水来源
    },
  });
}

// 精准刷新：购物车角标场景
export function refreshCartBadge() {
  refreshNuxtData('cart:count');
}
```

```vue
<!-- 同一页面两处使用同一 key，只发一次请求 -->
<script setup lang="ts">
const { data: price } = useProduct('1001');     // 发起
const { data: same } = useProduct('1001');      // 命中同一 pending，不重复请求
</script>
```
