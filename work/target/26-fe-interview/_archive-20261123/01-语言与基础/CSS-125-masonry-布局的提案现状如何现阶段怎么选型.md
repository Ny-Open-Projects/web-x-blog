---
title: [CSS-125] masonry 布局的提案现状如何？现阶段怎么选型？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-125：masonry 布局的提案现状如何？现阶段怎么选型？

**答**：
- 现状：`grid-template-rows: masonry` 仍处提案阶段，Chrome 以 flag 形式实验，未进 Baseline。
- 争议点：条目排列顺序（优先列序还是读序）与 WebKit 的 item-flow 整合方案尚未定论，API 可能变化。
- 可用替代一：CSS `columns`（纯 CSS 但纵向读序）；替代二：Grid 双列/多列手动分配；替代三：JS 最短列算法（读序正确）。
- 选型建议：内容顺序重要的信息流用 JS 或 grid；读序不敏感的图片墙用 columns；提案落地前不写依赖 masonry 关键布局的代码。

```css
/* 现阶段可用：columns 方案（读序纵向） */
.gallery {
  columns: 4 220px;
  column-gap: 16px;
}
.gallery img {
  width: 100%;
  margin-bottom: 16px;
  break-inside: avoid;
  display: block;
}

/* 未来可期（实验 flag 下） */
@supports (grid-template-rows: masonry) {
  .gallery-future {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: masonry;
    gap: 16px;
  }
}
```
