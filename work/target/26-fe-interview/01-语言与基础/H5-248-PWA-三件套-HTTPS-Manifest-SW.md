---
title: [H5-248] PWA 三件套是什么：HTTPS-Manifest-SW
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-248：PWA 三件套是什么：HTTPS、Manifest、SW

**答**：
- HTTPS：Service Worker 只在安全上下文注册（localhost 除外）——没有 HTTPS 一切免谈
- Manifest：JSON 清单声明应用名/图标/主题色/display 模式/start_url，是「可安装」的前提
- Service Worker：可编程的网络代理，负责离线缓存、请求拦截、消息推送——PWA 的灵魂
- 三者关系：HTTPS 是地基，Manifest 是身份证，SW 是发动机；「可安装 = HTTPS + 合法 Manifest + SW 处理 fetch」
- 面试话术：PWA 不是单个技术，是「让 Web 达到原生 App 体验」的工程组合，逐项说清能力边界

```json
{
  "name": "商店助手",
  "short_name": "商店",
  "start_url": "/?source=pwa",
  "display": "standalone",
  "background_color": "#fff",
  "theme_color": "#3367d6",
  "icons": [{ "src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable" }]
}
```
