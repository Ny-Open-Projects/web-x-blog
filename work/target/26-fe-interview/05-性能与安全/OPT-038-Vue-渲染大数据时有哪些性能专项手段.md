---
title: [OPT-038] Vue 渲染大数据时有哪些性能专项手段？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-038：Vue 渲染大数据时有哪些性能专项手段？

**答**：
- `shallowRef` 包大数组：跳过深层 Proxy 代理（10 万条数据逐个代理本身就要数百 ms），整体替换 `value` + `triggerRef()` 手动触发更新。
- `v-memo` 给列表行加缓存：`v-memo="[item.id, item.selected]"`，依赖不变就整行跳过 diff，等价于手动 memo。
- `v-once` / `v-pre` 用于纯静态内容，编译期就跳过后续更新。
- 列表页进出用 `keep-alive`：返回列表页不重新请求、保留滚动位置；配合 `include` 控制缓存范围，防止内存膨胀。

```vue
<!-- 一一对应：shallowRef + v-memo + keep-alive 的组合落地 -->
<template>
  <!-- v-memo：仅当 id 或 selected 变化时才重新渲染这一行 -->
  <li v-for="item in rows" :key="item.id" v-memo="[item.id, item.selected]">
    <span :class="{ active: item.selected }" @click="toggle(item.id)">
      {{ item.name }}
    </span>
  </li>
</template>

<script setup>
import { shallowRef, triggerRef } from 'vue';

// 10 万条数据用 shallowRef：不做深层响应式代理，初始化快一个量级
const rows = shallowRef(loadBigList());

function toggle(id) {
  const target = rows.value.find((r) => r.id === id);
  target.selected = !target.selected;
  // 直接改了引用内部数据，Proxy 不会通知；手动触发依赖此 ref 的更新
  triggerRef(rows);
}
</script>

<!-- App.vue：列表页 keep-alive，返回时保留状态与滚动位置 -->
<template>
  <router-view v-slot="{ Component }">
    <keep-alive include="ListPage">
      <component :is="Component" />
    </keep-alive>
  </router-view>
</template>
```
