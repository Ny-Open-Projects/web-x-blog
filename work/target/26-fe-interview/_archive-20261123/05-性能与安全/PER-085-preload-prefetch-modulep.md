---
title: [PER-085] preload/prefetch/modulepreload/dns-prefetch 的决策矩阵是什么？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-085：preload/prefetch/modulepreload/dns-prefetch 的决策矩阵是什么？

**答**：
- 决策矩阵：**preload**（当前导航必然要用的关键资源，提前到发现之前）、**modulepreload**（ESM 入口，自动解析并预取依赖图）、**prefetch**（下一跳导航大概率要用的资源，空闲时取）、**dns-prefetch**（只提前 DNS，适合第三方域名）、**preconnect**（DNS+TCP+TLS 全握手，适合必然要连的第三方）。
- 判断顺序：当前页关键路径用 preload，跨页复用用 prefetch，第三方关键域用 preconnect，冷门第三方用 dns-prefetch。
- 两个高频坑：preload 未被使用会触发控制台警告并浪费带宽（别 preload 视口外图片）；对带凭据的跨域请求 preload 要配 `crossorigin` 正确值，否则二次下载。
- prefetch 与 SW 的组合：路由级 prefetch 由 SW 拦截实现更可控（可统计命中率）。

```html
<!-- 决策矩阵落地示例：电商详情页 -->
<head>
  <!-- preconnect：必然要连的 API 与第三方字体域，全握手提前 -->
  <link rel="preconnect" href="https://api.example.com" crossorigin>
  <link rel="preconnect" href="https://fonts.example.com" crossorigin>

  <!-- dns-prefetch：低频第三方域，只省 DNS -->
  <link rel="dns-prefetch" href="https://tracking.example.com">

  <!-- preload：当前页关键路径——LCP 主图与首屏字体 -->
  <link rel="preload" as="image" href="/img/hero.avif" fetchpriority="high">
  <link rel="preload" as="font" type="font/woff2" href="/fonts/brand.woff2" crossorigin>

  <!-- modulepreload：SPA 下一路由的 ESM 入口，连依赖图一起预取 -->
  <link rel="modulepreload" href="/chunks/detail-page.js">

  <!-- prefetch：空闲时预取结算页资源，下一跳更快 -->
  <link rel="prefetch" href="/chunks/checkout.js" as="script">
</head>
```
