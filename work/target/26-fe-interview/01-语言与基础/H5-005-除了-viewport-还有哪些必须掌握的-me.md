---
title: [H5-005] 除了 viewport，还有哪些必须掌握的 meta 标签？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-005：除了 viewport，还有哪些必须掌握的 meta 标签？
**答**：
- `<meta charset="UTF-8">`：字符编码，必须尽早声明（前 1024 字节内），防乱码。
- `<meta name="description">`：搜索结果摘要，直接影响点击率；keywords 已被主流搜索引擎忽略。
- Open Graph（`og:title` 等）：社交平台分享卡片的内容来源。
- `http-equiv`：如 `X-UA-Compatible`（已过时）、`refresh` 自动跳转（不推荐）。

```html
<head>
  <meta charset="UTF-8" />

  <!-- SEO 基础 -->
  <title>前端面试题库 - 网络 HTML 精讲</title>
  <meta name="description" content="覆盖 HTTP 缓存渲染等高频前端面试考点，每题附可运行代码。" />

  <!-- Open Graph：微信/推特等分享卡片 -->
  <meta property="og:title" content="前端面试题库" />
  <meta property="og:description" content="网络与 HTML5 高频考点" />
  <meta property="og:image" content="https://example.com/cover.png" />

  <!-- 移动端_web app 相关 -->
  <meta name="theme-color" content="#3367d6" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
</head>
```
