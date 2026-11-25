---
title: [CSS-014] absolute 元素的包含块是怎么确定的？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-014：absolute 元素的包含块是怎么确定的？

**答**：
- 默认规则：最近的 `position` 非 static 的祖先元素的 padding box。
- 若祖先是 `transform`、`perspective`、`filter`、`will-change` 等，则该祖先成为包含块，即使它是 static。
- `position: fixed` 的包含块通常是视口，但存在上述属性祖先时改为那个祖先。
- 理解包含块才能解释“transform 导致 fixed 失效”这类高频问题。

```css
/* HTML: <div class="outer"><div class="inner">fixed?</div></div> */
.outer {
  transform: translateZ(0); /* 创建了包含块 */
}
.inner {
  position: fixed;
  top: 0;
  left: 0;
  /* 实际相对 .outer 定位，而不是视口 */
}
```
