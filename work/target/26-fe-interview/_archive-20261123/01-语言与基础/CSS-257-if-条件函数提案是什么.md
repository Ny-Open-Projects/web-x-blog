---
title: [CSS-257] if() 条件函数提案是什么
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## CSS-257：if() 条件函数提案是什么

**答**：
- if()：在 CSS 值内做条件分支——`if(media(...): a; supports(...): b; else: c)`，把「条件换值」从规则级下沉到「值级」
- 与 media query 的区别：@media 换「整条声明」，if() 换「一个值」——同一属性内按条件取不同值，声明更少
- 条件类型：media()、supports()、style()（变量值判断）三种，可组合 else 链
- 典型场景：间距在不同容器下取值、主题相关圆角、平台差异值——以前要重复整条声明
- 现状：Chromium 137+ 实验性；落地前用 CSS 变量 + @media 覆盖的写法仍是主流

```css
.gap {
  /* 概念示例（实验性） */
  padding: if(media(min-width: 768px): 24px; style(--dense: 1): 4px; else: 16px);
}
/* 现行等价写法 */
.gap { padding: 16px; }
@media (min-width: 768px) { .gap { padding: 24px; } }
.dense .gap { padding: 4px; }
```
