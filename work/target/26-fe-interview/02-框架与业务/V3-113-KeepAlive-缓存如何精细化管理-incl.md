---
title: [V3-113] KeepAlive 缓存如何精细化管理（include 动态缓存池）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-113：KeepAlive 缓存如何精细化管理（include 动态缓存池）？
**答**：
- 默认 max 或全量 include 都太粗：多 tab 后台中，缓存池应该等于“当前打开的 tab 集合”。
- tabs store 维护 tab 列表，cachedNames computed 派生缓存名单，进 tab 加入、关 tab 移除。
- KeepAlive 的 include 响应式变化后，被移除的组件实例立即销毁，缓存自动释放。
- 被缓存组件必须声明组件名（defineOptions name），且与路由 name 一致，否则 include 匹配不到。

```typescript
// stores/modules/tabs.ts —— tab 即缓存池
import { defineStore } from "pinia";
import { computed, ref } from "vue";

interface TabItem {
  name: string; // 与路由 name、组件名一致
  path: string;
  title: string;
}

export const useTabsStore = defineStore("tabs", () => {
  const tabs = ref<TabItem[]>([]);

  // 缓存名单由当前打开的 tabs 派生，驱动 KeepAlive 的 include
  const cachedNames = computed(() => tabs.value.map((t) => t.name));

  function add(tab: TabItem) {
    if (!tabs.value.some((t) => t.name === tab.name)) tabs.value.push(tab);
  }

  function remove(name: string) {
    tabs.value = tabs.value.filter((t) => t.name !== name); // 移出后对应组件实例被销毁
  }

  return { tabs, cachedNames, add, remove };
});
```

```vue
<!-- layouts/KeepAliveLayout.vue -->
<script setup lang="ts">
import { useTabsStore } from "@/stores/modules/tabs";

const tabsStore = useTabsStore();
</script>

<template>
  <RouterView v-slot="{ Component }">
    <KeepAlive :include="tabsStore.cachedNames" :max="10">
      <component :is="Component" v-if="Component" />
    </KeepAlive>
  </RouterView>
</template>

<!-- 被缓存的页面组件必须声明同名 name：
<script setup lang="ts">
defineOptions({ name: "Order" }); // 与路由 name 一致，include 才能命中
</script>
-->
```
