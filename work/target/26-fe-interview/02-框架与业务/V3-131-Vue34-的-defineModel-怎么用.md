---
title: [V3-131] Vue3.4 的 defineModel 怎么用？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-131：Vue3.4 的 defineModel 怎么用？
**答**：
- 一个宏替代三件套：声明 modelValue prop、注册 update:modelValue emit、返回可读写的 ref。
- 组件内部直接 `keyword.value = x`，宏自动 emit 给父组件，模板里可 v-model 绑定该 ref。
- 支持多个 v-model（defineModel("title")）、必填校验与默认值、内置与自定义修饰符。
- 是受控/非受控双模式组件（V3-075）的官方化简版：非受控时内部 ref 自治，受控时随父组件值。

```vue
<!-- components/SearchInput.vue -->
<script setup lang="ts">
// Vue3.4+：defineModel 一行替代 modelValue prop + update:modelValue emit 样板
const keyword = defineModel<string>({ default: "" });

// 多个 v-model：defineModel("title") 对应父组件的 v-model:title
// const title = defineModel<string>("title");

// 自定义修饰符：
// const [text, modifiers] = defineModel<string>();
// if (modifiers.trim) emit 处理时先 trim
</script>

<template>
  <input v-model="keyword" placeholder="搜索" />
  <p>当前值：{{ keyword }}</p>
</template>

<!-- 父组件使用：
<SearchInput v-model="search" />      // search 变化自动同步
<SearchInput v-model:title="t" />     // 命名 v-model
-->
```
