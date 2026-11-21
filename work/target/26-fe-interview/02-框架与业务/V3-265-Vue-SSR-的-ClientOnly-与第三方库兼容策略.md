---
title: [V3-265] Vue SSR 的 ClientOnly 与第三方库兼容策略是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-265：Vue SSR 的 ClientOnly 与第三方库兼容策略是什么？
**答**：
- 问题根源：多数编辑器/图表/地图库在模块加载或初始化时访问 `window/document`，SSR 渲染直接 ReferenceError。
- 兜底手段 1：`<ClientOnly>`（Nuxt 内置）+ `fallback` 插槽——SSR 输出占位，客户端挂载后渲染真实组件。
- 兜底手段 2：动态 import（`onMounted` 里 `await import('editor')`）+ `defineAsyncComponent({ server: false })`，保证 chunk 不进服务端 bundle。
- 判别准则：库"需要 DOM 才初始化"用 onMounted + 动态 import；库"模块顶层访问 window"必须 ClientOnly/`server: false`，且注意 ESM 顶层副作用无法 tree-shake 掉。
- SSR 骨架对齐：fallback 插槽的尺寸样式要和真实组件一致（min-height/aspect-ratio），避免水合后跳动（CLS）。

```vue
<script setup>
import { defineAsyncComponent, onMounted, ref } from 'vue';
// 方案 1：仅客户端的异步组件
const RichEditor = defineAsyncComponent({
  loader: () => import('@wangeditor/editor-for-vue'), // chunk 不进服务端
});
</script>
<template>
  <ClientOnly fallback-tag="div">
    <template #fallback><div class="editor-skeleton" style="min-height:300px"></div></template>
    <RichEditor />
  </ClientOnly>
  <!-- 方案 2：初始化需要 DOM，onMounted 动态 import -->
  <div ref="chartEl" style="min-height:280px"></div>
</template>
<script setup>
const chartEl = ref(null);
onMounted(async () => {
  const echarts = await import('echarts');
  echarts.init(chartEl.value).setOption(option);
});
</script>
```
