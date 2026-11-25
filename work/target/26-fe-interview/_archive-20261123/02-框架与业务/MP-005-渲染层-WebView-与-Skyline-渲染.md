---
title: [MP-005] 渲染层 WebView 与 Skyline 渲染引擎有什么区别？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-005：渲染层 WebView 与 Skyline 渲染引擎有什么区别？
**答**：
- WebView 渲染：每个页面一个 WebView（iOS WKWebView / Android chromium），逻辑层与渲染层天然隔离，setData 只能异步。
- Skyline：微信自研渲染引擎，渲染层不再用 WebView，改为轻量原生渲染管线；支持逻辑层与渲染层**同线程同步通信**，省去序列化跨线程开销，setData 更快。
- Skyline 启动更快、包内不依赖完整 WebView 环境、支持工作线程，但 **CSS 是子集**（不支持部分选择器、伪类、float 等），需按官方支持列表编写样式。
- 开启需要 `rendererOptions.skyline` + `componentFramework: "glass-easel"`，并配合 lazyCodeLoading。

```json
{
  "rendererOptions": {
    "skyline": {
      "defaultDisplayBlock": true,
      "defaultContentBox": true,
      "disableABTest": true
    }
  },
  "componentFramework": "glass-easel",
  "lazyCodeLoading": "requiredComponents"
}
```
