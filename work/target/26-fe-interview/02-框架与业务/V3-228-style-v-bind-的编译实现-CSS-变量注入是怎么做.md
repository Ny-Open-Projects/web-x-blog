---
title: [V3-228] `<style v-bind>`（样式绑定 JS 变量）的编译实现是怎么做的？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-228：`<style v-bind>`（样式绑定 JS 变量）的编译实现是怎么做的？
**答**：
- 原理：编译器扫描 style 块中 `v-bind(color)`，把它替换为 CSS 变量 `var(--hash-color)`，同时往组件 setup 返回值注入 `useCssVars` 调用。
- 运行时：`useCssVars` 在组件挂载/更新后把变量值写到组件根元素的 style 上（SSR 则内联到 HTML），选择器通过作用域 id 限定在组件内。
- 变量命名：编译器按变量名 + 组件 hash 生成唯一 key，避免多实例冲突；绑定响应式 ref 后改值即改样式，零重渲染。
- 价值：主题色、进度条宽度等"JS 状态驱动样式"场景不进 JS patch 路径，直接 CSS 变量生效，性能优于 :style 绑定。
- 对比：`:style="{ color }"` 走 props/attr patch；v-bind 走 CSS 变量，适合子元素深层使用场景（style 对象不必层层透传）。

```vue
<script setup>
import { ref } from 'vue';
const theme = ref('#409eff'); // 改变它，样式即时生效，不触发组件重渲染
</script>
<template><div class="card"><span>标题</span></div></template>
<style scoped>
.card { padding: 12px; }
.card span {
  color: v-bind(theme);            /* 编译为 color: var(--6f2a1e0c-theme) */
  border-bottom-color: v-bind('theme.toUpperCase()'); /* 表达式也支持 */
}
</style>
<!-- 编译产物（示意）：setup 返回 __vccOpts 且注入
useCssVars(() => ({ '--6f2a1e0c-theme': theme.value, ... }))
-> 挂载后 el.style.setProperty('--6f2a1e0c-theme', theme.value) -->
```
