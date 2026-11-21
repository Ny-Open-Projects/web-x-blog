---
title: [CSS-318] 笔试：CSS 骨架屏（渐变扫光）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 动画]
type: 笔试题
---

## CSS-318：笔试：CSS 骨架屏

**题目**：实现骨架屏：灰色占位块（圆形头像 + 两行文字）带从左到右的扫光动画；扫光循环平滑（无跳变）；暗色主题适配。

**答**：
```css
.skeleton {
  position: relative;
  background: #e8e8e8;
  border-radius: 6px;
  overflow: hidden;
}
/* 扫光：::after 平移，配合渐变无缝循环 */
.skeleton::after {
  content: '';
  position: absolute; inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(90deg,
    transparent,
    rgba(255,255,255,.6),
    transparent);
  animation: shimmer 1.4s infinite;
}
@keyframes shimmer { to { transform: translateX(100%); } }

/* 布局组合 */
.demo { display: flex; gap: 12px; align-items: center; }
.s-avatar { width: 48px; height: 48px; border-radius: 50%; flex: none; }
.s-line { height: 14px; }
.s-line.short { width: 40%; }

/* 暗色 */
[data-theme='dark'] .skeleton { background: #2a2a2a; }
[data-theme='dark'] .skeleton::after {
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.08), transparent);
}
/* 无动画偏好 */
@media (prefers-reduced-motion: reduce) {
  .skeleton::after { animation: none; }
}
```

**评分点**：
- ::after + translateX 扫光（不动背景，走合成）
- 循环无跳变：起始与结束都在元素外（-100% → 100%）
- 暗色主题下的扫光透明度调整
- prefers-reduced-motion 降级
