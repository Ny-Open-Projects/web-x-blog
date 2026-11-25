---
title: [CSS-316] 笔试：CSS 三角形与气泡箭头（含 border 变体）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 效果]
type: 笔试题
---

## CSS-316：笔试：CSS 三角形与气泡箭头

**题目**：实现：① 上/下/左/右四个方向的三角 ② 带边框的气泡箭头（箭头要有描边）③ clip-path 现代方案。

**答**：
```css
/* 方案一：border 三角原理（宽高为 0，边框拼合） */
.tri-up {
  width: 0; height: 0;
  border-left: 8px solid transparent;
  border-right: 8px solid transparent;
  border-bottom: 12px solid #333;   /* 只有底边有颜色 → 向上三角 */
}
.tri-down { border-top: 12px solid #333; border-bottom: none; }

/* 方案二：带边框的气泡箭头（双层三角叠放） */
.bubble { position: relative; background: #fff; border: 1px solid #ddd; border-radius: 6px; }
.bubble::before {   /* 描边层三角（大一号） */
  content: ''; position: absolute;
  top: -12px; left: 20px;
  border: 6px solid transparent;
  border-bottom-color: #ddd;
}
.bubble::after {    /* 填充层三角（盖住描边内沿） */
  content: ''; position: absolute;
  top: -11px; left: 20px;
  border: 6px solid transparent;
  border-bottom-color: #fff;
}

/* 方案三：clip-path（现代，支持任意形状） */
.tri-clip { width: 16px; height: 12px; background: #333;
  clip-path: polygon(0 0, 100% 0, 50% 100%); }
```

**评分点**：
- border 三角的透明边原理（相对方向着色）
- 带边框箭头的双层叠放（描边层在上、填充层偏移 1px 盖住内沿）
- clip-path polygon 的坐标语义
- 各方案取舍（border 老练、clip 现代、SVG 最可控）
