---
title: [OPT-009] 如何按场景选资源提示词？preload/prefetch/dns-prefetch/preconnect 实战选型
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-009：如何按场景选资源提示词？preload/prefetch/dns-prefetch/preconnect 实战选型

**答**：
- `preload`：**当前页面**马上要用的高优资源（关键字体、LCP 图、核心 CSS/JS），误用会造成带宽挤占和重复加载告警。
- `prefetch`：**下一次导航**可能用到的资源，空闲期低优先级下载，常用于预取下一页的 JS chunk。
- `preconnect`：提前完成 DNS + TCP + TLS 三步建连，适合确定要请求的第三方域（字体域、API 域）。
- `dns-prefetch`：只提前 DNS 解析，作为不支持 preconnect 浏览器的兜底，两者可并存。

```html
<!-- 一一对应：四种资源提示的正确分工 -->
<link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossorigin />
<link rel="preload" href="/img/lcp-hero.avif" as="image" fetchpriority="high" />

<link rel="preconnect" href="https://api.example.com" crossorigin />
<link rel="dns-prefetch" href="https://api.example.com" />

<!-- 预取下一页 chunk：用户大概率点击的详情页 -->
<link rel="prefetch" href="/js/detail-page.chunk.js" />
```
