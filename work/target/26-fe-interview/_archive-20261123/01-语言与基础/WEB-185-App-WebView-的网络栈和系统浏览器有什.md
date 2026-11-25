---
title: [WEB-185] App WebView 的网络栈和系统浏览器有什么差异？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-185：App WebView 的网络栈和系统浏览器有什么差异？
**答**：
- Android WebView 内嵌 Chromium 网络栈，但版本跟随系统 WebView 组件更新而非 App 自身——老设备能力差异大，要用特性检测兜底。
- iOS WKWebView 走系统 WebKit/URLSession 栈：HTTP/2 与 HTTP/3 支持度以 iOS 版本为准；App 原生网络层（OkHttp/Alamofire）又可能另配 HTTPDNS 或自实现协议。
- 坑点：WebView 与原生层的 Cookie、缓存互不共享；系统代理设置在两端生效范围不同。
- 实践：H5 里用特性检测而非 UA 判断能力；关键指标按端分开采集。

```javascript
// 端差异识别与能力兜底
const ua = navigator.userAgent;
const env = {
  androidWV: /;\s*wv\)/.test(ua) && /Android/.test(ua),   // Android WebView 特征
  iosWV: /iPhone|iPad/.test(ua) && !/Safari\//.test(ua),  // iOS 内嵌环境（非 Safari 主浏览器）
};
// 能力一律用特性检测，而不是只看 UA
const hasModernStorage = 'serviceWorker' in navigator && 'storage' in navigator;
// 需要端上能力（HTTPDNS、离线包、文件）时走 JSBridge
if (env.androidWV && window.NativeBridge?.setDns) {
  window.NativeBridge.setDns(JSON.stringify({ 'api.example.com': '203.0.113.7' }));
}
```
