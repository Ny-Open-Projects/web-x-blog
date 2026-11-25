---
title: [H5-336] rem/vw 适配方案演进与落地陷阱
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 适配]
type: 面试题
---

## H5-336：rem/vw 适配方案演进与落地陷阱

**答**：
- 演进路线：固定宽度 320/375 → rem（JS 设 html font-size，postcss-pxtorem）→ vw/vh（纯 CSS，postcss-px-to-viewport）→ vw + max/min clamp 限制极端
- vw 方案优势：纯 CSS 无 JS 依赖、无闪烁（rem 方案 JS 设置前会闪）；劣势：大屏/折叠屏等比放大会失真
- 混合方案（当前主流）：布局尺寸 vw、文本用 clamp(min, vw, max) 限幅、边框 1px 独立处理；设计稿 750 宽换算 1vw = 7.5px
- 经典陷阱：1px 边框在 DPR>1 的模糊——用 border 0.5px（部分支持）或 ::after transform scale(.5) 或 box-shadow 方案；小数像素取整问题
- 与安全区/横屏组合：vw 单位在横屏时 vh/vw 语义随方向变化，需要 CSS 逻辑属性与 @media orientation 双套

```css
/* 750 设计稿: 1vw = 7.5px */
.card { width: 92vw; padding: 4vw; }
.title {
  /* 字号限幅: 最小 14px 最大 20px */
  font-size: clamp(14px, 2.66vw, 20px);
}
.hairline {
  position: relative;
}
.hairline::after {
  content: ''; position: absolute; left: 0; top: 0; width: 100%; height: 1px;
  background: #eee; transform: scaleY(.5); transform-origin: 0 0;
}
```
