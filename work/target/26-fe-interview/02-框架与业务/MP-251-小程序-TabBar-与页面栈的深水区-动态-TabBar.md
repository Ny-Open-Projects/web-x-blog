---
title: [MP-251] 动态 TabBar（自定义 TabBar）的实现与坑？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-251：动态 TabBar 的实现与坑？
**答**：
- custom-tab-bar：app.json tabBar.custom=true + custom-tab-bar/index 组件——每个 tab 页持有独立实例（状态不共享）。
- 状态同步：selected 状态要在每个 tab 页 onShow 里 setData（这是最大坑——切 tab 后高亮错位）。
- 动态化：角标/红点/权限隐藏——组件内 store 订阅 + 各页 onShow 触发刷新。
- 性能：自定义 TabBar 是每页一份——组件要轻；图标走 CDN 或小体积。
- 兼容：custom tabbar 与原生切换动画差异、iPhone 底部安全区（env(safe-area-inset-bottom)）。
