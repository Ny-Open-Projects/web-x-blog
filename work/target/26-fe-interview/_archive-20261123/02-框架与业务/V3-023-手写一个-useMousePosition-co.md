---
title: [V3-023] 手写一个 useMousePosition composable？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-023：手写一个 useMousePosition composable？
**答**：
- composable = "以 use 开头的函数 + 组合式 API 封装状态与副作用"。
- 内部创建 ref 状态，在生命周期钩子里注册/清理事件监听。
- 返回多个 ref 保持响应式，调用方按需解构。
- 多次调用各自独立实例，比 mixin 的单例共享更可控。

```vue
<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";

function useMousePosition() {
  const x = ref(0);
  const y = ref(0);

  const update = (e: MouseEvent) => {
    x.value = e.pageX;
    y.value = e.pageY;
  };

  onMounted(() => window.addEventListener("mousemove", update));
  onUnmounted(() => window.removeEventListener("mousemove", update));

  return { x, y };
}

const { x, y } = useMousePosition();
</script>

<template>
  <p>鼠标位置 {{ x }}, {{ y }}</p>
</template>
```
