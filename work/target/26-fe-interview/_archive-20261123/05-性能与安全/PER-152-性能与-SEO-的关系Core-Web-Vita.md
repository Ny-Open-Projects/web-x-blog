---
title: [PER-152] 性能与 SEO 的关系？Core Web Vitals 如何影响排名？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-152：性能与 SEO 的关系？Core Web Vitals 如何影响排名？

**答**：
- Core Web Vitals（LCP/INP/CLS）是 Google 排名信号之一：它是"页面体验"信号组的一部分，与内容质量、外链等权重并存——**性能差不会让你消失，但内容同质时会输**。
- 数据来源是 CrUX（真实用户 28 天 P75），实验室分数不参与排名；移动端与桌面端分别计算。
- 性能伤 SEO 的典型场景：CSR 爬虫抓不到内容（要 SSR/SSG）、LCP 图片懒加载、CLS 大导致渲染不稳定、被 block 的 JS/CSS 让 Googlebot 渲染失败。
- 工程抓手：关键内容服务端直出、LCP 资源预加载、TTFB 经 CDN 压缩、用 Search Console CWV 报告做回归看板。

```html
<!-- 性能即 SEO：Core Web Vitals 是排名信号，以下是页面必须落实的性能 SEO 清单 -->
<head>
  <meta charset="utf-8">
  <title>商品详情 - 示例商城</title>
  <meta name="description" content="...">

  <!-- LCP：首图预加载 + 高优先级，禁用懒加载 -->
  <link rel="preload" as="image" href="/img/hero.avif" fetchpriority="high">

  <!-- 提前建连，压缩 TTFB 之后的等待 -->
  <link rel="preconnect" href="https://cdn.example.com" crossorigin>

  <!-- CLS：首屏媒体一律声明尺寸 -->
  <style>
    .hero { width: 100%; aspect-ratio: 16 / 9; object-fit: cover; }
  </style>

  <!-- 给爬虫与 CrUX 采样一致的渲染路径：关键内容必须服务端直出，禁止客户端二次替换 DOM -->
</head>
```
