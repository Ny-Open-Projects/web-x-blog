---
title: [V3-035] 如何自定义 v-model 修饰符？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-035：如何自定义 v-model 修饰符？
**答**：
- 修饰符会以 props 形式传入：`v-model.capitalize` 对应 `modelModifiers: { capitalize: true }`。
- 组件在 emit 前根据修饰符处理值，如首字母大写、数字转换。
- 带参数的修饰符（如 v-model:count.double）会合并进同名 key。
- 这是封装表单组件时的常用技巧。

```vue
<!-- CapitalizeInput.vue -->
<script setup lang="ts">
const props = defineProps<{
  modelValue: string;
  modelModifiers?: { capitalize?: boolean };
}>();

const emit = defineEmits<{ "update:modelValue": [value: string] }>();

function onInput(e: Event) {
  let value = (e.target as HTMLInputElement).value;
  // v-model.capitalize 会把修饰符以 modelModifiers 传入
  if (props.modelModifiers?.capitalize) {
    value = value.charAt(0).toUpperCase() + value.slice(1);
  }
  emit("update:modelValue", value);
}
</script>

<template>
  <input :value="modelValue" @input="onInput" />
</template>

<!-- 使用：<CapitalizeInput v-model.capitalize="name" /> -->
```

## 第八章 插槽 Slot
