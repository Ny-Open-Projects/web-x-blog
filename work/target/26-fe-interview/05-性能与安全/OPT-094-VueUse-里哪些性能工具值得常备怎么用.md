---
title: [OPT-094] VueUse 里哪些性能工具值得常备？怎么用？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-094：VueUse 里哪些性能工具值得常备？怎么用？

**答**：
- 四件套：`useThrottleFn`（高频事件收敛）、`useDebounceFn`（最终态收敛）、`useRafFn`（对齐渲染帧的循环）、`useIdleCallback`/`useTimeoutFn`（低优先级让路）。
- 价值在于**与响应式系统打通**：`watchWithFilter`/`refDebounced` 让"响应式数据变化 -> 高成本动作"自带节流策略，不用手写胶水代码。
- 常用组合：`refDebounced(keyword)` 驱动搜索请求；`useThrottleFn` 包 scroll 回调；`useEventListener` 自动随组件卸载解绑（兼治监听泄漏）。
- 注意参数语义与手写节流一致：throttle 的 trailing/leading、debounce 的 maxWait 都有，选错参数等于没优化。

```vue
<!-- 一一对应：VueUse 性能四件套在列表页的组合落地 -->
<script setup>
import {
  refDebounced, useThrottleFn, useRafFn, useEventListener, watchDebounced,
} from '@vueuse/core';
import { ref, watch } from 'vue';

const keyword = ref('');
const scrollY = ref(0);
const progress = ref(0);

// ① refDebounced：防抖后的搜索词，请求与重过滤都吃它
const debouncedKeyword = refDebounced(keyword, 300);
watchDebounced(keyword, (kw) => fetchResults(kw), { debounce: 300, maxWait: 1000 });
// maxWait 保证连续输入时最迟 1s 必发一次请求，防饿死

// ② useThrottleFn：scroll 收敛到 100ms 一次
const onScroll = useThrottleFn(() => {
  scrollY.value = window.scrollY;
}, 100, true); // trailing: true 保证最后一次位置不丢

// ③ useEventListener：绑定即自动随组件卸载解绑，兼治监听器泄漏
useEventListener(window, 'scroll', onScroll, { passive: true });

// ④ useRafFn：与渲染对齐的连续动画/进度计算
const { pause } = useRafFn(() => {
  progress.value = Math.min(1, window.scrollY / document.body.scrollHeight);
});
// 组件卸载自动 pause（useRafFn 内部随 scope 清理）；也可手动 pause() 省电

// ⑤ useIdleCallback：埋点类低优先级任务压到空闲期
import { useIdleCallback } from '@vueuse/core';
// useIdleCallback(() => preloadNextPage(), { timeout: 3000 });
</script>

<template>
  <input v-model="keyword" />
  <div class="progress" :style="{ transform: `scaleX(${progress})` }" />
</template>
```
