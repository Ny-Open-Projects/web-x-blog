---
title: [H5-261] TWA 与 PWA 上架应用商店的路径
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-261：TWA 与 PWA 上架应用商店的路径

**答**：
- TWA（Trusted Web Activity）：把 PWA 用 WebView 一样的容器（Custom Tab，无地址栏）包装成 Android APK 上架 Google Play——内容仍是 Web，外壳是原生
- 依赖条件：站点通过 Digital Asset Links 校验（assetlinks.json 放在 /.well-known/，包名与签名匹配），否则 TWA 里会显示地址栏
- iOS 侧：没有官方 TWA，用 WKWebView 壳（如 Capacitor）或直接上架 PWA 的快捷方式能力有限——体验降级明显
- 成本权衡：TWA 复用全部 Web 代码与更新（无需发版审核热更），但依赖商店审核外壳包
- 加分项：说出「TWA 崩溃=Web 事故、原生壳崩溃=App 事故」的监控分界

```json
// /.well-known/assetlinks.json（简化）
[{ "relation": ["delegate_permission/common.handle_all_urls"],
   "target": { "namespace": "android_app",
     "package_name": "com.example.app",
     "sha256_cert_fingerprints": ["AB:CD:..."] } }]
```
