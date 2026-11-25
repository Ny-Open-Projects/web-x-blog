---
title: [CSS-370] CSS 加载闪烁全景：FOUC/FOIT/CLS 治理
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## CSS-370：CSS 加载闪烁全景：FOUC/FOIT/CLS 治理

**答**：
- 三类闪烁：FOUC（无样式内容闪现——CSS 未就绪先渲染）、FOIT（字体隐形期）、CLS（布局跳动——图片/字体/异步块尺寸未知）——三类常叠加，治理各有一条主线
- FOUC 治理：关键 CSS 内联、非关键 CSS 异步化（media 切换技巧）、SPA 挂载前骨架内联——「首字节即可渲染出正确结构」
- FOIT 治理：font-display: swap + preload + 字体子集（H5-367）；回退字体 metrics 调整（size-adjust）缩小切换跳动
- CLS 治理：图片宽高/aspect-ratio、广告位/异步卡片预留尺寸（min-height）、动态插入放已有内容下方、字体 size-adjust——CLS 目标 <0.1，Cumulative 面板定位每个 shift 来源
- 度量闭环：Performance 面板 Layout Shift 区域可视化 + 线上 web-vitals 按 CLS 元素归因上报（cls entry sources）

```html
<!-- FOUC: 关键样式内联 -->
<style>/* above-the-fold */</style>
<link rel="preload" href="rest.css" as="style" onload="this.rel='stylesheet'">
<!-- 字体 -->
<link rel="preload" href="main.woff2" as="font" crossorigin>
```

```css
/* CLS: 预留异步块 */
.ad-slot { min-height: 250px; }        /* 广告加载前占位 */
img, video { aspect-ratio: attr(width) / attr(height); } /* 或直接写 width/height */
```
