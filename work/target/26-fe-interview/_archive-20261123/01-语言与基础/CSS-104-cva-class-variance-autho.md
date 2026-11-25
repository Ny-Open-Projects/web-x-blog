---
title: [CSS-104] cva（class variance authority）思想如何用纯 CSS 实现组件变体系统？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-104：cva（class variance authority）思想如何用纯 CSS 实现组件变体系统？

**答**：
- cva 核心：把组件样式拆成 base + 各维度 variant 声明，由"变体组合"生成最终样式。
- CSS 侧等价实现：base 类 + 属性选择器声明各维度，组合自动生效，无 JS 运行时。
- 复合条件用 `[data-a="x"][data-b="y"]` 组合选择器表达，等价 cva 的 compound variants。
- 复杂默认值继承链用 CSS 变量：子维度缺省时回退到父维度值。
- 适合设计系统 Button/Input/Tag 这类维度清晰的原子组件。

```css
/* base：所有变体共享 */
.btn {
  display: inline-flex; align-items: center; gap: 6px;
  border-radius: var(--radius-md);
  transition: background 0.2s, transform 0.1s;
}

/* variants：维度一（意图）× 维度二（尺寸）正交声明 */
.btn[data-intent="danger"]  { --btn-bg: var(--color-danger); --btn-fg: #fff; }
.btn[data-intent="neutral"] { --btn-bg: var(--bg-sunken);    --btn-fg: var(--fg-primary); }
.btn[data-size="md"]        { --btn-pad: 8px 16px; }

/* compound variant：组合条件的专门规则 */
.btn[data-intent="danger"][data-size="md"] {
  font-weight: 600; /* 危险按钮中尺寸强调 */
}

/* defaultVariants：缺失维度时的回退 */
.btn:not([data-size]) { --btn-pad: 8px 16px; }
.btn:not([data-intent]) { --btn-bg: var(--color-accent); --btn-fg: #fff; }
```
