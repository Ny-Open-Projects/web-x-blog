---
title: [CSS-061] :is() 和 :where() 有什么区别？为什么说 :where() 更适合写默认样式？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-061：:is() 和 :where() 有什么区别？为什么说 :where() 更适合写默认样式？

**答**：
- 两者都用于缩短选择器列表，`:is(h1, h2, h3)` 等价于逐个写出，且支持在复杂选择器中间嵌套。
- 核心差异在优先级：`:is()` 取参数中优先级最高的一条来计算；`:where()` 优先级恒为 0。
- 因此默认样式写 `:where()`，业务代码任何类选择器都能直接覆盖，无需 !important。
- 参数只能是复合选择器列表，不能包含伪元素。
- 均已进入 Baseline，现代浏览器可直接使用。

```css
/* :is() 优先级跟随参数中最高的那条（这里是 .nav a，0-1-1） */
:is(.nav, footer) a { color: #409eff; }

/* :where() 优先级恒为 0，任何普通类都能覆盖它 */
:where(h1, h2, h3) {
  margin-block: 0.5em;
  font-weight: 600;
}

/* 业务覆盖无需提高优先级 */
h2 { margin-block: 1em; } /* 轻松覆盖 :where 的 0.5em */
```
