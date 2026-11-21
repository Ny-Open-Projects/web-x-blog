---
title: [CSS-184] JS 与 CSS 的断点如何统一管理（matchMedia）？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-184：JS 与 CSS 的断点如何统一管理（matchMedia）？

**答**：
- 两侧断点必须同源：单一配置（构建期共享的 breakpoints 常量）同时生成 CSS 媒体查询与 JS 判断，或反向由 CSS 变量提供数值。
- 运行时监听：`matchMedia(query).addEventListener('change')`，回调拿 `e.matches`；老浏览器用 addListener。
- 初始状态别忘了同步一次（change 只在变化时触发）。
- 典型用途：JS 侧的轮播是否启用、虚拟列表列数、事件节流策略随断点切换，与 CSS 布局保持同一步调。

```javascript
// 方案一：构建期共享 breakpoints 常量（tailwind/PostCSS 同源配置）
const BP = { md: 768, lg: 1208 };
const mq = window.matchMedia(`(max-width: ${BP.md}px)`);
function sync(e) {
  isMobile = e.matches;
  renderNav();          // JS 行为与 CSS 断点同步
}
mq.addEventListener('change', sync);   // 老浏览器：mq.addListener(sync)
sync(mq);                              // 初始状态必须同步一次

// 方案二：CSS 变量提供断点数值，JS 动态构造查询
const bp = getComputedStyle(document.documentElement)
  .getPropertyValue('--bp-md');        // "768px"
const mq2 = matchMedia(`(max-width: ${bp})`);
mq2.addEventListener('change', e => {
  grid.setColumns(e.matches ? 1 : 3);
});

// 方案三：一次性判断（非监听场景）
if (matchMedia('(prefers-reduced-motion: reduce)').matches) skipIntro();
```

## 三十、调试与质量
