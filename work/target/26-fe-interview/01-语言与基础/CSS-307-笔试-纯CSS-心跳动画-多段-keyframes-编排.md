---
title: [CSS-307] 笔试：纯 CSS 心跳动画（多段 keyframes 编排）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 动画]
type: 笔试题
---

## CSS-307：笔试：纯 CSS 心跳动画

**题目**：实现逼真心跳：一次周期内「快跳两下 + 停顿」（扑通-扑通——停），非匀速非对称节奏；可缩放基线为 1，最大 1.15。

**答**：
```css
.heart {
  animation: beat 1.2s ease-in-out infinite;
  transform-origin: center;
}
@keyframes beat {
  0%   { transform: scale(1); }                  /* 静止 */
  14%  { transform: scale(1.15); }               /* 第一跳峰值 */
  28%  { transform: scale(1); }                  /* 回落 */
  42%  { transform: scale(1.12); }               /* 第二跳（略小） */
  70%  { transform: scale(1); }                  /* 长停顿开始 */
  100% { transform: scale(1); }                  /* 停满余下时间 */
}
```
```css
/* 扩展：心跳 + 颜色脉动（两个动画同周期叠加） */
.heart-glow {
  animation:
    beat 1.2s ease-in-out infinite,
    glow 1.2s ease-in-out infinite;
}
@keyframes glow {
  14% { filter: drop-shadow(0 0 6px rgba(226, 66, 66, .6)); }
  28% { filter: drop-shadow(0 0 0 transparent); }
  42% { filter: drop-shadow(0 0 4px rgba(226, 66, 66, .5)); }
  70% { filter: drop-shadow(0 0 0 transparent); }
}
```

**评分点**：
- 多段关键帧的非对称节奏（14%/28%/42%/70%）——不是 from/to 两帧的简单缩放
- 缩放基线与 transform-origin
- 多动画同周期叠加（transform + filter 各自关键帧对齐）
- 停顿用「重复的相同值关键帧」表达（70%~100% 持续 scale(1)）
