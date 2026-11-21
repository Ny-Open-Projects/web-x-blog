---
title: [V3-028] Vue3 中 props 和 emit 如何做类型声明？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-028：Vue3 中 props 和 emit 如何做类型声明？
**答**：
- defineProps 泛型写法直接描述 props 结构，编译器自动生成运行时校验。
- defineEmits 用类型对象声明事件名与参数元组（3.3+ 语法）。
- props 是 shallowReadonly 的，子组件不能修改；单向数据流是契约。
- 父组件用 kebab-case 监听 camelCase 事件即可。

```vue
<!-- Child.vue -->
<script setup lang="ts">
const props = defineProps<{
  title: string;
  count?: number;
}>();

const emit = defineEmits<{
  change: [value: number];
  update: [id: string, value: unknown];
}>();

function add() {
  emit("change", (props.count ?? 0) + 1);
}
</script>

<template>
  <h3>{{ title }}</h3>
  <button @click="add">count 加一</button>
</template>

<!-- 父组件使用：
<Child title="标题" :count="1" @change="onChange" /> -->
```
