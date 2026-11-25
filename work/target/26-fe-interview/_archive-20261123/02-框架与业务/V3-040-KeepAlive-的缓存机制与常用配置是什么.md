---
title: [V3-040] KeepAlive 的缓存机制与常用配置是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-040：KeepAlive 的缓存机制与常用配置是什么？
**答**：
- KeepAlive 缓存组件 vnode 与实例，切换时不销毁、恢复时不重新创建。
- include/exclude 按组件 name 匹配白名单/黑名单，max 用 LRU 策略限制缓存数量。
- 被缓存的组件触发 activated/deactivated，而不是 mounted/unmounted。
- 适合 tab 页缓存、列表返回保持滚动位置等场景。

```vue
<script setup lang="ts">
import { ref, onActivated, onDeactivated } from "vue";

const currentTab = ref("TabA");
const tabs = ["TabA", "TabB"];

// TabA.vue 中：
// onActivated(() => 重新拉取数据);
// onDeactivated(() => 暂停轮询);
</script>

<template>
  <button v-for="t in tabs" :key="t" @click="currentTab = t">{{ t }}</button>
  <!-- include 按组件 name 匹配，max 控制缓存上限（LRU 淘汰） -->
  <KeepAlive :include="['TabA']" :max="10">
    <component :is="currentTab" />
  </KeepAlive>
</template>
```
