---
title: [V3-045] defineAsyncComponent 如何使用？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-045：defineAsyncComponent 如何使用？
**答**：
- 基本用法传工厂函数 `() => import('./X.vue')`，组件按需拆 chunk、用到时才加载。
- 高级配置：delay 控制 loading 出现时机避免闪烁、timeout 超时报错。
- loadingComponent/errorComponent 分别指定加载中与失败兜底组件。
- onError 回调支持失败重试，常配合弱网环境。

```vue
<script setup lang="ts">
import { defineAsyncComponent } from "vue";

// 路由级大组件按需拆包，首屏不加载
const HeavyEditor = defineAsyncComponent({
  loader: () => import("./HeavyEditor.vue"),
  delay: 200, // 超过 200ms 才显示 loading，避免闪烁
  timeout: 10000, // 超时判定为加载失败
  loadingComponent: () => import("./Loading.vue"),
  errorComponent: () => import("./ErrorBox.vue"),
  onError(error, retry, fail, attempts) {
    if (attempts <= 2) retry(); // 失败自动重试两次
    else fail();
  },
});
</script>

<template>
  <HeavyEditor />
</template>
```

## 第十二章 自定义指令
