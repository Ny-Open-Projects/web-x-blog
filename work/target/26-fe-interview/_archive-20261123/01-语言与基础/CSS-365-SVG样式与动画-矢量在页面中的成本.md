---
title: [CSS-365] SVG 样式与动画：矢量图形在页面中的成本
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-365：SVG 样式与动画：矢量图形在页面中的成本

**答**：
- 两种形态成本差异：inline SVG（可 CSS 交互、每实例独立解析）vs <use>/svg sprite（复用解析）、img 引用 svg（不可 CSS 定制内部）——图标系统用 sprite + CSS 变量着色
- SVG 样式能力：fill/stroke 可继承 CSS（currentColor 联动文本色）、几何属性（cx/r）可 CSS 化（geometry properties）、SVG 内部可写 style 块
- 动画路径：SMIL（废弃倾向）→ CSS 动画（transform/opacity 可合成）→ WAAPI/JS 驱动 stroke-dashoffset（描边动画，paint 重绘，小图标可接受）——复杂矢量动画上 Lottie（canvas/SVG 渲染器）
- 性能点：path 复杂度（节点数）决定栅格化成本，设计师导出的图标要过 SVGO 清理（减节点/合并 path）；大面积 SVG 缩放动画触发重栅格，位图代替
- 无障碍：inline SVG 要 role="img" + aria-label/title；装饰性图标 aria-hidden

```html
<svg style="display:none"><symbol id="i-star" viewBox="0 0 24 24">
  <path fill="currentColor" d="..."/>
</symbol></svg>
<svg class="icon" role="img" aria-label="收藏"><use href="#i-star"/></svg>
```

```css
.icon { width: 20px; height: 20px; color: var(--fg); }
.icon--active { color: var(--primary); }   /* currentColor 联动 */
/* 描边动画 */
.draw { stroke-dasharray: 100; stroke-dashoffset: 100; animation: draw 1s forwards; }
@keyframes draw { to { stroke-dashoffset: 0; } }
```
