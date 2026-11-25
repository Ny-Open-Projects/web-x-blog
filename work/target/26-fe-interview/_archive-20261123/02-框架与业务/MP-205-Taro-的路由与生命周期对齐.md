---
title: [MP-205] Taro 怎么把 React 路由/生命周期对齐到小程序？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-205：Taro 路由与生命周期对齐？
**答**：
- 页面 = 小程序页面实例 + React 组件容器：每个页面独立 React root，路由参数从 onLoad options 注入（useRouter）。
- 生命周期映射：componentDidMount ↔ onLoad+onReady、页面隐藏 ↔ onHide（onShow 同理）、卸载 ↔ onUnload；Tab 页常驻（不卸载）。
- 兼容差异：小程序无「前进后退历史栈操作」（navigateBack 不能带参数回传）——Taro 提供 eventCenter/全局 store 补偿。
- 跨页面通信：Taro 的 events 模块（全局事件总线）或页面实例间传参。
- Hook 层：useDidShow/useDidHide 等把小程序生命周期做成 React hooks。
