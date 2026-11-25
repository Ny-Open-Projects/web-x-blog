---
title: [HW-162] 手写字体加载状态机——FontFaceSet loadingdone/loadingerror 事件驱动的多字体降级
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-162：手写字体加载状态机——FontFaceSet loadingdone/loadingerror 事件驱动的多字体降级
**答**：多字体（标题体/正文体/等宽体）独立降级：document.fonts 事件驱动（loadingdone/loadingerror）——字体失败逐个降级（标题体失败用次选/系统字体），页面级 loading class 的解除按"关键字体集"判定（部分字体失败不阻塞关键路径渲染）。

```javascript
function fontStateMachine(criticalFonts, fallbacks) {
  // criticalFonts: ['PingFang-Title', 'PingFang-Body']  关键字体：全好才解除 loading
  // fallbacks: { 'PingFang-Title': 'system-title', ... }
  const state = new Map(criticalFonts.map((f) => [f, 'loading']));
  document.fonts.addEventListener('loadingdone', (e) => {
    for (const face of e.fontfaces) state.set(face.family, 'loaded');
    update();
  });
  document.fonts.addEventListener('loadingerror', (e) => {
    for (const face of e.fontfaces) {
      state.set(face.family, 'error');
      applyFallback(face.family);                          // 单字体失败：局部降级
    }
    update();
  });
  function update() {
    const allCritical = criticalFonts.every((f) => ['loaded', 'error'].includes(state.get(f)));
    if (allCritical) document.documentElement.classList.remove('fonts-loading');
  }
  function applyFallback(family) {                          // 局部降级：切换 CSS 变量
    document.documentElement.style.setProperty(`--font-${family}`, fallbacks[family] ?? 'sans-serif');
  }
  // 超时兜底：3s 仍未完成 → 强制解除 loading（font-display swap 兜底渲染）
  setTimeout(() => document.documentElement.classList.remove('fonts-loading'), 3000);
}
// 与 PER-218 的差异：多字体独立状态机（单字体失败不阻塞其他关键字体路径）
// loadingerror 的降级是"局部"的（标题体失败换标题备选，正文体继续等）
```

**评分点**：
- 多字体独立状态机（关键字体集判定解除时机）——比 PER-218 单一版更工程化。
- loadingerror 局部降级（CSS 变量切换备选）。
- 超时兜底强制解除（不留死锁）。
- document.fonts 事件（loadingdone/loadingerror）的使用正确。
