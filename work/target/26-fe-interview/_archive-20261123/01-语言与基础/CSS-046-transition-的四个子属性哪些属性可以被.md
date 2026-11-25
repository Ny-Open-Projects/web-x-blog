---
title: [CSS-046] transition 的四个子属性？哪些属性可以被过渡？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-046：transition 的四个子属性？哪些属性可以被过渡？

**答**：
- 四子属性：`transition-property`、`duration`、`timing-function`、`delay`，简写时 duration 在 delay 前。
- 可过渡的是“有中间值”的属性：长度、颜色、透明度、transform 等；display、visibility 是离散属性，默认无过渡（visibility 在过渡期结束时才切换；display 需配合 `transition-behavior: allow-discrete` 才可参与过渡）。
- 可用 `transition: all` 但性能差且易误伤，推荐显式列出属性。
- 高度 auto 无法过渡，需要用 grid-template-rows: 0fr/1fr 或 JS 计算等技巧。

```css
.btn {
  background: #409eff;
  color: #fff;
  /* property duration timing-function delay */
  transition: background 0.25s ease-out 0s,
              transform 0.25s ease;
}
.btn:hover {
  background: #337ecc;
  transform: translateY(-2px);
}

/* 高度 auto 过渡的 grid 技巧 */
.collapse {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 0.3s;
}
.collapse.open { grid-template-rows: 1fr; }
.collapse > .inner { overflow: hidden; min-height: 0; }
```
