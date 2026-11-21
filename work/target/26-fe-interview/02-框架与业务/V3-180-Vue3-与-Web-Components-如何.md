---
title: [V3-180] Vue3 与 Web Components 如何互操作？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-180：Vue3 与 Web Components 如何互操作？
**答**：
- Vue -> WC：defineCustomElement 把 SFC 编译成自定义元素，注册后任何框架甚至纯 HTML 都能用；样式默认打进 shadow root。
- WC -> Vue：第三方自定义元素直接写在模板里，需在 compilerOptions.isCustomElement 里声明，避免 Vue 当组件解析报警告。
- 事件与属性：WC 派发 CustomEvent，Vue 用 @事件名 监听；复杂对象属性必须走 property（DOM property）而非 attribute。
- 注意点：shadow DOM 里 slot 行为与 Vue slot 不同；样式穿透用 ::part 或让 WC 暴露 CSS 变量。

```typescript
// 1. Vue -> Web Components：defineCustomElement
import { defineCustomElement } from "vue";
import RatingStars from "./RatingStars.ce.vue"; // .ce.vue 后缀自动按 WC 模式编译

// 转成自定义元素并注册，之后 <rating-stars> 全局可用
customElements.define("rating-stars", defineCustomElement(RatingStars));

// RatingStars.ce.vue 内部（组合式 API 完全可用）：
// <script setup lang="ts">
// const model = defineModel<number>({ default: 0 });
// const emit = (v: number) => model.value = v;
// </script>
// <template>
//   <button v-for="i in 5" :key="i" @click="emit(i)">{{ i <= model ? "★" : "☆" }}</button>
// </template>
// <style> /* 打进 shadow root，外部样式不干扰 */ </style>
```

```vue
<!-- 2. WC -> Vue：消费第三方自定义元素 -->
<script setup lang="ts">
// vite.config.ts 需配置：
// plugins: [vue({ template: { compilerOptions: { isCustomElement: (tag) => tag.includes("-") } } })]
const score = ref(0);

function onRate(e: Event) {
  // WC 派发的 CustomEvent，detail 携带数据
  score.value = (e as CustomEvent<number>).detail;
}
</script>

<template>
  <!-- 复杂对象必须用 :prop 绑定（property），字符串才可用 attribute -->
  <rating-stars :value="score" @input="onRate" />
  <p>当前评分：{{ score }}</p>

  <!-- shadow DOM 的样式沟通：WC 内部约定 CSS 变量 -->
  <!-- WC 内部：button { color: var(--rating-color, gold) } -->
</template>

<style>
:root { --rating-color: #f56c6c; } /* 通过 CSS 变量穿透 shadow DOM */
</style>
```
