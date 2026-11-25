---
title: [PER-012] 图片优化有哪些手段？如何用 picture 与 srcset 做格式与分辨率适配？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-012：图片优化有哪些手段？如何用 picture 与 srcset 做格式与分辨率适配？

**答**：
- 格式：AVIF > WebP > JPEG/PNG，新格式同画质体积减少 30% 以上，用 `<picture>` 做降级。
- 分辨率：`srcset` + `sizes` 让小屏不拉大图，节省流量。
- 工程手段：构建期压缩（imagemin/sharp）、CDN 图片服务按参数裁剪、`decoding="async"` 异步解码。
- 尺寸必填 `width/height` 或 `aspect-ratio`，防止加载后撑开布局推高 CLS。

```html
<picture>
  <!-- 支持 AVIF/WebP 的浏览器走新格式，体积减少 30% 以上，其余降级 JPEG -->
  <source type="image/avif" srcset="hero.avif">
  <source type="image/webp" srcset="hero.webp">
  <img src="hero.jpg" alt="首页横幅" width="1280" height="640" decoding="async">
</picture>

<!-- 响应式：按视口宽度请求不同分辨率，避免小屏拉大图 -->
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1600.jpg 1600w"
  sizes="(max-width: 600px) 100vw, 50vw"
  alt="照片">
```
