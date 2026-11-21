---
title: [CSS-179] getComputedStyle 读到的值有什么特点？自定义属性怎么读？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-179：getComputedStyle 读到的值有什么特点？自定义属性怎么读？

**答**：
- 普通属性返回**解析后的绝对值**：auto 会变成实际像素值，相对单位会被换算成 px，颜色返回 rgb/rgba。
- 自定义属性返回**声明原样字符串**（含空格），需要 trim/parseFloat 自己处理。
- 读样式会触发强制同步布局（若存在待处理的写操作），务必“先批量读、后批量写”避免布局抖动。
- 写自定义属性用 `el.style.setProperty('--x', v)`，支持继承级联，比直接改十几个 style 属性干净得多。

```javascript
const el = document.querySelector('.card');
const cs = getComputedStyle(el);

// 普通属性：解析后的绝对值
cs.width;            // "320px"（即使是 auto 也会算出实际值）
cs.marginTop;        // "0px"
cs.color;            // "rgb(0, 153, 102)"

// 自定义属性：声明原样字符串
const theme = cs.getPropertyValue('--theme').trim();  // "dark"
const gap = parseFloat(cs.getPropertyValue('--gap')); // "16px" → 16

// 避免布局抖动：批量读后再批量写
const widths = cards.map(c => getComputedStyle(c).width);   // 读阶段
cards.forEach((c, i) => c.style.width = widths[i]);         // 写阶段

// 写自定义属性
el.style.setProperty('--theme', 'light');
el.style.setProperty('--gap', '24px', 'important');
```
