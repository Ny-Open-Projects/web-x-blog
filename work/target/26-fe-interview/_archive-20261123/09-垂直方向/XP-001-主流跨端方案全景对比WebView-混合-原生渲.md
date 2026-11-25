---
title: [XP-001] 主流跨端方案全景对比？WebView 混合、原生渲染、自绘引擎、编译时方案的差异？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-001：主流跨端方案全景对比？WebView 混合、原生渲染、自绘引擎、编译时方案的差异？
**答**：
- **WebView 混合**（Cordova/Ionic/Hybrid App）：UI 全部用 H5，容器提供桥接 API；开发成本低、动态化最强，但受 WebView 内核性能与 JSBridge 序列化开销制约。
- **原生渲染**（React Native 新架构）：JS 写业务，UI 映射为系统原生控件；交互体验接近原生，但受桥接（旧架构）与布局到原生映射（平台差异）影响。
- **自绘引擎**（Flutter）：不依赖原生控件，Skia/Impeller 直接绘制像素；三端像素级一致，但包体积大、动态化受限、无浏览器生态。
- **编译时方案**（Taro/uni-app/Rax）：同一 DSL 编译到小程序/RN/H5 多目标；一套代码覆盖面最广，但受目标端能力上限约束，运行时适配层有损耗。
- 选型本质是 **性能上限 vs 动态化 vs 一致性 vs 生态** 四角权衡，没有银弹。

```text
方案            渲染方式        性能上限    动态化        一致性    生态/上手
WebView 混合    浏览器内核      低-中       极强(免发版)  差        前端零成本
RN 新架构       原生控件映射    中-高       强(热更新)    中        React 生态
Flutter         Skia/Impeller   高          弱(需发版/壳) 极强      Dart 生态
编译时 Taro     各端各自渲染    取决于目标  中           中        React/Vue 语法
小程序原生      双线程+原生     中          强(审核发布)  各家不一  各家私有 DSL
Electron        Chromium        中          强(整包更新) 强        Node + Web
```
