---
title: [DP-131] `<component :is>` 的工厂用法如何落地？动态组件与工厂模式的关系？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-131：`<component :is>` 的工厂用法如何落地？动态组件与工厂模式的关系？（高频）
**答**：
- `<component :is>` 是运行时组件工厂：以"类型字符串/组件对象"为参数产出组件实例，对应 DP-018 schema 动态表单的渲染端。
- 规范用法：组件映射表（白名单）+ markRaw 包组件对象（避免被响应式代理导致性能损耗与告警）；shallowRef 存"当前组件"。
- 组合场景：低代码物料渲染、后台配置化卡片、权限下替换组件（工厂 + 策略）。

```vue
<script setup>
import { shallowRef, markRaw, computed } from 'vue';
import ChartCard from './ChartCard.vue';
import TableCard from './TableCard.vue';
import RichCard from './RichCard.vue';
// 工厂的"产品目录"：白名单映射，避免任意字符串渲染（安全）
const catalog = markRaw({ chart: ChartCard, table: TableCard, rich: RichCard });
const config = ref({ widgets: [{ type: 'chart', props: { api: '/stat' } }, { type: 'table' }] });
const resolve = (type) => catalog[type] ?? FallbackCard;                // 工厂函数：type → 组件
const activeType = shallowRef('chart');
const activeComp = computed(() => resolve(activeType.value));
</script>
<template>
  <component :is="activeComp" v-bind="activeProps" />                    <!-- 工厂渲染：is 接组件对象 -->
  <!-- schema 驱动：遍历配置产出整个面板（工厂 + 组合） -->
  <template v-for="w in config.widgets" :key="w.type">
    <component :is="resolve(w.type)" v-bind="w.props" />
  </template>
</template>
```

---

## 十六、数据层模式
