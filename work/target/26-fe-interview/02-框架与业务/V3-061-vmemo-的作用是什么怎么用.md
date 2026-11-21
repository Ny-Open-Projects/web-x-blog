---
title: [V3-061] v-memo 的作用是什么？怎么用？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-061：v-memo 的作用是什么？怎么用？
**答**：
- v-memo 接收依赖数组，数组值不变时跳过该子树整个 vnode 的 diff。
- 适合"列表项大部分不变、个别交互频繁"的长列表优化。
- 通常与 v-for 搭配，依赖数组里放该项相关的判断条件。
- 依赖数组为 `[]` 时只渲染一次；注意依赖写错会导致不更新的 bug。

```vue
<script setup lang="ts">
import { ref } from "vue";

const items = ref(
  Array.from({ length: 1000 }, (_, i) => ({
    id: i,
    name: `item-${i}`,
  }))
);
const selectedId = ref(-1);
</script>

<template>
  <!-- item.id === selectedId 不变时，该节点的 diff 被整体跳过 -->
  <div v-for="item in items" :key="item.id" v-memo="[item.id === selectedId]">
    <span>{{ item.name }}</span>
    <button @click="selectedId = item.id">选中</button>
  </div>
</template>
```
