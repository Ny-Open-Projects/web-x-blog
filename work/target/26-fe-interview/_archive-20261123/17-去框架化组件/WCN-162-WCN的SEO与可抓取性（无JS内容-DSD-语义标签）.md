---
title: [WCN-162] WCN 的 SEO 与可抓取性：爬虫对 Shadow DOM 的支持现状与对策？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-162：WCN 的 SEO 与可抓取性：爬虫对 Shadow DOM 的支持现状与对策？

**答**：
- 现状：Googlebot 已渲染 JS 且支持 Shadow DOM（含 DSD），但其他引擎与社交抓取器（部分）仍可能读不到影子树内容——关键内容（标题/价格/正文）不要只存在于影子树。
- 对策一：DSD 优先——服务端输出 `<template shadowrootmode>` 让内容直接在 HTML 源码里（源码级可抓取，最稳）。
- 对策二：light DOM 冗余——把 SEO 关键文本放在 light DOM（slot 投影展示），影子树只承载装饰结构；`<slot>` 内容本身就是源码可见的。
- 对策三：语义标签与元数据外置——页面级 title/meta/schema.org 结构化数据照常写主文档，组件不承载元信息。
- 验证方式：用 Google Search Console 的"URL 检查"渲染快照、或抓取模拟器（无 JS/有 JS 两次对比）确认内容可达。

```html
<!-- SEO 安全的组件用法：关键文本在 light DOM -->
<product-card sku="A1">
  <h2 slot="title">无线降噪耳机</h2>          <!-- 源码可见，爬虫可读 -->
  <p slot="summary">主动降噪 · 40 小时续航</p>
  <template shadowrootmode="open">
    <style>.price{color:#16a34a}</style>
    <slot name="title"></slot><slot name="summary"></slot>
    <span class="price">¥299</span>           <!-- 装饰性内容在影子树 -->
  </template>
</product-card>
```
