---
title: [PER-219] 图片为什么是 CLS 头号来源？aspect-ratio 与 width/height 属性的正确用法？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-219：图片为什么是 CLS 头号来源？aspect-ratio 与 width/height 属性的正确用法？

**答**：
- 机理：浏览器在图片头解析出尺寸前不知道占位大小，只能按 0 高度排布，图片加载完再撑开，下方内容全部下移——这就是最大的布局位移来源。轮播图、封面图、头像列表都高发。
- 正确姿势一：HTML 里写 `width`/`height` 属性（与图片真实比例一致），浏览器据此算出内在比例并预留空间，配合 `height: auto` 响应式缩放不位移。
- 正确姿势二：CSS `aspect-ratio: 16 / 9` 显式声明比例，适合比例固定但实际渲染尺寸由容器决定的场景；背景图占位可用 `padding-top` 百分比技巧（老方案）或 `aspect-ratio`。
- 进阶：占位图/主色块（LQIP）在图片到达前填充同样比例的模糊色块；轮播图整体容器定高，内部切换用 transform，杜绝轮播切换时页面高度抖动。

```html
<!-- 写法一：属性声明比例，浏览器加载前即可预留 -->
<img src="hero.avif" width="1280" height="720" alt="首屏"
     style="width:100%;height:auto;object-fit:cover">

<!-- 写法二：比例固定、尺寸随容器 -->
<div class="cover"><img src="p.avif" alt="" style="width:100%;height:100%;object-fit:cover"></div>
<style>
.cover { aspect-ratio: 16 / 9; width: 100%; }  /* 加载前就有高度，零位移 */
</style>
```
