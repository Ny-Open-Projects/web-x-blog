---
title: [WEB-047] dns-prefetch、preconnect、preload、prefetch 有什么区别？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-047：dns-prefetch、preconnect、preload、prefetch 有什么区别？
**答**：
- `dns-prefetch`：提前做 DNS 解析，只省 DNS 时间；`preconnect`：DNS + TCP + TLS 一步到位，收益更大，只对关键第三方域用。
- `preload`：当前页面马上要用的关键资源（字体、首屏 CSS/JS），高优先级提前下载。
- `prefetch`：下一跳可能用的资源，空闲时低优先级下载。
- 滥用反而抢带宽，preconnect 一般控制在 2~4 个关键域。

```html
<!-- 资源提示完整示例 -->
<head>
  <!-- 1. DNS 预解析：低成本的域名预热 -->
  <link rel="dns-prefetch" href="//cdn.example.com" />

  <!-- 2. 预连接：握手全做完，适合马上要请求的第三方域 -->
  <link rel="preconnect" href="https://cdn.example.com" crossorigin />
  <link rel="preconnect" href="https://api.example.com" />

  <!-- 3. preload：当前页关键资源，as 声明类型 -->
  <link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="preload" href="/static/app.css" as="style" />

  <!-- 4. prefetch：下一跳路由可能用到的资源，空闲时下载 -->
  <link rel="prefetch" href="/static/detail-page.js" as="script" />
</head>
```

## 九、浏览器渲染流程
