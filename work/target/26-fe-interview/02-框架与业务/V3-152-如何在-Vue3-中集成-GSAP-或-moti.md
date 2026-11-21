---
title: [V3-152] 如何在 Vue3 中集成 GSAP（或 motion-v）这类动画库？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-152：如何在 Vue3 中集成 GSAP（或 motion-v）这类动画库？
**答**：
- 职责划分：简单状态过渡交给 Vue 的 CSS 类；进入离开编排、数字滚动、复杂 timeline 交给 gsap，通过 JS 钩子桥接。
- gsap.from/to 操作的就是钩子传入的 el，onComplete 里调用 done() 让 Vue 结束过渡。
- 列表场景：TransitionGroup 的 move 类负责补位动画，enter/leave 钩子用 gsap 做进场与退场，二者叠加不冲突。
- motion-v 是 motion 的 Vue 移植，思路相同但走声明式 props（:initial/:animate/:exit），适合声明式为主的团队。

```vue
<script setup lang="ts">
import { ref } from "vue";
import gsap from "gsap";

const list = ref(["A", "B", "C"]);

// enter/leave 走 gsap 编排，move 补位交给 CSS 类
function onEnter(el: Element, done: () => void) {
  gsap.from(el, { opacity: 0, y: 24, duration: 0.5, ease: "power2.out", onComplete: done });
}
function onLeave(el: Element, done: () => void) {
  gsap.to(el, { opacity: 0, y: 12, duration: 0.3, ease: "power1.in", onComplete: done });
}
function add() {
  list.value.push(String.fromCharCode(65 + list.value.length));
}
</script>

<template>
  <button @click="add">加一项</button>
  <TransitionGroup name="g" tag="ul" @enter="onEnter" @leave="onLeave">
    <li v-for="(item, i) in list" :key="item" class="row" @click="list.splice(i, 1)">
      {{ item }}（点击删除）
    </li>
  </TransitionGroup>
</template>

<style>
.g-move { transition: transform .4s ease; } /* 补位动画仍由 CSS 负责 */
.g-leave-active { position: absolute; }     /* 离场脱离文档流 */
.row { width: 260px; }
</style>
```
