---
title: [V3-068] 泛型 defineProps 与 withDefaults 怎么用？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-068：泛型 defineProps 与 withDefaults 怎么用？
**答**：
- `defineProps<Props>()` 以类型为唯一数据源，编译器自动生成运行时 props 校验。
- 默认值用 withDefaults：引用类型的默认值必须写成工厂函数。
- 3.5+ 支持响应式 props 解构：`const { count = 0 } = defineProps<Props>()`。
- 编译器宏无需 import，且不能在普通 ts 文件中使用。

```vue
<script setup lang="ts">
interface Props {
  title: string;
  count?: number;
  tags?: string[];
}

// 泛型参数即类型声明，编译器自动生成运行时 props
const props = withDefaults(defineProps<Props>(), {
  count: 0,
  tags: () => [], // 引用类型默认值要返回函数
});

// 3.5+ 也可以用响应式解构代替 withDefaults：
// const { count = 0, tags = [] } = defineProps<Props>();
console.log(props.title);
</script>

<template>
  <h3>{{ title }} {{ count }}</h3>
</template>
```

## 第二十章 VueUse 常用
