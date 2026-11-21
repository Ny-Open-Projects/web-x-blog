---
title: [CSS-126] color-mix() 与相对颜色语法如何派生颜色？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-126：color-mix() 与相对颜色语法如何派生颜色？

**答**：
- `color-mix(in 色彩空间, A p1%, B p2%)` 按比例混合两色，派生 hover/disabled/border 色不再手调。
- 相对颜色语法：`hsl(from var(--c) h s calc(l - 10%))` 从基准色解构出各分量再重组，做明暗阶梯。
- in oklch 混合比 in srgb 更符合感知（中间色不发灰）。
- 配合 CSS 变量实现"一个主色派生整套语义色"，主题只需改一个变量。
- 两者均已 Baseline，可与 color-mix 嵌套使用。

```css
:root { --brand: #409eff; }

.btn {
  background: var(--brand);
  border-color: color-mix(in oklch, var(--brand) 70%, black); /* 边框：加深 */
}
.btn:hover {
  background: color-mix(in oklch, var(--brand) 85%, white);   /* hover：提亮 */
}
.btn[data-disabled] {
  background: color-mix(in srgb, var(--brand) 40%, transparent);
}

/* 相对颜色语法：从主色解构出明度阶梯 */
:root {
  --brand-dark:  oklch(from var(--brand) calc(l - 0.15) c h);
  --brand-light: oklch(from var(--brand) calc(l + 0.15) c h);
  --brand-bg:    hsl(from var(--brand) h s calc(l * 100% + 40%) / 15%);
}
```
