---
title: [CSS-004] 父子元素 margin 塌陷的原因与解决方案？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-004：父子元素 margin 塌陷的原因与解决方案？

**答**：
- 父元素没有 border、padding 或行内内容分隔时，第一个子元素的 `margin-top` 会“穿透”到父元素外，表现为父元素被一起推下去。
- 本质是父元素与子元素的上边界相邻，属于外边距合并的一种。
- 解决：给父元素建立 BFC、加 `padding-top` 或 `border-top` 分隔、改用 padding 撑间距。
- 推荐习惯：间距一律用父元素 padding 或 gap，而不是第一个子元素的 margin。

```css
/* 问题代码 */
.parent {
  background: #eee;
}
.parent > .child {
  margin-top: 50px; /* 穿透出去，父元素整体下移 50px */
}

/* 方案一：父元素建立 BFC */
.parent { overflow: hidden; }

/* 方案二：padding 分隔 */
.parent { padding-top: 1px; }

/* 方案三：伪元素分隔（不产生多余 DOM） */
.parent::before {
  content: "";
  display: table;
}
```
