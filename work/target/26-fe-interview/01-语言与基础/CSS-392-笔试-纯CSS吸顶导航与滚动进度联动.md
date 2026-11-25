---
title: [CSS-392] 笔试：纯 CSS 吸顶导航与滚动进度联动
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 笔试题, 布局]
type: 笔试题
---

## CSS-392：笔试：纯 CSS 吸顶导航与滚动进度联动

**答**：实现：① 页头 sticky 吸顶且滚动离开顶部后加阴影与缩边（滚动检测用 scroll-driven animation 而非 JS）；② 顶部阅读进度条随滚动填充；③ 侧边目录当前项高亮（scroll-snap 或 scroll-margin 配合）。要求尽量纯 CSS（scroll-timeline），写出关键实现与降级思路。

```css
/* ① 吸顶 + 离开顶部变阴影: scroll(root) 时间线 + animation-range */
.header {
  position: sticky; top: 0;
  animation: elevate linear both;
  animation-timeline: scroll(root);
  animation-range: 0 120px;               /* 前120px滚动内完成变化 */
}
@keyframes elevate { to { box-shadow: 0 2px 8px #0001; } }

/* ② 进度条 */
.progress {
  transform-origin: 0 50%; transform: scaleX(0);
  animation: fill linear;
  animation-timeline: scroll(root);
}
@keyframes fill { to { transform: scaleX(1); } }

/* ③ 锚点跳转不遮挡: scroll-margin */
section { scroll-margin-top: 80px; }
```

```javascript
// 降级: 不支持 animation-timeline 时 JS 驱动
if (!CSS.supports('animation-timeline: scroll()')) {
  addEventListener('scroll', () => {
    const p = scrollY / (document.body.scrollHeight - innerHeight);
    progress.style.transform = `scaleX(${p})`;
    header.classList.toggle('scrolled', scrollY > 10);
  }, { passive: true });
}
```

**评分点**：
- animation-range 限定滚动区间实现「离开顶部才变化」
- sticky + scroll-margin 防锚点遮挡
- scroll-timeline 零主线程方案的优先级与 @supports 降级
- transform scaleX 驱动进度条（合成器友好）
