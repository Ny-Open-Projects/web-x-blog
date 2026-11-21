---
title: [WCN-086] Vue Vapor 模式是什么？去掉 VDOM 后更新如何工作？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-086：Vue Vapor 模式是什么？去掉 VDOM 后更新如何工作？

**答**：
- Vapor：Vue 3 的编译目标模式（实验性），编译器直接输出"操作真实 DOM 的更新函数"，跳过 VDOM 创建与 diff，包体更小、更新更快。
- 工作方式：模板编译时识别出动态绑定，为每处绑定生成独立的"更新 effect"（`renderEffect`），effect 内直接 `el.textContent = x.value` / `el.setAttribute`。
- 控制流：`v-if/v-for` 编译为 `createIf/createFor` 助手，内部维护分支缓存与 keyed 子块，块级复用而非全量重渲染。
- 与现有 Vue 关系：同一 SFC 语法，编译目标不同（vdom vs vapor）；组合式 API 语义不变，ref/watch/computed 行为一致——学习成本接近零。
- 意义：Vue 内核从"运行时 diff"迁移到"编译时定位 + 运行时细粒度"，与 Solid/Vapor 阵营趋同；SSR 水合也更快（无 vdom 树比对）。

```vue
<!-- Counter.vue（vapor 模式编译示意） -->
<template>
  <span>{{ count }}</span>
  <button @click="count++">+1</button>
</template>
<script setup>
import { ref } from 'vue';
const count = ref(0);
</script>

<!-- 编译产物（伪码）：没有 vnode，只有直接 DOM 操作 -->
// const span = h('span');
// renderEffect(() => setText(span, count.value));
// btn.__onClick = () => count.value++;   // 触发 effect 直改 span
```
