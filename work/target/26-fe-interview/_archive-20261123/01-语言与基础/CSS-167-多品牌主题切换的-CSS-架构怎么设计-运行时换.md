---
title: [CSS-167] 多品牌主题切换的 CSS 架构怎么设计（运行时换肤）？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-167：多品牌主题切换的 CSS 架构怎么设计（运行时换肤）？

**答**：
- 分层：token 层（变量定义）→ 组件层（只读变量）→ 换肤层（data 属性覆盖 token）。组件永不写死颜色。
- 每个品牌用 `:root[data-brand=x]` 覆盖一组 token，组件层零改动。
- 派生色（hover、浅底、透明度）用 `color-mix()` 从主色计算，品牌切换时自动跟随，避免每品牌重复定义全套色板。
- 运行时换肤只需一行 JS 改 data 属性；预构建所有品牌 CSS 还是运行时算派生色，按品牌数量权衡。

```css
/* 1. token 层：默认品牌 */
:root {
  --brand: #096;
  /* 派生色由 color-mix 计算，品牌切换自动跟随 */
  --brand-weak: color-mix(in srgb, var(--brand) 12%, white);
  --brand-hover: color-mix(in srgb, var(--brand) 85%, black);
}

/* 2. 换肤层：其余品牌只覆盖主色这一个源头 */
:root[data-brand="b"] { --brand: #f60; }
:root[data-brand="c"] { --brand: #7c3aed; }

/* 3. 组件层：只读变量，永不出现具体色值 */
.btn-primary {
  background: var(--brand);
  color: #fff;
  border-radius: var(--radius, 6px);
}
.btn-primary:hover { background: var(--brand-hover); }
.card-tag { background: var(--brand-weak); color: var(--brand); }

/* 4. 运行时换肤一行 JS：
   document.documentElement.dataset.brand = 'b'; */
```
