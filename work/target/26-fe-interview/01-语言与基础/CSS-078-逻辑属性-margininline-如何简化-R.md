---
title: [CSS-078] 逻辑属性 margin-inline 如何简化 RTL 适配？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-078：逻辑属性 margin-inline 如何简化 RTL 适配？

**答**：
- `margin-inline` / `padding-block` / `inset-inline-start` 等逻辑属性按"起止方向"而非物理左右定义。
- 页面切 `dir="rtl"` 时逻辑属性自动镜像，一套样式同时服务 LTR/RTL，不用维护两份。
- 文本对齐用 `text-align: start/end`，定位用 `inset-inline-start`，边框用 `border-inline-start`。
- 混用物理属性（left/right）与逻辑属性时注意层叠覆盖关系，团队内约定统一用逻辑属性。
- 现代浏览器全面支持，Arabic/Hebrew 国际化项目的标配。

```css
/* 一套样式，LTR 与 RTL 自动镜像 */
.card {
  margin-inline: auto;                 /* 物理上等于左右 auto */
  padding-inline: 16px;
  border-inline-start: 3px solid var(--brand);
  text-align: start;                   /* LTR 时左对齐，RTL 时右对齐 */
}

.badge {
  position: absolute;
  inset-inline-start: 8px;             /* LTR 的 left / RTL 的 right */
  inset-block-start: 8px;
}

/* RTL 只需关心内容本身差异 */
[dir="rtl"] .arrow-icon { transform: scaleX(-1); }
```
