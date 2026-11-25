---
title: [V3-020] watch 的 flush 时机有哪几种？对应哪些 API？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-020：watch 的 flush 时机有哪几种？对应哪些 API？
**答**：
- pre（默认）：回调在组件更新前执行，同一 tick 内多次变更只调一次。
- post：回调在组件更新后执行，能拿到更新后的 DOM，等价 API 是 watchPostEffect。
- sync：依赖变化立即同步执行，不做批处理，等价 API 是 watchSyncEffect。
- 需要操作"最新 DOM"的场景一律用 post，避免手动 nextTick。

```vue
<script setup lang="ts">
import { ref, watchEffect, watchPostEffect, watchSyncEffect } from "vue";

const count = ref(0);

// flush: 'pre'（默认）：组件更新前执行
watchEffect(() => console.log("pre", count.value));

// flush: 'post'：组件更新后执行，等价于 watchPostEffect
watchPostEffect(() => {
  // 可安全访问更新后的 DOM
  console.log("post", document.title);
});

// flush: 'sync'：依赖变化立即同步执行，等价于 watchSyncEffect
watchSyncEffect(() => console.log("sync", count.value));
</script>
```

## 第四章 组合式 API 与逻辑复用
