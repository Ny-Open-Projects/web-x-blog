---
title: [CSS-088] prefers-reduced-motion 的系统性处理方案是什么？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-088：prefers-reduced-motion 的系统性处理方案是什么？

**答**：
- 系统级开关：媒体查询读取用户的"减少动态效果"设置，全局收敛动画行为。
- 不是一刀切禁用：位移/缩放类动画替换为 opacity 淡入，保留反馈但去除眩晕源。
- token 化处理：定义 `--motion-duration/--motion-distance` 变量，reduced 时统一归零。
- JS 动画（WAAPI、canvas、滚动劫持）用 `matchMedia` 同步判断，与 CSS 行为一致。
- view transitions、平滑滚动等隐式动效也要纳入同一开关。

```css
:root { --motion-duration: 0.3s; --motion-distance: 24px; }

@media (prefers-reduced-motion: reduce) {
  :root { --motion-duration: 0.01s; --motion-distance: 0px; }
  html { scroll-behavior: auto; }          /* 关闭平滑滚动 */
  *, *::before, *::after {
    animation-duration: var(--motion-duration) !important;
    transition-duration: var(--motion-duration) !important;
    animation-iteration-count: 1 !important; /* 停掉无限循环动画 */
  }
}

/* 淡入类保留：只用 opacity，不产生位移 */
.fade-in { animation: fade var(--motion-duration) both; }
@keyframes fade { from { opacity: 0; } }
```

```javascript
// JS 动画与 CSS 保持同一开关
const reduced = matchMedia('(prefers-reduced-motion: reduce)');
el.animate([{ opacity: 0 }, { opacity: 1 }],
  { duration: reduced.matches ? 0 : 300 });
reduced.addEventListener('change', syncMotionPreference);
```

## 十六、视觉与图形
