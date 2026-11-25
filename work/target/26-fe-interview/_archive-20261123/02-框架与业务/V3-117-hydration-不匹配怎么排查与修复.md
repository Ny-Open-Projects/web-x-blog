---
title: [V3-117] hydration 不匹配怎么排查与修复？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-117：hydration 不匹配怎么排查与修复？
**答**：
- 常见来源：渲染了依赖环境的数据（Date.now、Math.random、window 尺寸）、服务端与客户端 v-if 条件不同、非法 HTML 嵌套被浏览器纠正（p 里套 div）。
- 排查：开发模式下 Vue 会在控制台打印不匹配的节点与两份渲染文本；按打印定位到具体表达式。
- 修复模式：环境相关值先渲染占位，onMounted 后再补真实值；纯客户端内容用 `<ClientOnly>`（Nuxt）或挂载标记包裹。
- 大面积不匹配宁可让该子树客户端独占渲染，也不要逐个补丁。

```vue
<!-- hydration 修复示例：环境相关内容延迟到客户端 -->
<script setup lang="ts">
import { onMounted, ref } from "vue";

// 错误写法：const now = ref(Date.now())
// 服务端渲染的时间与客户端 hydrate 时的时间几乎必然不同，触发不匹配警告

// 正确写法：SSR 渲染占位，客户端挂载后再补真实值
const now = ref<number | null>(null);
onMounted(() => {
  now.value = Date.now();
});
</script>

<template>
  <!-- 两端渲染结果一致：都是占位骨架 -->
  <p v-if="now === null" class="skeleton">--:--:--</p>
  <!-- hydrate 完成后 onMounted 触发，安全切换为真实时间 -->
  <p v-else>当前时间：{{ new Date(now).toLocaleTimeString() }}</p>
</template>
```
