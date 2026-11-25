---
title: [CSS-001] 标准盒模型和 IE 盒模型有什么区别？如何切换？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-001：标准盒模型和 IE 盒模型有什么区别？如何切换？

**答**：
- 标准盒模型（content-box）：`width` 只包含内容区，总宽度 = width + padding + border。
- IE 盒模型（border-box）：`width` 已包含 padding 和 border，实际内容区被压缩。
- 通过 `box-sizing: border-box` 切换，切到 border-box 后布局计算更直观。
- 现代工程默认全局使用 border-box，避免加 padding 导致元素变宽。

```css
.box-standard {
  box-sizing: content-box; /* 默认值，width 只算内容 */
  width: 200px;
  padding: 20px;
  border: 5px solid #333;
  /* 实际占用宽度 = 200 + 20*2 + 5*2 = 250px */
}

.box-ie {
  box-sizing: border-box; /* width 含 padding 与 border */
  width: 250px;
  padding: 20px;
  border: 5px solid #333;
  /* 实际占用宽度 = 250px，内容区被压缩为 200px */
}
```
