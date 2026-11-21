---
title: [CSS-317] 笔试：CSS 手风琴展开动画（grid 0fr/1fr）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 动画]
type: 笔试题
---

## CSS-317：笔试：CSS 手风琴展开动画

**题目**：实现任意高度内容的展开/收起动画：不用 JS 量高度、不用 max-height 猜测值，点击标题平滑展开。给出两种纯 CSS 状态切换方案（checkbox hack 与 :has）。

**答**：
```css
/* 共用：grid 0fr→1fr 动画高度（内容高度任意） */
.acc .body {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .35s ease;
}
.acc .body > div { overflow: hidden; min-height: 0; }  /* 关键：min-height:0 允许收缩 */

/* 方案一：:has（checkbox 视觉隐藏放 body 直下） */
.acc:has(> .toggle:checked) .body { grid-template-rows: 1fr; }
.acc > .toggle { position: absolute; opacity: 0; }

/* 方案二：details + interpolate-size（现代浏览器） */
html { interpolate-size: allow-keywords; }
details.acc2 .body { height: 0; overflow: hidden; transition: height .35s; }
details.acc2[open] .body { height: auto; }  /* auto 可动画了 */

/* 指示箭头 */
.acc:has(.toggle:checked) .arrow { transform: rotate(180deg); }
.arrow { transition: transform .35s; }
```

**评分点**：
- grid 0fr/1fr + overflow hidden + min-height: 0 三件套（缺 min-height 会不收缩）
- :has 联动 checkbox 的结构
- interpolate-size 方案与兼容性说明
- 动画属性是 grid-template-rows（不是 height），能解释为什么这样可行
