---
title: [MP-067] uni-app 的实现原理是什么？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-067：uni-app 的实现原理是什么？
**答**：
- 组成：**编译器**（vue 单文件组件编译到各端：H5 直接运行、小程序生成 wxml/wxss/js、App 端生成 nvue/weex 或 webview 渲染）+ **运行时**（各端适配层，统一 vue API 与 uni.xxx API）。
- 以 Vue 语法为中心，通过条件编译抹平差异；小程序端产物接近原生代码（编译时为主），复杂特性靠运行时适配。
- App 端双渲染引擎：webview 渲染（常规 vue 页）与 nvue 原生渲染（weex）。

```vue
<!-- uni-app 页面：Vue 语法编译到各端 -->
<template>
  <view class="content">
    <text>{{ title }}</text>
    <button @click="onTap">点击</button>
  </view>
</template>

<script>
export default {
  data: () => ({ title: 'uni-app' }),
  methods: {
    onTap() { uni.showToast({ title: 'clicked' }) }   // 统一 API 层
  }
}
</script>
```
