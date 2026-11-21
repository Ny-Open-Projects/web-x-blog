---
title: [V3-042] key 的作用是什么？为什么不能用 index 当 key？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-042：key 的作用是什么？为什么不能用 index 当 key？
**答**：
- key 是 vnode 的身份标识，diff 时用于判断"是否同一个节点"，从而复用 DOM 并移动而不是重建。
- 无 key 时 Vue 走"就地复用"策略，只做内容 patch，插入删除时状态可能错位。
- 用 index 当 key：头部插入后，后续项的 key 全部变化且内容平移，带输入框等内部状态的组件会错乱。
- 正确做法：用稳定唯一的业务 id 做 key。

```vue
<script setup lang="ts">
import { ref } from "vue";

const list = ref([
  { id: 1, name: "a" },
  { id: 2, name: "b" },
  { id: 3, name: "c" },
]);

function insertFirst() {
  // 有 key 时高效复用并移动 DOM；无 key 或 index 当 key 时可能原地复用出错
  list.value.unshift({ id: Date.now(), name: "new" });
}
</script>

<template>
  <ul>
    <!-- key 是节点的身份标识：无 key 时 Vue 用就地复用策略 -->
    <li v-for="item in list" :key="item.id">
      {{ item.name }} <input placeholder="输入内容试试" />
    </li>
  </ul>
  <!-- 错误示范：用 index 当 key，头部插入会导致输入框状态错乱 -->
  <button @click="insertFirst">头部插入</button>
</template>
```
