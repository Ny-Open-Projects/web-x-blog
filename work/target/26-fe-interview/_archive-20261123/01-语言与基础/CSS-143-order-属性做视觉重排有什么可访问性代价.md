---
title: [CSS-143] order 属性做视觉重排有什么可访问性代价？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-143：order 属性做视觉重排有什么可访问性代价？

**答**：
- order 只改视觉顺序，DOM 顺序不变：Tab 键焦点顺序、屏幕阅读器朗读顺序仍按 DOM 走，视觉与交互顺序割裂。
- 典型事故：order 把“提交按钮”视觉前置，但键盘用户按 Tab 却先落到其他按钮。
- 原则：能用 DOM 顺序解决的不要用 order；order 留给“小幅度视觉微调”（如置顶卡片 `order: -1`）并配合 aria 或语义验证。
- 自动化审计（axe/Lighthouse）会把“焦点顺序与视觉顺序不一致”标为问题，媒体查询重排优先用 grid-template-areas 或 flex-direction。

```css
/* 视觉重排：main 视觉在前，aside 与 ad 依次在后 */
.page { display: flex; }
.page .main  { order: 1; flex: 1; }
.page .aside { order: 2; width: 220px; }
.page .ad    { order: 3; width: 120px; }

/* 置顶卡片：小幅视觉调整，DOM 仍在原位 */
.feed { display: flex; flex-direction: column; }
.feed .pin { order: -1; background: #fffbe6; }

/* 风险演示：DOM 顺序是 aside → main，但视觉 main 在前，
   键盘 Tab 先进 aside 里的链接 —— 与用户看到的顺序相反 */
```
