---
title: [V3-150] TransitionGroup 如何实现列表排序动画（FLIP 原理）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-150：TransitionGroup 如何实现列表排序动画（FLIP 原理）？
**答**：
- FLIP 四步：First 记录元素旧位置 → Last 应用新位置 → Invert 用 transform 反向偏移回旧位 → Play 过渡回 0。TransitionGroup 自动帮你做。
- 你只需要写对 `.xxx-move` 类（管位移）、`.xxx-enter/leave-active`（管进出）。
- 关键坑：`.leave-active { position: absolute }` 让离场元素脱离文档流，其余元素才能立即补位产生平滑移动动画。
- 每个列表项必须有稳定的 key（通常业务 id），用 index 作 key 移动动画会错乱。

```vue
<script setup lang="ts">
import { ref } from "vue";

let id = 0;
const items = ref(
  Array.from({ length: 5 }, () => ({ id: ++id, name: `item-${id}` }))
);

function shuffle() {
  items.value = [...items.value].sort(() => Math.random() - 0.5); // 乱序触发 move 动画
}
function remove(item: { id: number }) {
  items.value = items.value.filter((i) => i.id !== item.id);
}
function add() {
  items.value.push({ id: ++id, name: `item-${id}` });
}
</script>

<template>
  <button @click="shuffle">乱序</button>
  <button @click="add">加一项</button>
  <!-- TransitionGroup 自动执行 FLIP；tag 指定渲染成 ul -->
  <TransitionGroup name="flip" tag="ul">
    <li v-for="item in items" :key="item.id" class="row">
      {{ item.name }}
      <button @click="remove(item)">删</button>
    </li>
  </TransitionGroup>
</template>

<style>
.flip-move { transition: transform 0.4s ease; }          /* 核心：位移过渡 */
.flip-enter-active, .flip-leave-active { transition: all 0.3s; }
.flip-leave-active { position: absolute; }                /* 关键：离场脱离文档流，其余项才能补位 */
.flip-enter-from, .flip-leave-to { opacity: 0; transform: translateX(30px); }
.row { width: 240px; }
</style>
```
