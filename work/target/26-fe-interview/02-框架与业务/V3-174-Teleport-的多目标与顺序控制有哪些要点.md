---
title: [V3-174] Teleport 的多目标与顺序控制有哪些要点？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-174：Teleport 的多目标与顺序控制有哪些要点？
**答**：
- to 支持选择器与真实元素：动态目标（响应式 ref/计算属性）可以实现"弹窗挂到不同容器"。
- 多个 Teleport 到同一目标时按挂载顺序 append；需要控制层级用目标容器内的 CSS order 或不同 zIndex。
- disabled 属性：条件挂回原位置，做"内嵌/弹出双形态"组件很好用。
- 3.5 新增 defer：解决"目标容器由同一棵树更晚渲染"导致的挂载失败，Teleport 会等目标出现后再传送。

```vue
<script setup lang="ts">
import { ref } from "vue";

// 动态目标：弹窗可切换挂载位置（如全屏 / 挂在某个卡片内）
const target = ref<string>("#modal-root");
const inline = ref(false); // disabled 为 true 时内容留在原地渲染
</script>

<template>
  <button @click="target = target === '#modal-root' ? '#drawer-root' : '#modal-root'">
    切换挂载目标
  </button>

  <!-- 多个 Teleport 可共存：弹窗与抽屉各自的目标容器 -->
  <Teleport :to="target" :disabled="inline" defer>
    <div class="modal">
      内容（target：{{ target }}）
      <button @click="inline = !inline">切换内嵌形态</button>
    </div>
  </Teleport>

  <!-- 顺序/zIndex 控制：同一目标的多个 Teleport，用类名+zIndex 管层级 -->
  <Teleport to="#modal-root">
    <div class="toast" style="z-index: 3001">Toast 在弹窗之上</div>
  </Teleport>

  <div id="modal-root"></div>
  <div id="drawer-root"></div>
</template>

<style>
.modal { position: fixed; inset: 20% 30%; background: #fff; z-index: 3000; box-shadow: 0 4px 16px rgba(0,0,0,.2); padding: 24px; }
.toast { position: fixed; top: 16px; left: 50%; transform: translateX(-50%); background: #333; color: #fff; padding: 8px 16px; border-radius: 4px; }
</style>
```
