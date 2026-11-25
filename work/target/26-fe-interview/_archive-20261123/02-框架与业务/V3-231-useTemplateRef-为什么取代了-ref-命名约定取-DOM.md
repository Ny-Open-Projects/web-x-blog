---
title: [V3-231] useTemplateRef 为什么取代了「ref 同名约定」取 DOM 的旧写法？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-231：useTemplateRef 为什么取代了「ref 同名约定」取 DOM 的旧写法？
**答**：
- 旧写法问题：`const input = ref(null)` + `<input ref="input">` 靠**字符串同名匹配**绑定，编译器无法知道这层关系，变量改名/移动会静默失效，IDE 也无法跟踪引用。
- 新 API：`const input = useTemplateRef('input')`——显式按模板 ref 名取值，编译器产出 `TemplateRefsType` 推导，IDE 可跳转、可重命名重构。
- 类型：自动从模板收集 ref 名生成类型（`ComponentPublicInstance | HTMLElement | null`），拿组件实例也有类型。
- 迁移：3.5 起推荐 useTemplateRef；同名约定仍可用但处于"不推荐"状态，Vapor 模式下同名约定直接不支持。
- 类比：从"隐式约定"到"显式声明"，与 defineModel 一样是编译器增强开发体验的路线。

```vue
<script setup>
import { useTemplateRef } from 'vue';
const inputRef = useTemplateRef('my-input'); // 参数是模板上的 ref 名（字符串）
const listRef = useTemplateRef('list');      // v-for 上的 ref 得到数组
function focus() { inputRef.value?.focus(); }
</script>
<template>
  <input ref="my-input" />
  <ul ref="list"><li v-for="i in 3" :key="i">{{ i }}</li></ul> <!-- list.value 为元素数组 -->
  <button @click="focus">聚焦</button>
</template>
```
