---
title: [BAS-008] jpg、png、gif、webp、svg 分别适合什么图片？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-008：jpg、png、gif、webp、svg 分别适合什么图片？
**答**：
- jpg：有损压缩、不支持透明，适合照片、banner 等色彩丰富的大图。
- png：无损 + 透明通道，适合图标、截图、需要透明的素材。
- gif：仅 256 色，适合简单帧动画，现在多被 webp/apng 或视频替代。
- webp/avif：有损无损都支持，比 jpg 小 25%~50%，现代浏览器优先使用。
- svg：矢量格式，无限缩放不失真，可用 CSS 改色，适合图标与插画。

```html
<picture>
  <source srcset="hero.avif" type="image/avif" />
  <source srcset="hero.webp" type="image/webp" />
  <img src="hero.jpg" alt="首屏大图" />
  <!-- 浏览器从上到下选第一个支持的格式，jpg 兜底 -->
</picture>
```
