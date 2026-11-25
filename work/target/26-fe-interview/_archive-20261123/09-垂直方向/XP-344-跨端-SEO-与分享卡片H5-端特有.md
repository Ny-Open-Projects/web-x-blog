---
title: [XP-344] 跨端 SEO 与分享卡片（H5 端特有）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-344：跨端 SEO 与分享卡片（H5 端特有）

**答**：
- SEO：SSR/预渲染（H5 端），meta 标签规范；App/小程序端不适用。
- 分享：og: 标签（微信/FB 抓取）、分享卡片图规范（5:4 比例）。
- 性能：分享落地页首屏直出（SSR），爬虫 UA 优化响应。

```javascript
// 分享元信息
function shareMeta({ title, desc, img, url }) {
  return `<meta property="og:title" content="${esc(title)}">
<meta property="og:description" content="${esc(desc)}">
<meta property="og:image" content="${img}">
<meta property="og:url" content="${url}">`;
}
function esc(s) { return s.replace(/&/g, '&amp;').replace(/"/g, '&quot;'); }
```
