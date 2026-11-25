---
title: [CSS-314] 笔试：CSS 实现 0.5px 边框
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 移动端]
type: 笔试题
---

## CSS-314：笔试：CSS 实现 0.5px 细边框

**题目**：DPR=2/3 屏幕上 1px 边框显粗，实现物理 0.5px 视觉细线：至少两种方案（含 modern 原生检测）。

**答**：
```css
/* 方案一：0.5px 直接声明（Safari/Chrome 108+ 支持，浏览器四舍五入策略不同） */
.hairline {
  border: 0.5px solid #ddd;
}

/* 方案二：伪类缩放（兼容性最强） */
.hairline-scale { position: relative; }
.hairline-scale::after {
  content: ''; position: absolute;
  top: 0; left: 0;
  width: 200%; height: 200%;
  border: 1px solid #ddd;
  transform: scale(0.5);          /* 1px × 0.5 = 0.5px 物理 */
  transform-origin: 0 0;
  pointer-events: none;
  box-sizing: border-box;
}

/* 方案三：@supports 组合：原生支持优先，否则回退缩放 */
.hairline-scale::after { display: none; }
@supports not (border: 0.5px solid #ddd) {
  .hairline-scale::after { display: block; }
}
```

**评分点**：
- 0.5px 原生支持的浏览器差异（部分浏览器舍入为 0 或 1px）——所以需要检测
- scale(0.5) 方案的 width/height 200% 与 transform-origin: 0 0 细节
- pointer-events: none（伪类不挡交互）
- @supports 优先级组合
