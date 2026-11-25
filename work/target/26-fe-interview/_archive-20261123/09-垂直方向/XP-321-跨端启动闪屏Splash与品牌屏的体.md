---
title: [XP-321] 跨端启动闪屏（Splash）与品牌屏的体验
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-321：跨端启动闪屏（Splash）与品牌屏的体验

**答**：
- 作用：掩盖启动空白（品牌展示）——但超 2s 用户流失。
- 实现：原生层闪屏（先于 WebView/引擎）+ 骨架衔接（闪屏淡出时页面已有内容）。
- 度量：闪屏到可交互时间；闪屏被跳过率（用户点击跳过）。

```javascript
// 闪屏衔接
function splashHandover(splashEl, readyPromise, { minShow = 800 } = {}) {
  const t0 = performance.now();
  return readyPromise.then(() => {
    const wait = Math.max(0, minShow - (performance.now() - t0));
    setTimeout(() => {
      splashEl.style.transition = 'opacity 300ms';
      splashEl.style.opacity = '0';
      setTimeout(() => splashEl.remove(), 300);      // 淡出后移除
    }, wait);
  });
}
```
