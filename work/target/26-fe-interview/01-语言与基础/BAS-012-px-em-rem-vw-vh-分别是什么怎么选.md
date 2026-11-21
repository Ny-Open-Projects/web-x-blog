---
title: [BAS-012] px、em、rem、vw、vh 分别是什么？怎么选？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-012：px、em、rem、vw、vh 分别是什么？怎么选？
**答**：
- px：固定像素，不随用户字号设置缩放。
- em：相对当前元素（继承）的 font-size，嵌套会复合放大，适合描述"相对当前字号"的间距。
- rem：相对根元素 font-size，整体字号与间距统一缩放的首选。
- vw/vh：视口宽/高的 1%；移动端 100vh 受地址栏影响，可用 svh/dvh 精确控制。

```css
html    { font-size: 16px; }
.title  { font-size: 1.5rem; }   /* 24px，随根字号整体缩放 */
.list   { font-size: 1.2em;  }   /* 相对父级字号，嵌套会叠加 */
.hero   { height: 100dvh;    }   /* 动态视口高度，兼容地址栏与软键盘 */
.sidebar{ width: 20vw;       }   /* 视口宽度的 20% */
```
