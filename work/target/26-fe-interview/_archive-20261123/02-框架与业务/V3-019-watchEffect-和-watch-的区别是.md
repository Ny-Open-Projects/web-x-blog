---
title: [V3-019] watchEffect 和 watch 的区别是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-019：watchEffect 和 watch 的区别是什么？
**答**：
- watch 懒执行、需要显式声明数据源、回调拿到新旧值；watchEffect 立即执行、自动收集依赖、没有新旧值。
- watchEffect 适合"多个依赖都要跑副作用"的场景，依赖声明写在函数体里。
- 两者都返回 stop 函数，组件卸载时自动停止。
- 副作用需要清理时用 onCleanup 回调，常用于取消上一次请求。

```vue
<script setup lang="ts">
import { ref, watchEffect, watch } from "vue";

const id = ref(1);

// watchEffect：立即执行，自动收集依赖
const stop = watchEffect(async (onCleanup) => {
  const controller = new AbortController();
  onCleanup(() => controller.abort()); // 依赖变化/组件卸载前取消上次请求
  await fetch(`/api/user/${id.value}`, { signal: controller.signal });
});

// watch：懒执行，需要指明数据源，有新旧值
watch(id, (newId, oldId) => {
  console.log(`id 从 ${oldId} 变成 ${newId}`);
});

stop(); // 手动停止（一般不需要）
</script>
```
