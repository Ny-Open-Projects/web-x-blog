---
title: [OPT-090] v-memo 的适用场景和陷阱是什么？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-090：v-memo 的适用场景和陷阱是什么？

**答**：
- `v-memo="[deps]"`：deps 未变时**整段子树跳过 diff**（ vnode 缓存复用），是模板级的 memo，粒度比组件 memo 更细。
- 高价值场景：万行列表中"绝大多数行内容不变"——`v-memo="item.id === selectedId"` 只让选中行变化时 diff 两行，其余全跳过。
- 陷阱一：deps 数组写漏依赖 -> 该更新的不更新，出"灵异 bug"；陷阱二：在内部含 slot/动态组件的复杂子树上乱用，缓存失效条件难对齐。
- 记住权衡：v-memo 本身有比较成本，**变化率低于 30% 的列表才值得**；高频全变的列表是负优化。

```vue
<!-- 一一对应：v-memo 万行列表只 diff 变化行 -->
<script setup>
import { ref } from 'vue';
const items = ref(/* 10 万条 */ []);
const selectedId = ref(null);
</script>

<template>
  <ul>
    <!-- 依赖只有"是否选中"：非选中状态切换到非选中状态 -> 整行跳过 diff -->
    <li
      v-for="item in items"
      :key="item.id"
      v-memo="[item.id === selectedId]"
      :class="{ active: item.id === selectedId }"
    >
      {{ item.name }} - {{ item.price }}
    </li>
  </ul>
</template>
<!-- 效果：点击选中某行，只有旧行+新行两行参与 diff，其余 99998 行直接复用缓存 -->

<!-- 陷阱示例：deps 写漏 -->
<!-- 反例：v-memo="[item.id]" 但模板里用了 item.count，count 更新后界面不刷新 -->
<!-- 反例 2：v-memo="[]" 永久缓存，挂载后任何数据更新都被跳过 -->

<!-- 正确的多依赖写法：把子树用到的所有变化源列全 -->
<li v-for="item in items" :key="item.id" v-memo="[item.count, selectedId, filter]">
  {{ item.name }} x{{ item.count }}
</li>

<!-- 选型对照：
  行内容整体频繁变化      -> 不用 v-memo，考虑虚拟列表
  大列表 + 少数行变化     -> v-memo（本例）
  组件级复用             -> 用组件 + props 记忆化，不用 v-memo -->
```
