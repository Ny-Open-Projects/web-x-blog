---
title: [CSS-105] Skeleton 骨架屏的 shimmer 动画怎么实现？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-105：Skeleton 骨架屏的 shimmer 动画怎么实现？

**答**：
- 结构：占位块（灰底圆角）+ 一层斜向高光渐变左右平移，即 shimmer 扫光。
- 高光用 `linear-gradient(100deg, transparent, 白色半透明, transparent)` 平铺 200% 宽度做 background-position 动画。
- 只动 background-position 或 transform，走合成层不重排。
- 骨架布局要与真实内容一致（标题/头像/行高对齐），否则加载完成会跳动。
- 无障碍：容器加 `aria-busy="true"`，骨架块对读屏隐藏。

```html
<div class="skeleton-card" aria-busy="true">
  <div class="sk sk-avatar" aria-hidden="true"></div>
  <div class="sk sk-line" style="--w: 70%" aria-hidden="true"></div>
  <div class="sk sk-line" style="--w: 45%" aria-hidden="true"></div>
</div>
```

```css
.sk {
  position: relative;
  overflow: hidden;
  background: var(--bg-sunken);
  border-radius: 6px;
}
.sk::after {
  content: "";
  position: absolute; inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(
    100deg, transparent 20%,
    rgb(255 255 255 / 0.55) 50%, transparent 80%
  );
  animation: shimmer 1.4s infinite;
}
@keyframes shimmer { to { transform: translateX(100%); } }

.sk-avatar { width: 44px; height: 44px; border-radius: 50%; }
.sk-line   { height: 14px; width: var(--w, 100%); margin-block: 8px; }
```
