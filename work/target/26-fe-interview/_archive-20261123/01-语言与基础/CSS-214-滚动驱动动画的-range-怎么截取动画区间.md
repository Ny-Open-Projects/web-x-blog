---
title: [CSS-214] 滚动驱动动画的 animation-range 怎么截取动画区间
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-214：滚动驱动动画的 animation-range 怎么截取动画区间

**答**：
- animation-range 限定「滚动进度里哪一段映射到关键帧 0%~100%」，让动画只在需要的滚动区间播放
- 语法：`animation-range: <start> <end>`——start/end 可用命名区间（entry/cover/exit）+ 偏移（`entry 20%`、`exit -10%`），或直接长度/百分比（`0px 300px`）
- 命名区间只对 view() 有意义；scroll() 时间轴用百分比或长度
- 常见配方：`entry 0% cover 40%`（进入后到滚动 40% 处）、`exit-crossing 0% exit-crossing 100%`（穿过中线时）
- 调试技巧：Chrome 动画面板可选中 timeline 直接拖动看区间映射，比脑算快

```css
.hero {
  animation: shrink linear both;
  animation-timeline: scroll(root block);
  animation-range: 0px 400px;  /* 只在前 400px 滚动内播放 */
}
@keyframes shrink { to { transform: scale(.8); opacity: .6; } }
```
