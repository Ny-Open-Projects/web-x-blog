---
title: [V3-001] Vue3 相比 Vue2 有哪些核心变化？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-001：Vue3 相比 Vue2 有哪些核心变化？
**答**：
- 响应式从 Object.defineProperty 换成 Proxy，支持新增/删除属性、数组索引与 length。
- 新增组合式 API（setup、ref、computed 等），逻辑复用从 mixin 转向 composable。
- 编译期优化：静态提升、patchFlag、block tree，diff 更快；支持 Fragment 多根节点。
- 全面支持 TypeScript、新增 Teleport/Suspense/KeepAlive 内置组件、移除 filter 与 \$on 等 API。

```vue
<script setup lang="ts">
import { ref, computed } from "vue";

// 组合式 API：按功能组织逻辑，类型推断友好
const count = ref(0);
const double = computed(() => count.value * 2);
</script>

<template>
  <!-- Fragment：模板可以有多个根节点 -->
  <button @click="count++">count 加一</button>
  <p>{{ count }} - {{ double }}</p>
</template>
```
