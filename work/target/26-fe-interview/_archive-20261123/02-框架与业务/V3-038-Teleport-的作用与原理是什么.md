---
title: [V3-038] Teleport 的作用与原理是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-038：Teleport 的作用与原理是什么？
**答**：
- Teleport 把子节点渲染到指定 DOM 目标（to 选择器/元素），而组件逻辑仍留在原组件树。
- 解决弹窗、Toast 被 overflow: hidden 或 z-index 层叠上下文困住的问题。
- to 目标必须在 Teleport 挂载时已存在，通常用 body 或 #app 之外的容器。
- 支持 disabled 切换为原地渲染；配合 CSS 定位实现全屏弹窗。

```vue
<script setup lang="ts">
import { ref } from "vue";

const show = ref(false);
</script>

<template>
  <!-- Teleport 把渲染结果传送到 body，组件逻辑仍在原组件树 -->
  <button @click="show = true">打开弹窗</button>
  <Teleport to="body" :disabled="false">
    <div v-if="show" class="modal">弹窗内容，不受父级 overflow 与 z-index 影响</div>
  </Teleport>
</template>

<style scoped>
.modal {
  position: fixed;
  inset: 0;
  margin: auto;
  width: 300px;
  height: 200px;
  background: #fff;
}
</style>
```
