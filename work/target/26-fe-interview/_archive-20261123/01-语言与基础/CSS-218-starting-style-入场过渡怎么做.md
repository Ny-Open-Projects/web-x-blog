---
title: [CSS-218] @starting-style 是什么：入场过渡怎么做
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-218：@starting-style：入场过渡怎么做

**答**：
- 长期难题：元素「插入 DOM 时」直接以最终样式出现，transition 没有起点无法触发
- @starting-style：声明「首次渲染的起点样式」，浏览器从它过渡到正常样式——入场动画纯 CSS
- 语法：`@starting-style { .toast { opacity: 0; transform: translateY(20px); } }`
- 配合 display 过渡（transition-behavior: allow-discrete）可实现「display:none → block」的完整出入场
- 适用：toast、popover、dialog、列表项插入——所有「动态插入」场景

```css
.toast {
  opacity: 1;
  transform: translateY(0);
  transition: opacity .3s, transform .3s, overlay .3s allow-discrete, display .3s allow-discrete;
}
@starting-style {
  .toast { opacity: 0; transform: translateY(20px); } /* 插入时的起点 */
}
.toast.hide { opacity: 0; transform: translateY(20px); } /* 离场走这里 */
```
