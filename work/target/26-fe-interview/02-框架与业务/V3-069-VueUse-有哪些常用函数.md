---
title: [V3-069] VueUse 有哪些常用函数？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-069：VueUse 有哪些常用函数？
**答**：
- 状态类：useLocalStorage/useSessionStorage（响应式存储）、useDark（暗色模式）。
- 副作用类：useDebounceFn/useThrottleFn、useEventListener（自动清理监听）。
- 感知类：useMouse、useIntersectionObserver（进入视口）、useResizeObserver。
- 它是组合式 API 最佳实践的集合，源码值得当作 composable 教材阅读。

```vue
<script setup lang="ts">
import {
  useLocalStorage, // 响应式 localStorage
  useDebounceFn, // 防抖函数
  useIntersectionObserver, // 元素进入视口
  useDark, // 暗色模式切换
  useMouse, // 鼠标位置
} from "@vueuse/core";
import { ref } from "vue";

const settings = useLocalStorage("settings", { theme: "light", lang: "zh" });
const search = useDebounceFn(
  (kw: string) => console.log("搜索：", kw),
  300
);
const { x, y } = useMouse();
const isDark = useDark();

// 图片进入视口后再加载
const target = ref<HTMLElement | null>(null);
const { stop } = useIntersectionObserver(target, ([entry]) => {
  if (entry?.isIntersecting) {
    console.log("进入视口，加载资源");
    stop();
  }
});
</script>

<template>
  <p>{{ x }}, {{ y }} - {{ settings.theme }} - {{ isDark }}</p>
  <input @input="search(($event.target as HTMLInputElement).value)" />
  <div ref="target">观察目标</div>
</template>
```
