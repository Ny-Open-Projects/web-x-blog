---
title: [WEB-057] PWA 由哪几部分组成？manifest 常配哪些字段？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-057：PWA 由哪几部分组成？manifest 常配哪些字段？
**答**：
- 三大件：Web App Manifest（安装与图标）、Service Worker（离线与请求代理）、HTTPS（安全前提）。
- manifest 关键字段：`name/short_name`、`start_url`、`display: standalone`、`theme_color/background_color`、`icons`（含 192/512 尺寸）。
- 配合 SW 的缓存策略可达到可安装、离线可用、类原生体验；更新靠 SW 版本化与 skipWaiting 流程。
- 加分项：说清 PWA 与小程序/原生 App 的取舍（触达快、能力受限、分发不依赖商店）。

```html
<!-- index.html：引入 manifest 与主题色 -->
<link rel="manifest" href="/manifest.json" />
<meta name="theme-color" content="#3367d6" />
<link rel="apple-touch-icon" href="/icons/icon-192.png" />
```

```json
{
  "name": "Fe Interview PWA",
  "short_name": "FeQuiz",
  "start_url": "/?source=pwa",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#3367d6",
  "icons": [
    { "src": "/icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icons/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```
