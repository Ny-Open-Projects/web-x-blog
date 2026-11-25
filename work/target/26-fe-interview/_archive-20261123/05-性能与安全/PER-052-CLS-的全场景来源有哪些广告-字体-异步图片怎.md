---
title: [PER-052] CLS 的全场景来源有哪些？广告、字体、异步图片怎么防抖动？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-052：CLS 的全场景来源有哪些？广告、字体、异步图片怎么防抖动？

**答**：
- 常见偏移源：无宽高的异步图片/视频、后插入的广告位、字体替换导致的文字回流、顶部动态 banner、懒加载弹层挤开内容。
- 防抖三板斧：**预留空间**（CSS `aspect-ratio` 或固定 min-height）、**占位替换**（广告位先渲染骨架，字体用 `size-adjust` 匹配 fallback）、**位移改覆盖**（浮层用 `position: fixed` 脱离文档流）。
- 字体替换只在**换行点变化**时产生偏移，把 fallback 字体调到与 webfont 的宽度、行高、字距接近即可把 CLS 压到 0。
- `aspect-ratio` 需要知道宽高比；比例未知的场景用 `min-height` + 渐进填充。

```html
<style>
  /* 异步图片：用 aspect-ratio 预留空间，CLS 贡献为 0 */
  .cover { aspect-ratio: 16 / 9; width: 100%; background: #eee; }
  .cover img { width: 100%; height: 100%; object-fit: cover; }

  /* 广告位：固定最小高度占位，加载后不会推挤下方内容 */
  .ad-slot { min-height: 250px; background: repeating-linear-gradient(45deg, #fafafa, #fafafa 8px, #f0f0f0 8px, #f0f0f0 16px); }

  /* 字体回退匹配：size-adjust + ascent-override 让 Arial 近似模拟品牌字体 */
  @font-face {
    font-family: 'BrandFallback';
    src: local('Arial');
    size-adjust: 105%;
    ascent-override: 90%;
    descent-override: 22%;
    line-gap-override: 0%;
  }
  @font-face {
    font-family: 'Brand';
    src: url('/fonts/brand.woff2') format('woff2');
    font-display: swap; /* 先用 fallback 渲染，webfont 到达后替换 */
  }
  body { font-family: 'Brand', 'BrandFallback', sans-serif; }
</style>
<div class="cover"><img src="/img/cover.avif" alt=""></div>
<div class="ad-slot" data-ad="sidebar"></div>
```
