---
title: [V3-032] 父组件如何调用子组件的方法？defineExpose 是干什么的？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-032：父组件如何调用子组件的方法？defineExpose 是干什么的？
**答**：
- `<script setup>` 的组件默认对外封闭，模板 ref 拿到的实例是空壳。
- defineExpose 显式暴露属性和方法，父组件通过模板 ref 访问。
- 模板 ref 需要用 `ref<InstanceType<typeof Child>>()` 声明类型。
- 这种"命令式调用"应克制使用，优先考虑 props/emit 的声明式通信。

```vue
<!-- Child.vue -->
<script setup lang="ts">
import { ref } from "vue";

// <script setup> 默认是封闭的，父组件拿不到内部属性
const count = ref(0);
function reset() {
  count.value = 0;
}
defineExpose({ count, reset }); // 显式暴露
</script>

<template>
  <span>{{ count }}</span>
</template>

<!-- Parent.vue 中：
const childRef = ref<InstanceType<typeof Child>>();
childRef.value?.reset(); -->
```
