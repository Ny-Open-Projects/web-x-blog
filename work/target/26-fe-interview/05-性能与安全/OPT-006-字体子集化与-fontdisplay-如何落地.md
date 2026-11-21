---
title: [OPT-006] 字体子集化与 font-display 如何落地？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-006：字体子集化与 font-display 如何落地？

**答**：
- 中文字体动辄 5~10MB，必须子集化：`pyftsubset`（fonttools）按实际用到的字符裁剪，或用中文分片方案（按 unicode-range 切成几十个小包，用到哪片下哪片）。
- `font-display: swap` 让浏览器先用回退字体渲染，字体到位后切换，避免 3 秒白屏（FOIT），代价是短暂 FOUT 闪烁。
- 首屏关键字体加 `preload` 提前加载，配合 `font-family` 回退链调整行高避免布局抖动。
- 数字/Logo 类小字符集字体可内联为 base64 或 WOFF2 直接打包。

```css
/* 一一对应：子集化后的字体声明 + font-display: swap */
@font-face {
  font-family: 'PingFangSubset';
  /* pyftsubset 产物，只含页面实际用到的几百个字符 */
  src: url('./fonts/main-subset.woff2') format('woff2');
  font-display: swap;      /* 先用回退字体显示，加载完再切换 */
  unicode-range: U+4E00-9FFF; /* 只对中文区间生效，其余字符走回退 */
}

/* 预加载关键字体，与 CSS 中的 URL 保持一致 */
```

```html
<!-- 一一对应：关键字体的 preload -->
<link rel="preload" href="/fonts/main-subset.woff2" as="font" type="font/woff2" crossorigin />
```

## 二、加载策略与关键渲染路径
