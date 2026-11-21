---
title: [OPT-091] computed 和 watch 的性能取舍怎么定？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-091：computed 和 watch 的性能取舍怎么定？

**答**：
- computed 是**惰性 + 缓存**：依赖不变不重算、无消费者不执行，天然免浪费；watch 是**主动触发**：依赖变化即执行副作用，即使没人消费。
- 性能优先原则：能用 computed 派生就不要 watch 同步状态——watch 常见的 `data -> setData` 回写模式多跑一次更新且易抖动。
- computed 的坑：getter 里写昂贵循环会在每次依赖变化时重算，且模板里多处引用同一 computed 只算一次（这是它的优势，要确保多处复用同一实例而非重复计算）。
- watch 的正确位置：需要副作用（发请求、写 localStorage、操作非响应式库）时用；`watchEffect` 注意自动收集依赖可能"扫进来"额外依赖。

```vue
<!-- 一一对应：computed vs watch 的三种场景对照 -->
<script setup>
import { ref, computed, watch, watchEffect } from 'vue';
const items = ref([]);
const keyword = ref('');

// 场景 1：派生数据 -> 必须 computed（惰性 + 缓存 + 多处复用只算一次）
const filtered = computed(() => {
  const kw = keyword.value.trim().toLowerCase();
  return kw ? items.value.filter((it) => it.name.toLowerCase().includes(kw)) : items.value;
});
// 反例：watch(keyword, () => filtered.value = items.filter(...))
// 问题：组件未渲染也执行；keyword 每变一次全量重算；模板多处引用各自重算

// 场景 2：副作用（搜索请求）-> watch + 防抖
let timer;
watch(keyword, (kw) => {
  clearTimeout(timer);
  timer = setTimeout(() => fetchResults(kw), 300); // 副作用留在 watch
});

// 场景 3：watchEffect 的依赖陷阱
// 反例：函数里顺手读了 items.value，搜索时列表任何变化都会触发重跑
watchEffect(() => {
  console.log('searching', keyword.value, items.value.length); // items 被误收集
});
// 修复：effect 里只读真正需要的依赖；确需大依赖用 watch 显式声明
</script>

<template>
  <!-- 模板里 filtered 可以引用多次，只计算一次 -->
  <p>共 {{ filtered.length }} 条</p>
  <virtual-list :items="filtered" />
</template>
```
