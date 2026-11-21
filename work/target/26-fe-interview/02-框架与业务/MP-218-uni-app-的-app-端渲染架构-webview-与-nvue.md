---
title: [MP-218] uni-app 的 App 端渲染：WebView 与 nvue 的双引擎？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-218：uni-app App 端双引擎？
**答**：
- 默认引擎：页面跑在 WebView（每页一个或共用），Vue 组件直接渲染——生态兼容最好，性能中等。
- nvue（native vue）：weex 引擎原生渲染——长列表/动画/视频类页面性能高；但 CSS 受限（flex 布局子集）、生态组件少。
- 混合策略：多数页面 vue、性能热点页 nvue，页面级选择引擎。
- uni-app x：UTS 语言编译原生（Kotlin/Swift），组件树直映 ArkUI/原生 View——新一代方案，摆脱 WebView。
- 选型：常规业务 WebView 足够；游戏化/直播/超长列表才值得 nvue/x 的维护成本。
