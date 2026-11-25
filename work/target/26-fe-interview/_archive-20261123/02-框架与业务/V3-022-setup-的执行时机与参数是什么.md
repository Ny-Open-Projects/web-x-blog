---
title: [V3-022] setup 的执行时机与参数是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-022：setup 的执行时机与参数是什么？
**答**：
- setup 在组件实例创建之前、props 解析之后执行，早于 beforeCreate。
- `<script setup>` 中 this 不是组件实例，组合式 API 也不依赖 this。
- defineProps/defineEmits/defineExpose 是编译器宏，无需 import，只能在 setup 顶层使用。
- setup 无法访问 data/methods 等选项式成员，因为它们此时还不存在。

```vue
<script setup lang="ts">
// setup 在组件实例创建前、props 解析后执行
// 此时 this 不是组件实例（组合式 API 里也不该用 this）
interface Props {
  title: string;
  count?: number;
}

// defineProps / defineEmits 是编译器宏，无需 import
const props = defineProps<Props>();
const emit = defineEmits<{ change: [value: string] }>();

console.log(props.title); // props 已可用
emit("change", "init");
</script>

<template>
  <h3>{{ title }}</h3>
</template>
```
