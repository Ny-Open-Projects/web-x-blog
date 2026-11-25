---
title: [V3-257] Nuxt 的 useAsyncData/useFetch：缓存、竞态与刷新怎么用好？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-257：Nuxt 的 useAsyncData/useFetch：缓存、竞态与刷新怎么用好？
**答**：
- 双端执行：SSR 时服务端执行并写入 payload；客户端水合直接复用不重发请求（默认行为），这是 useAsyncData 相比裸 fetch 的核心价值。
- key 即缓存：`useAsyncData('products', fetch)` 以 key 做 Nuxt 数据缓存（组件切换复用、payload 复用），key 变化触发重新执行。
- 竞态处理：`watch(source, cb)` 源变化时内置取消旧请求（abort），并保证只采纳最新结果；手写 fetch 需自己维护 AbortController。
- 刷新与失效：`refresh()` 强制重取；`clearNuxtData(key)` 清缓存；跨组件共享同一 key 的数据天然一致。
- 选项：`immediate: false`（守卫后手动执行）、`server: false`（仅客户端执行）、`lazy: true`（不阻塞 SSR 导航）、`dedupe: 'cancel'`。

```typescript
const page = ref(1);
const { data, pending, error, refresh } = await useAsyncData(
  `products-${page.value}`,                          // key 带参数：翻页各自缓存
  () => $fetch('/api/products', { query: { page: page.value } }),
  { watch: [page], dedupe: 'cancel' },               // page 变化：取消旧请求
);
// useFetch 是 useAsyncData + $fetch 的糖：useFetch('/api/products', { query })
// 仅客户端数据（如本地存储相关）：{ server: false }
```
