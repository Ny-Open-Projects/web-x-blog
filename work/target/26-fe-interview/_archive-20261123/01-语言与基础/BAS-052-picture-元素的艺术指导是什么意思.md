---
title: [BAS-052] picture 元素的"艺术指导"是什么意思？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-052：picture 元素的"艺术指导"是什么意思？
**答**：
- 艺术指导指不同场景使用构图不同的图片（如移动端用裁剪后的方图），而非同一张图的不同分辨率。
- picture 里多个 source 按顺序匹配 media/type，命中即用；都不命中回退到 img 的 src。
- 分辨率自适应优先用 srcset/sizes，构图切换才用 picture。

```html
<picture>
  <source media="(max-width: 600px)" srcset="logo-square.jpg" />
  <source type="image/webp" srcset="logo.webp" />
  <img src="logo-wide.jpg" alt="站点 Logo" />
</picture>
```
