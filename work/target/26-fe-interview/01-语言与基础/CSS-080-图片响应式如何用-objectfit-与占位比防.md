---
title: [CSS-080] 图片响应式如何用 object-fit 与占位比防抖动？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-080：图片响应式如何用 object-fit 与占位比防抖动？

**答**：
- `object-fit: cover` 裁剪填满并保持比例，`contain` 完整显示留白，是替代 background-image 的语义化方案。
- 提前用 `aspect-ratio` 锁定占位高度，图片加载前后布局零跳动（消除 CLS）。
- `object-position` 控制裁剪焦点，如人像偏上 `50% 20%`。
- 多分辨率供给配合 `<img srcset sizes>`，让浏览器自选最合适资源。
- 懒加载图片给 `loading="lazy"` + `decoding="async"`。

```html
<img
  class="cover-img"
  src="photo-800w.avif"
  srcset="photo-400w.avif 400w, photo-800w.avif 800w, photo-1600w.avif 1600w"
  sizes="(min-width: 75em) 33vw, 100vw"
  width="800" height="450"
  loading="lazy" decoding="async"
  alt="封面图"
>
```

```css
.cover-img {
  width: 100%;
  aspect-ratio: 16 / 9;   /* 与 width/height 属性一致，占位防 CLS */
  object-fit: cover;      /* 比例不符时裁剪填充 */
  object-position: 50% 20%;
  background: var(--bg-sunken);  /* 加载前占位底色 */
}
```
