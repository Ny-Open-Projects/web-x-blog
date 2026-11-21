---
title: [V3-018] watch 的 deep、immediate、once、flush 选项分别做什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-018：watch 的 deep、immediate、once、flush 选项分别做什么？
**答**：
- deep: true 深层遍历监听对象内部变化；对 ref 包裹的对象默认不深，需要手动开。
- 加分点：Vue 3.5+ 的 deep 可以传数字（如 `deep: 2`），限制遍历深度，在大对象上比 `deep: true` 更省性能。
- immediate: true 立即以当前值执行一次回调，常用于初始化拉取数据。
- once: true（3.4+）只触发一次后自动停止。
- flush: 'pre'（默认，组件更新前）/ 'post'（更新后，可读 DOM）/ 'sync'（同步立即）。

```vue
<script setup lang="ts">
import { ref, watch } from "vue";

const form = ref({ name: "", tags: [] as string[] });

watch(
  form,
  (val) => console.log("form changed", val),
  {
    deep: true, // ref 包对象默认不深监听，需要手动开启
    immediate: true, // 立即以当前值执行一次，常用于初始化请求
    once: true, // 3.4+：只触发一次后自动停止
    flush: "post", // DOM 更新后再执行，可安全读取最新 DOM
  }
);

// 手动停止监听（组件卸载时自动停止）
const stop = watch(form, () => {});
stop();
</script>
```
