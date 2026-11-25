---
title: [CSS-012] IFC 是什么？行内元素的排版规则有哪些？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-012：IFC 是什么？行内元素的排版规则有哪些？

**答**：
- IFC（Inline Formatting Context）行内格式化上下文，由一行内多个行内级元素构成行盒（line box）。
- 行内元素水平方向用 margin/padding，垂直方向的 padding 不影响布局高度，margin 上下无效。
- 行盒高度由最高的 inline-level 盒决定，`vertical-align` 控制行内盒子在行盒内的对齐。
- 经典坑：图片下方出现空隙，因为图片默认按 baseline 对齐，底部到行盒底缘有 descent 空隙。

```css
/* 经典坑：img 底部 4px 左右空隙 */
.img-wrap {
  font-size: 0;        /* 解法一：去掉 baseline 空隙来源 */
}
.img-wrap img {
  display: block;      /* 解法二：变成块级 */
}
.img-wrap img.valign {
  vertical-align: top; /* 解法三：改对齐方式 */
}

/* 行内元素 padding 的行为 */
span.demo {
  padding: 10px;       /* 左右撑开布局，上下只是视觉绘制 */
  background: #fc0;
}
```

## 三、定位与层叠上下文
