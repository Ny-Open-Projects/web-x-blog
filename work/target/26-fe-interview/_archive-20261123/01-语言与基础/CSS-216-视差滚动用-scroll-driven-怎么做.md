---
title: [CSS-216] 视差滚动用 scroll-driven 怎么做，以前怎么做
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-216：视差滚动用 scroll-driven 怎么做

**答**：
- 旧方案：scroll 事件 + transform 修正——主线程抖动、每帧 JS
- 新方案：不同元素用 view() + animation-range 错开区间，或 scroll() + 不同速率的关键帧——纯声明式，滚动时在合成线程响应
- 视差本质：同一次滚动里，让不同元素移动不同「距离」——用关键帧位移量的差异实现
- 性能：只用 transform（合成属性），滚动与动画都在合成器侧，掉帧风险极低
- 兼容：不支持时自然退化为「所有元素同速滚动」（可接受的渐进增强）

```css
.layer-back {
  animation: drift linear both;
  animation-timeline: view();
  animation-range: cover 0% cover 100%;
}
@keyframes drift { from { transform: translateY(80px); } to { transform: translateY(-80px); } }
/* 前景层反向且幅度更小 → 产生视差 */
.layer-front { animation-name: drift-2; }
@keyframes drift-2 { from { transform: translateY(-30px); } to { transform: translateY(30px); } }
```
