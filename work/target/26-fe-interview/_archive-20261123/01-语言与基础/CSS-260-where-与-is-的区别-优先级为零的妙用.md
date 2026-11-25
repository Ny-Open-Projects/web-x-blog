---
title: [CSS-260] :where() 与 :is() 的区别：优先级为零的妙用
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 选择器]
type: 面试题
---

## CSS-260：:where() 与 :is() 的区别

**答**：
- 共同点：简化选择器组，`:is(h1, h2, h3)` 替代三行重复；都能写复杂条件（:is(input:not([type=submit]), button)）
- 区别在优先级：:is() 取「组内最高优先级」；:where() 恒为 0——后者专用于「默认样式可被任意覆盖」
- 典型用法：reset 用 :where()——` :where(h1, h2) { margin: 0 } `，业务任何一条同名规则都能赢，无需 !important
- 配合选择器组：` :where(.dark) .card { … } ` 前缀条件不增加权重——主题包装不污染优先级
- 兼容：2021 起全主流支持，可生产

```css
/* reset：零优先级，可被覆盖 */
:where(h1, h2, h3) { margin: 0; font-weight: 600; }

/* 主题前缀不加权重 */
:where(.dark) .card { background: #222; }

/* 对比：:is() 取组内最高优先级 */
:is(#main, .box) { color: red; }  /* 命中 #main 时权重 = ID 级 */
```
