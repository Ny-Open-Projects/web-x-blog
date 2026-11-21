---
title: [V3-149] Transition 的完整用法有哪些？JS 钩子怎么配合 CSS 类使用？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-149：Transition 的完整用法有哪些？JS 钩子怎么配合 CSS 类使用？
**答**：
- 完整清单：name 命名类、mode="out-in|in-out" 控制新旧元素时序、appear 首次渲染也过渡、enter/leave 六段类名。
- JS 钩子四件套：@before-enter、@enter、@leave、@after-enter；用了 JS 钩子通常配 `:css="false"` 跳过类名探测，由 done() 显式收尾。
- 典型组合：列表项用 CSS 管 hover 等简单过渡，进出场用 JS 钩子接 Web Animations API 或 gsap。
- 注意点：Transition 只对单元素/单组件生效，切换靠 key 或 v-if/v-else 分支。

```vue
<script setup lang="ts">
import { ref } from "vue";

const status = ref<"loading" | "done">("loading");

// JS 钩子：用 Web Animations API，done() 收尾（也可配 :css="false" 跳过类名探测）
function onBeforeEnter(el: Element) {
  (el as HTMLElement).style.opacity = "0";
}
function onEnter(el: Element, done: () => void) {
  (el as HTMLElement)
    .animate(
      [
        { opacity: 0, transform: "translateY(-20px)" },
        { opacity: 1, transform: "translateY(0)" },
      ],
      { duration: 400, easing: "ease-out" }
    )
    .onfinish = done; // 必须调用 done，Vue 才知道动画结束
}
function onLeave(el: Element, done: () => void) {
  (el as HTMLElement)
    .animate([{ opacity: 1 }, { opacity: 0, transform: "translateY(20px)" }], {
      duration: 300,
      easing: "ease-in",
    })
    .onfinish = done;
}

function finish() {
  status.value = status.value === "loading" ? "done" : "loading";
}
</script>

<template>
  <!-- mode out-in：先离场再进场，避免两个状态叠在一起 -->
  <Transition mode="out-in" appear @before-enter="onBeforeEnter" @enter="onEnter" @leave="onLeave">
    <p :key="status" class="status">{{ status === "loading" ? "加载中..." : "加载完成" }}</p>
  </Transition>
  <button @click="finish">切换状态</button>
</template>

<style>
.status { font-weight: bold; }
</style>
```
