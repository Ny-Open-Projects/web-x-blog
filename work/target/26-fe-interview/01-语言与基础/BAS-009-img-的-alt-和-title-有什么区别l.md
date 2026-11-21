---
title: [BAS-009] img 的 alt 和 title 有什么区别？loading="lazy" 是什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-009：img 的 alt 和 title 有什么区别？loading="lazy" 是什么？
**答**：
- alt：图片加载失败或读屏场景下的替代文本，是可访问性与 SEO 的必需属性。
- title：鼠标悬停时的提示文案，纯增强性质。
- `loading="lazy"`：原生懒加载，接近视口时才发起请求；首屏大图不要加，否则拖慢 LCP。

```html
<img
  src="chart.png"
  alt="2026 年各季度营收柱状图"
  title="点击查看大图"
  loading="lazy"
  decoding="async" />
```
