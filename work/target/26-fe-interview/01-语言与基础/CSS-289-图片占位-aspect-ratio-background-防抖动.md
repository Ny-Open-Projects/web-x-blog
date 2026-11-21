---
title: [CSS-289] 图片占位：aspect-ratio + background 防抖动
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## CSS-289：图片占位：aspect-ratio + background 防抖动

**答**：
- 图片未加载时高度为 0 → 加载后撑开 → 整页布局跳动（CLS 劣化）——必须预留占位
- 现代方案：img 上直接 `aspect-ratio: 16/9; width: 100%` + 背景色占位（浏览器知道比例，加载前就占位正确）
- 无比例信息时：服务端返回宽高 → 内联 style aspect-ratio（或 width/height 属性——现代浏览器用 attrs 自动算比例）
- 视觉增强：低质量占位图 LQIP（blurhash/微缩图 blur 拉伸）替代纯色块
- 面试话术：CLS 是 Core Web Vitals 指标，图片占位是最常见的 CLS 修复项

```html
<!-- width/height 属性让浏览器提前算比例 -->
<img src="a.jpg" width="1280" height="720" style="width:100%;height:auto;background:#eee">
```
```css
/* 或 CSS 声明 */
.cover { aspect-ratio: 16 / 9; width: 100%; background: #eee; }
```
