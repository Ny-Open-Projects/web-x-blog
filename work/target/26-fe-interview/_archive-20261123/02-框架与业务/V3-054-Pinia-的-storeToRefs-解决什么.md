---
title: [V3-054] Pinia 的 storeToRefs 解决什么问题？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-054：Pinia 的 storeToRefs 解决什么问题？
**答**：
- 直接解构 store 会丢失响应式（state 变成普通值、action 没问题）。
- storeToRefs 只把 state 和 getters 转成 ref，action 保持原样可以直接解构。
- 其内部基于 toRefs 并跳过函数属性。
- 忘记用它是最常见的 Pinia 响应式丢失事故。

```vue
<script setup lang="ts">
import { useCounterStore } from "@/stores/counter";
import { storeToRefs } from "pinia";

const store = useCounterStore();

// 错误：解构丢失响应式
// const { count, double } = store;

// 正确：storeToRefs 只转换 state 与 getters
const { count, double } = storeToRefs(store);

// action 不是响应式值，直接解构即可
const { increment } = store;
</script>

<template>
  <p>{{ count }} - {{ double }}</p>
  <button @click="increment">加一</button>
</template>
```

## 第十五章 Vue Router4

一次导航中各类守卫的执行顺序如下图，理解顺序才能正确做鉴权与重定向。

```mermaid
sequenceDiagram
    participant U as 用户触发导航
    participant GB as 全局 beforeEach
    participant RE as 路由独享 beforeEnter
    participant CE as 组件内 beforeRouteEnter
    participant BR as 全局 beforeResolve
    participant AC as 全局 afterEach
    U->>GB: 开始导航
    GB->>RE: 守卫放行 next
    RE->>CE: 解析懒加载组件
    CE->>BR: 所有守卫通过
    BR->>AC: 确认导航
    AC->>U: 导航完成并更新 DOM
```
