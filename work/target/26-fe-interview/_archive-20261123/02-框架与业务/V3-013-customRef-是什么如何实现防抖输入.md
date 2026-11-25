---
title: [V3-013] customRef 是什么？如何实现防抖输入？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-013：customRef 是什么？如何实现防抖输入？
**答**：
- customRef 允许自定义 track 与 trigger 的时机，是"手写响应式行为"的出口。
- 工厂函数接收 { track, trigger }，返回带 get/set 的对象。
- 经典应用：防抖 ref——set 时延迟 trigger，输入停止 N ms 后才更新视图。
- 也可用于 sync ref（立即同步）、与本地存储同步的 ref 等。

```vue
<script setup lang="ts">
import { customRef } from "vue";

function useDebouncedRef(initial: string, delay = 300) {
  let timer: ReturnType<typeof setTimeout>;
  return customRef((track, trigger) => ({
    get() {
      track(); // 声明依赖
      return initial;
    },
    set(newValue) {
      clearTimeout(timer);
      timer = setTimeout(() => {
        initial = newValue;
        trigger(); // 延迟派发更新，实现防抖
      }, delay);
    },
  }));
}

const keyword = useDebouncedRef("");
</script>

<template>
  <input v-model="keyword" placeholder="输入停止 300ms 后更新" />
  <p>{{ keyword }}</p>
</template>
```
