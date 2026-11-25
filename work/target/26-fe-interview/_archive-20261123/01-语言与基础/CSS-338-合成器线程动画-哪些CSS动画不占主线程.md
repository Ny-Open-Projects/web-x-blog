---
title: [CSS-338] 合成器线程动画：哪些 CSS 动画不占主线程
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-338：合成器线程动画：哪些 CSS 动画不占主线程

**答**：
- 合成器线程动画条件：只动画 transform/opacity、元素已提层、动画属性无主线程依赖——主线程卡死（长任务）时动画依然流畅，这是「合成器动画」的判别标准
- 提层触发：will-change: transform/opacity、3d transform、animation 显式 transform/opacity（引擎自动提升）；filter/box-shadow 动画全在主线程
- 主线程参与的例外：CSS 变量驱动（var 在 keyframes 中要重算样式）、动画与布局属性混写（width 与 transform 同一动画）、未提层元素的首帧
- scroll-timeline/驱动动画：滚动进度驱动动画早期版本在主线程（scroll 事件），新 scroll() 时间线函数由合成器直接驱动——滚动视差可以零主线程成本
- 验证方法：主线程注入死循环任务，动画仍流畅 → 合成器动画；卡顿 → 主线程动画，需要修

```css
/* 合成器动画 */
.spinner { animation: spin 1s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
/* 滚动驱动: 合成器直接吃滚动进度 */
.parallax {
  animation: parallax linear;
  animation-timeline: scroll(root);
}
@keyframes parallax { to { transform: translateY(-200px); } }
```
