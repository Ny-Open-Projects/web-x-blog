---
title: [V3-039] Suspense 如何处理异步组件？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-039：Suspense 如何处理异步组件？
**答**：
- Suspense 包裹含异步依赖的组件（async setup、顶层 await、异步组件），等待期间显示 fallback。
- 组件内 `await` 必须写在 async setup 中；Suspense 是实验性 API，生产使用需谨慎。
- 支持 default/fallback 两个插槽，可有多个异步子组件统一等待。
- 配合 onErrorCaptured 或 onRejected 处理加载失败。

```vue
<script setup lang="ts">
import { defineAsyncComponent } from "vue";
const AsyncChart = defineAsyncComponent(() => import("./AsyncChart.vue"));
</script>

<template>
  <Suspense>
    <template #default>
      <!-- 组件内 async setup 或顶层 await 的组件在此等待 -->
      <AsyncChart />
    </template>
    <template #fallback>
      <p>加载中...</p>
    </template>
  </Suspense>
</template>
```
