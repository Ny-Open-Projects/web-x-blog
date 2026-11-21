---
title: [H5-043] srcset 和 picture 分别解决什么问题？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-043：srcset 和 picture 分别解决什么问题？
**答**：
- `srcset` + `sizes`：同一张图的多分辨率选择，浏览器按"视口宽 × DPR"选最合适文件，解决高清屏与小屏的流量浪费。
- `picture`：按条件切换不同资源（不同格式 WebP/AVIF、不同裁切的 art direction），source 支持 media 与 type。
- 都写上时 picture 的 source 匹配优先于 img 的 srcset。
- 兜底原则：img 的 src 必填（老浏览器），加 width/height 防 CLS。

```html
<!-- 场景一：同图多分辨率，srcset + sizes -->
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1600.jpg 1600w"
  sizes="(max-width: 600px) 100vw, 50vw"
  width="800" height="600"
  alt="风景"
/>
<!-- sizes：600px 以下视口占满屏宽，否则占一半；浏览器结合 DPR 自动挑 srcset -->

<!-- 场景二：新格式渐进增强 -->
<picture>
  <source srcset="hero.avif" type="image/avif" />
  <source srcset="hero.webp" type="image/webp" />
  <img src="hero.jpg" width="1200" height="400" alt="首屏大图" />
</picture>

<!-- 场景三：art direction，移动端裁成方的 -->
<picture>
  <source media="(max-width: 600px)" srcset="hero-square.jpg" width="600" height="600" />
  <img src="hero-wide.jpg" width="1200" height="400" alt="横幅" />
</picture>
```
