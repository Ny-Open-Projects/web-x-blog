---
title: [V3-034] Vue3 组件上的 v-model 是如何实现的？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-034：Vue3 组件上的 v-model 是如何实现的？
**答**：
- `v-model="title"` 展开为 `:modelValue="title"` + `@update:modelValue="title = $event"`。
- 子组件用 modelValue prop 接收，用 update:modelValue 事件通知。
- Vue3 支持多个 v-model：`v-model:name`、`v-model:age`，用参数区分。
- 相比 Vue2 的 value/input + model 选项，命名统一且可组合。

```vue
<!-- ModelChild.vue -->
<script setup lang="ts">
// v-model="title" 展开为 :modelValue="title" + @update:modelValue="title = $event"
const props = defineProps<{ modelValue: string }>();
const emit = defineEmits<{ "update:modelValue": [value: string] }>();

function onInput(e: Event) {
  emit("update:modelValue", (e.target as HTMLInputElement).value);
}
</script>

<template>
  <input :value="modelValue" @input="onInput" />
</template>

<!-- Vue3 支持多个 v-model，用参数区分：
<UserForm v-model:name="name" v-model:age="age" /> -->
```
