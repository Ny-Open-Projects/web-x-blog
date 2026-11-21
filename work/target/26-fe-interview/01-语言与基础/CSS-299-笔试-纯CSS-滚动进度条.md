---
title: [CSS-299] 笔试：纯 CSS 滚动进度条
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 动画]
type: 笔试题
---

## CSS-299：笔试：纯 CSS 滚动进度条

**题目**：纯 CSS 实现右侧竖向滚动进度指示（高度随滚动变化），并额外实现「当前章节高亮」：滚动到某 section 时对应目录项变色。只允许 CSS。

**答**：
```css
/* ① 竖向进度条 */
.progress {
  position: fixed; right: 0; top: 0;
  width: 4px; height: 100%;
  transform-origin: 50% 0;
  transform: scaleY(0);
  background: #4285f4;
  animation: fill linear both;
  animation-timeline: scroll(root block);
}
@keyframes fill { to { transform: scaleY(1); } }

/* ② 当前章节高亮：scroll-marker / scroll-driven 方案（新标准演进中），
      兼容落点用 view() 时间线 + 兄弟结构 */
.toc a { color: #888; }
.toc a:target { color: #4285f4; }      /* 锚点跳转后高亮（hash 方案） */

/* ③ 渐进增强：容器内 section 进入视口中线时高亮（实验性 selector 不可用时跳过） */
section {
  animation: highlight linear both;
  animation-timeline: view();
  animation-range: entry 0% exit 100%;
}
@keyframes highlight { to { background: #f6f8ff; } }

/* 降级 */
@supports not (animation-timeline: scroll()) {
  .progress { display: none; }
}
```

**评分点**：
- scaleY + transform-origin 与 scaleX 侧的选择说明（轴对应）
- scroll(root block) 时间轴语法完整
- 纯 CSS 下「章节高亮」能力边界清醒（:target/实验特性），不硬编 JS 逻辑
- @supports 降级
