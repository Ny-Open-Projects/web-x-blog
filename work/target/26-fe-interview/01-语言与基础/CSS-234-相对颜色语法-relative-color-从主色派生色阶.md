---
title: [CSS-234] 相对颜色语法：从主色派生色阶
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 设计系统]
type: 面试题
---

## CSS-234：相对颜色语法（relative color）：从主色派生色阶

**答**：
- 语法：`oklch(from var(--brand) calc(l * 0.8) c h)`——取出原色的 l/c/h 通道，逐通道计算后重组
- 与 color-mix 的区别：相对颜色是「通道级手术」（只动亮度/色度/色相），mix 是「颜色间混合」
- 派生色阶正解：同 hue 与 chroma，L 按比例缩放——比手工调十档颜色稳定得多
- 典型用途：hover 深化、disabled 降饱和、色相偏移（品牌色 → 邻近色）
- 兼容：Chrome 119+/Safari 16.4+/Firefox 128+；与 oklch 组合是设计系统程序化配色的现代答案

```css
:root { --brand: oklch(62% 0.19 260); }
.btn:hover   { background: oklch(from var(--brand) calc(l * 0.85) c h); }  /* 更深 */
.btn:disabled{ background: oklch(from var(--brand) l calc(c * 0.4) h); }   /* 降饱和 */
.tag-cyan    { background: oklch(from var(--brand) l c calc(h + 120)); }   /* 色相偏移 */
```
