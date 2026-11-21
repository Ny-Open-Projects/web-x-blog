---
title: [BAS-071] object-fit 的几个值分别是什么效果？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-071：object-fit 的几个值分别是什么效果？
**答**：
- 控制替换元素（img/video）内容如何填入元素框：cover 等比放大裁剪填满（最常用）；contain 等比缩放完整显示、留空白。
- fill 是默认值，不保比例直接拉伸变形；none 不缩放按原始尺寸；scale-down 取 none 和 contain 中显示更小的那个。
- 配合 object-position 调整裁剪焦点，如 `object-position: center top` 保住人像头部。

```css
.cover { object-fit: cover; object-position: center top; }  /* 裁剪填充，焦点在顶部 */
.contain-box { object-fit: contain; background: #eee; }     /* 完整显示，留白 */
.stretch { object-fit: fill; }                              /* 拉伸变形，慎用 */
```
