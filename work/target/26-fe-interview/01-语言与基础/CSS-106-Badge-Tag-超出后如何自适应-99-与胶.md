---
title: [CSS-106] Badge/Tag 超出后如何自适应（99+ 与胶囊收缩）？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-106：Badge/Tag 超出后如何自适应（99+ 与胶囊收缩）？

**答**：
- 数字徽标"99+"由 JS 计算文本、CSS 只负责展示，纯 CSS 无法比较数值大小。
- 胶囊自适应：`min-width: 20px` 圆点态，内容出现后 `padding-inline: 6px` 自动撑开，border-radius: 999px 两态通吃。
- 绝对定位徽标注意父容器 `overflow` 裁剪，必要时挂在不被裁剪的锚点上。
- 多字符 Tag 超宽用 max-width + 单行截断兜底。

```css
/* 1. 胶囊徽标：圆点 → 数字 自适应 */
.badge {
  position: absolute;
  inset-block-start: -4px;
  inset-inline-end: -4px;
  min-width: 18px; height: 18px;
  padding-inline: 5px;          /* 内容撑开成胶囊 */
  border-radius: 999px;
  display: inline-flex; align-items: center; justify-content: center;
  font-size: 11px;
  background: var(--color-danger); color: #fff;
}
.badge:empty { padding-inline: 0; }  /* 无文本时收缩为圆点 */

/* 2. 长文本 Tag 兜底 */
.tag {
  max-width: 160px;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
```

```javascript
// 数值封顶由 JS 决定，CSS 展示
const label = count > 99 ? '99+' : String(count);
badgeEl.textContent = count > 0 ? label : '';
```
