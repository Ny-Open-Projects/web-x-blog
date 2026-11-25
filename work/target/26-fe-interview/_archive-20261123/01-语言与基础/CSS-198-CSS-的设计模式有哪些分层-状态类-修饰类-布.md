---
title: [CSS-198] CSS 的设计模式有哪些分层（状态类/修饰类/布局类）？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-198：CSS 的设计模式有哪些分层（状态类/修饰类/布局类）？

**答**：
- 布局类：只管排布（display/gap/定位），不含颜色字体——可套用在任意业务组件上。
- 外观类：默认视觉（背景、圆角、阴影），修饰类改外观变体（--bordered/--ghost），状态类表达瞬时状态（is-/has- 前缀）。
- 层级约定：布局 < 外观 < 修饰 < 状态，同级内靠书写顺序，跨级靠层（@layer），不靠 important。
- is-/has- 前缀的价值：一眼区分“数据驱动状态”与“设计变体”，JS 只操作状态类，不碰修饰类。

```css
/* 布局类：与视觉完全解耦 */
.layout-split { display: flex; gap: var(--gap); }
.layout-stack { display: flex; flex-direction: column; gap: var(--gap-sm); }

/* 外观类：组件默认视觉 */
.card {
  background: var(--bg-surface);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
}

/* 修饰类：设计变体，用 -- 双横线 */
.card--bordered { border: 1px solid var(--line); }
.card--ghost    { background: transparent; box-shadow: none; }

/* 状态类：JS/数据驱动，用 is- has- 前缀 */
.card.is-active  { box-shadow: 0 0 0 2px var(--brand); }
.card.has-error  { border-color: var(--danger); }
.card.is-loading { pointer-events: none; opacity: .6; }

/* 层级：布局 < 外观 < 修饰 < 状态，状态类总是最后书写 */
```
