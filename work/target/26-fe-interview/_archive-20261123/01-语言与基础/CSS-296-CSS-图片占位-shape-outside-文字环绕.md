---
title: [CSS-296] shape-outside：文字环绕不规则图形
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 排版]
type: 面试题
---

## CSS-296：shape-outside：文字环绕不规则图形

**答**：
- shape-outside：让浮动元素周围的文字沿「形状」而非「矩形盒」环绕——圆形头像、多边形、图片 alpha 轮廓
- 取值：circle()/ellipse()/polygon()/path() 或 url(图片)（用图片透明度作为轮廓，需同源/CORS）
- 配套：shape-margin（文字与形状的间距）、shape-image-threshold（alpha 轮廓阈值）
- 局限：只作用于 float 元素——不能用于 flex/grid 布局内；现代排版（杂志式环绕）用得多
- 兼容：Chrome/Safari 支持，Firefox 支持——可用，但场景窄

```css
.avatar {
  float: left;
  width: 120px; height: 120px;
  border-radius: 50%;
  shape-outside: circle(50%);
  shape-margin: 12px;
}
.stamp {
  float: left;
  shape-outside: url('/stamp.png');  /* 按图片轮廓环绕 */
  shape-image-threshold: 0.5;
}
```
