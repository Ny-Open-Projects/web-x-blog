---
title: [V3-025] Vue3 的生命周期钩子与 Vue2 如何对应？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-025：Vue3 的生命周期钩子与 Vue2 如何对应？
**答**：
- beforeCreate/created 被 setup 本身取代，不需要专门钩子。
- beforeDestroy/destroyed 更名为 onBeforeUnmount/onUnmounted。
- 其余一一对应：onBeforeMount、onMounted、onBeforeUpdate、onUpdated。
- KeepAlive 内用 onActivated/onDeactivated，错误捕获用 onErrorCaptured。

```vue
<script setup lang="ts">
import { onMounted, onUnmounted } from "vue";

// Vue2 -> Vue3 对照：
// beforeCreate / created -> setup 本身
// beforeMount -> onBeforeMount
// mounted -> onMounted
// beforeUpdate -> onBeforeUpdate
// updated -> onUpdated
// beforeDestroy -> onBeforeUnmount
// destroyed -> onUnmounted
// activated / deactivated -> onActivated / onDeactivated（KeepAlive 内）
// errorCaptured -> onErrorCaptured

onMounted(() => console.log("DOM 已挂载"));
onUnmounted(() => console.log("已卸载，做清理"));
</script>

<template>
  <p>生命周期示例</p>
</template>
```
