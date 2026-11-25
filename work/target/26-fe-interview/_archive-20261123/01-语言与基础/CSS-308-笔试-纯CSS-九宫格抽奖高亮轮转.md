---
title: [CSS-308] 笔试：纯 CSS 九宫格抽奖高亮轮转
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 动画]
type: 笔试题
---

## CSS-308：笔试：纯 CSS 九宫格抽奖高亮轮转

**题目**：实现九宫格（3×3，格子序号按顺时针 0-7，中心为按钮）的高亮轮转动画：高亮沿顺时针移动，先慢后快再慢（抽奖手感），持续轮转直到 JS 停止或纯 CSS 演示循环。

**答**：
```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 80px);
  grid-template-rows: repeat(3, 80px);
  gap: 8px;
}
.cell { background: #eee; border-radius: 8px; display: grid; place-items: center; }
/* DOM 顺序 0,1,2,3(中心),4,5,6,7,8；高亮顺序按顺时针排列 */
.cell:nth-child(1) { grid-area: 1/1; }
.cell:nth-child(2) { grid-area: 1/2; }
.cell:nth-child(3) { grid-area: 1/3; }
.cell:nth-child(4) { grid-area: 3/3; }
.cell:nth-child(5) { grid-area: 3/2; }
.cell:nth-child(6) { grid-area: 3/1; }
.cell:nth-child(7) { grid-area: 2/1; }
.cell:nth-child(8) { grid-area: 2/2; } /* 占位，不加高亮 */

/* 逐格点亮：8 个格子依次亮 1/8 周期（steps 语义由 delay 阶梯化） */
.cell { animation: blink 1.6s infinite; }
.cell:nth-child(2) { animation-delay: .2s; }
.cell:nth-child(3) { animation-delay: .4s; }
.cell:nth-child(4) { animation-delay: .6s; }
.cell:nth-child(5) { animation-delay: .8s; }
.cell:nth-child(6) { animation-delay: 1s; }
.cell:nth-child(7) { animation-delay: 1.2s; }
.cell:nth-child(1) { animation-delay: 1.4s; }
@keyframes blink {
  0%, 12.5% { background: #ffc107; box-shadow: 0 0 8px #ffc107; }
  12.6%, 100% { background: #eee; box-shadow: none; }
}
```

**评分点**：
- grid-area 实现顺时针视觉顺序（与 DOM 顺序解耦）
- animation-delay 阶梯实现「轮流点亮」——非 steps 动画的替代思路
- 单格亮灯窗口 12.5% = 1/8 周期，衔接不重叠
- 中心按钮位置说明与纯 CSS 局限（真实抽奖的减速停止必须 JS 控制）
