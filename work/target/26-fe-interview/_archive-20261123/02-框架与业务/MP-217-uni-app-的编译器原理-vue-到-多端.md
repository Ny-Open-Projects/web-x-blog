---
title: [MP-217] uni-app 的编译器原理：Vue 模板怎么转成各端？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-217：uni-app 编译器原理？
**答**：
- Vue SFC → 平台产物：小程序端把模板编译成 WXML/UDL（指令映射 v-if→wx:if、v-for→wx:for），样式转 wxss/acss，JS 保留 Vue 运行时。
- Vue2 时代模板静态编译 + 数据驱动（setData）；Vue3（uni-app x / uni-app vue3）：编译成组合式 API + 精细化 setData（基于 @dcloudio/uni-cli-shared）。
- App 端：uni-app x 用uts 编译为 Kotlin/Swift 原生渲染；老版 app 用 WebView 渲染 + JSBridge。
- 条件编译：#ifdef MP-WEIXIN / APP-PLUS 注释指令块级裁剪。
- 与 Taro 对比：uni-app 编译时比重更大（模板直接转），Taro 运行时比重更大（React 完整心智）。
