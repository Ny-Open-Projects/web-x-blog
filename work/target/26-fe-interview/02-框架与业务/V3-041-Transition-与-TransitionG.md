---
title: [V3-041] Transition 与 TransitionGroup 的区别是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-041：Transition 与 TransitionGroup 的区别是什么？
**答**：
- Transition 用于单元素/组件的进出场，通过自动添加 fade-enter-from 等 class 驱动 CSS 过渡。
- TransitionGroup 用于列表，支持 move class 实现排序位移动画，渲染真实元素需指定 tag。
- 进出场由 v-if/v-show/动态组件切换触发，leave 期间元素保持挂载。
- 也可用 JavaScript 钩子（@enter/@leave）做动画库集成。

```vue
<script setup lang="ts">
import { ref } from "vue";
const show = ref(true);
const list = ref([1, 2, 3]);
</script>

<template>
  <button @click="show = !show">切换</button>
  <!-- Transition 在插入/移除时自动添加过渡 class -->
  <Transition name="fade">
    <p v-if="show">淡入淡出的文本</p>
  </Transition>

  <!-- TransitionGroup 用于列表，支持 move class -->
  <TransitionGroup name="list" tag="ul">
    <li v-for="item in list" :key="item">{{ item }}</li>
  </TransitionGroup>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.list-move {
  transition: transform 0.3s;
}
</style>
```

## 第十章 diff 算法与 key
