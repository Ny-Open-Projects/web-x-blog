---
title: [OPT-089] 为什么大数组要用 shallowRef？深层响应式的开销在哪？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-089：为什么大数组要用 shallowRef？深层响应式的开销在哪？

**答**：
- `ref([])` 默认深层响应式：数组每个元素、每个嵌套字段都被 Proxy 包装，10 万条数据光是初始化代理就多花几百 ms，后续每次读取还要走 proxy 拦截。
- `shallowRef` 只代理引用本身：整体替换数组（`list.value = newArr`）才触发更新，内部字段保持原生对象，读写都是零代理开销。
- 配合 `triggerRef` 可在原地修改后手动通知；`markRaw` 能标记个别嵌套对象永不代理。
- 适用判断：列表数据"整体拉取、整体渲染、不改内部字段"（商品流、聊天记录）——服务端数据天然是只读快照，深层响应式是纯浪费。

```vue
<!-- 一一对应：大列表 shallowRef 深浅对比与手动触发 -->
<script setup>
import { ref, shallowRef, triggerRef } from 'vue';

// 反例：深层代理 10 万条 -> 初始化 +500ms，滚动时每个字段读取都过 proxy
const deepList = ref([]);

// 正解：shallowRef，数据保持原生
const list = shallowRef([]);

async function load() {
  const res = await fetch('/api/goods?size=100000');
  const { items } = await res.json();
  list.value = items; // 整体替换触发更新；items 内部零代理，访问开销与普通对象相同
}

// 原地修改某项后手动触发：只通知，不重建代理
function updateItem(id, patch) {
  const item = list.value.find((it) => it.id === id);
  Object.assign(item, patch);   // 直接改原生对象
  triggerRef(list);             // 手动发信号，视图更新一次
}

// 局部需要响应式的"漏网之鱼"（如表单编辑的那一条），用 markRaw 隔离
import { markRaw, reactive } from 'vue';
const editing = reactive(markRaw({ id: 1, name: '' })); // 外层可控，字段按需
</script>

<template>
  <!-- 配合虚拟列表（见 OPT-033），万级数据滚动满帧 -->
  <li v-for="item in list" :key="item.id">{{ item.name }}</li>
</template>
```
