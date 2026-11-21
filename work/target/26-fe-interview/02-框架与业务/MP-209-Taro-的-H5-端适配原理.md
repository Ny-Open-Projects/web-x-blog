---
title: [MP-209] Taro 的 H5 端适配原理是什么？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-209：Taro H5 端适配原理？
**答**：
- 同一套 React/Vue 组件树，H5 端用真实 DOM host（不再需要 BOM 垫片）——组件库 API 层面抹平（View→div、ScrollView→scroll 容器封装）。
- 路由：react-router/vue-router 映射小程序页面路径；TabBar → 底部导航组件。
- API：wx.xxx → H5 实现层（@tarojs/taro-h5）——如 showToast→toast 库、chooseImage→input file。
- 差异域：支付/登录（H5 走各自 SDK）、分包（H5 无分包概念）、分享（微信 JS-SDK）。
- 设计哲学：一次多端不是「像素级一致」，而是「能力对齐 + 条件编译补差异」。
