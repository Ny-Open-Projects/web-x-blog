---
title: [PER-086] 字体加载的完整策略是什么？font-display/子集化/size-adjust 如何组合？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-086：字体加载的完整策略是什么？font-display/子集化/size-adjust 如何组合？

**答**：
- 组合拳：**woff2 + unicode-range 子集化**（中文字体按字符区间拆几十个包，用到哪个下哪个）、**font-display: swap**（先用 fallback 渲染不阻塞文本）、**size-adjust 匹配 fallback**（替换时宽度对齐，消除 CLS）、**preload 首屏字体**。
- font-display 取值：`auto`（浏览器决定）、`block`（最多等 3s 隐形文本）、`swap`（立即用 fallback，字体到了替换）、`fallback`（约 100ms 后用 fallback，2s 内字体到才替换）、`optional`（约 100ms 决定，超时本次会话用 fallback，最稳）。
- 中文场景特殊：全量字体动辄数 MB，子集化（按页面实际字符集或 GB2312 分片）是必选项；`text=` 参数适合图标字体场景。
- 监控：字体加载失败要降级到系统字体栈，不能让正文不可读。

```css
/* 字体全策略：子集化 + swap + fallback 对齐 */
/* 中文主字体按 unicode-range 分片（构建工具生成多个分片，这里示意两个） */
@font-face {
  font-family: 'BrandSC';
  src: url('/fonts/brand-sc-0.woff2') format('woff2');
  font-display: swap;             // 先渲染 fallback，不阻塞文本
  unicode-range: U+4E00-4FFF;     // CJK 第一区间，用到才下载
}
@font-face {
  font-family: 'BrandSC';
  src: url('/fonts/brand-sc-1.woff2') format('woff2');
  font-display: swap;
  unicode-range: U+5000-5FFF;
}
/* fallback 字体：size-adjust 把 Arial 调到与 BrandSC 度量一致，替换零偏移 */
@font-face {
  font-family: 'BrandSC-Fallback';
  src: local('PingFang SC'), local('Microsoft YaHei'), local('Arial');
  size-adjust: 102%;
  ascent-override: 88%;
  descent-override: 20%;
  line-gap-override: 0%;
}
body {
  font-family: 'BrandSC', 'BrandSC-Fallback', sans-serif;
  font-synthesis: none; /* 防止伪粗体伪斜体引发布局漂移 */
}
```

```html
<!-- 首屏关键字体 preload：提前开始下载 woff2 -->
<link rel="preload" href="/fonts/brand-sc-0.woff2" as="font" type="font/woff2" crossorigin>
```
