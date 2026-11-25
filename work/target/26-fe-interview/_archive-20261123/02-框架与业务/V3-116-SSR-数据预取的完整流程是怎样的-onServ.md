---
title: [V3-116] SSR 数据预取的完整流程是怎样的（onServerPrefetch + 状态注水）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-116：SSR 数据预取的完整流程是怎样的（onServerPrefetch + 状态注水）？
**答**：
- 服务端：组件 setup 里用 onServerPrefetch 注册异步钩子，renderToString 前会等待其完成，数据写入 Pinia。
- 注水：服务端把 `pinia.state.value` 序列化成 JSON，注入 HTML 的 `window.__PINIA_STATE__`。
- 客户端：entry-client 创建 pinia 后用注水状态恢复 store，hydrate 直接渲染出与服务器一致的 DOM。
- 校验闭环：客户端不再重复请求同一数据——onServerPrefetch 只在服务端执行，天然不会二次请求。

```vue
<!-- pages/Product.vue —— 服务端预取数据 -->
<script setup lang="ts">
import { onServerPrefetch } from "vue";
import { useRoute } from "vue-router";
import { useProductStore } from "@/stores/product";

const store = useProductStore();
const route = useRoute();

// 只在服务端执行：数据写入 Pinia，随 HTML 下发，客户端不会重复请求
onServerPrefetch(async () => {
  await store.fetchProduct(String(route.params.id));
});
</script>

<template>
  <h1>{{ store.current.title }}</h1>
</template>
```

```javascript
// entry-server.js 与 entry-client.js 的注水关键片段
import { createSSRApp } from "vue";
import { createPinia } from "pinia";

// —— 服务端：渲染完成后序列化状态注入 HTML ——
export async function render(url) {
  const app = createSSRApp(App);
  const pinia = createPinia();
  app.use(pinia);

  const html = await renderToString(app, { url });
  const state = JSON.stringify(pinia.state.value);
  return {
    html,
    stateTag: `<script>window.__PINIA_STATE__=${state.replace(/</g, "\\u003c")}<\/script>`,
  };
}

// —— 客户端：用注水状态恢复 store，再 hydrate ——
export function createClientApp() {
  const app = createSSRApp(App);
  const pinia = createPinia();
  app.use(pinia);

  if (window.__PINIA_STATE__) {
    pinia.state.value = window.__PINIA_STATE__; // 注水：store 直接拥有服务端数据
  }
  return { app };
}
```
