---
title: [CSS-324] 笔试：CSS 无缝滚动 marquee
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 动画]
type: 笔试题
---

## CSS-324：笔试：CSS 无缝滚动 marquee

**题目**：实现跑马灯无缝循环：内容复制两份，平移一份宽度后回跳无感知；速度与内容宽度解耦（用百分比）；hover 暂停。

**答**：
```css
.marquee {
  overflow: hidden;
  white-space: nowrap;
}
.marquee-track {
  display: inline-flex;
  gap: 32px;
  animation: scroll 20s linear infinite;
}
.marquee:hover .marquee-track { animation-play-state: paused; }

/* 关键：内容渲染两份，位移 -50%（+ 半个 gap 修正）实现无缝 */
@keyframes scroll {
  to { transform: translateX(calc(-50% - 16px)); } /* gap/2 补偿 */
}
```
```html
<div class="marquee">
  <div class="marquee-track">
    <span>A</span><span>B</span><span>C</span>
    <span>A</span><span>B</span><span>C</span> <!-- 复制一份 -->
  </div>
</div>
```
```css
/* 无 gap 版更简单：两份内容等宽，位移 -50% 即可 */
.marquee-track2 { display: inline-flex; }
.marquee-track2 span { margin-right: 32px; } /* 用 margin 而非 gap，位移 -50% 严格成立 */
@keyframes scroll2 { to { transform: translateX(-50%); } }
```

**评分点**：
- 两份内容 + translateX(-50%) 的无缝原理（核心）
- gap 导致的 50% 偏差与 -50% - gap/2 修正（或改用 margin）——细节判分
- linear 匀速（循环不顿挫）；hover 暂停用 animation-play-state
- 内容宽度未知时用百分比（与宽度解耦）
