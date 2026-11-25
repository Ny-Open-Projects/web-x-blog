---
title: [PER-966] Paint Holding 与导航白屏：浏览器怎么隐藏新页面的"未就绪时刻"
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-966：Paint Holding 与导航白屏：浏览器怎么隐藏新页面的"未就绪时刻"

**答**：
- Paint Holding：导航到同源页面时，浏览器保持旧页面画面，直到新页面首次绘制或超时，避免白屏闪烁。
- 对前端的含义：新页面 TTFB 后尽快渲染出有意义内容（哪怕骨架），让 holding 尽早解除；长时间无绘制则回退白屏。
- 配合 view-transitions API：同文档/跨文档过渡让页面切换有连续感，减少"跳动"。
- 实测：Chrome DevTools Performance 里观察 "Paint Holding" 与首次绘制时间的关系；SSR 页面收益最大。

```javascript
// 配合 paint holding：尽早有内容可画
// SSR 输出关键骨架，水合不阻塞首绘
document.addEventListener('DOMContentLoaded', () => {
  // 首屏骨架已在 HTML 中，浏览器可立即解除 paint holding
  document.startViewTransition?.(() => {
    // 同文档切换路由时包裹 DOM 更新，获得平滑过渡
    mount(nextRoute);
  });
});
```
