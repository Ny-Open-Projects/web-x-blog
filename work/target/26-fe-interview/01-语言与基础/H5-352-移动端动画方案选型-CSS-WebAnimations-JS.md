---
title: [H5-352] 移动端动画方案选型：CSS、WAAPI 与 JS 驱动
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## H5-352：移动端动画方案选型：CSS、WAAPI 与 JS 驱动

**答**：
- 决策树：可预定义且只动 transform/opacity → CSS transition/animation（最省电，合成线程跑）；需要编排/暂停/取速率 → WAAPI（element.animate，可用 CSS 引擎）；需要跟手/物理 → JS + rAF
- CSS 动画的移动端坑：部分内核合成线程不接管复杂属性（box-shadow 动画全主线程）；animation-fill-mode 引发的常驻层内存；大量并发 animation 的调度开销
- WAAPI 优势：可暂停/seek/reverse、promise 结束回调、组合 transform，移动端支持度已好（iOS 13.1+）；CSS 与 WAAPI 可混合（keyframes 复用）
- JS 物理动画：spring 模型参数（刚度/阻尼）决定手感，跟手场景必须 JS 驱动；结束后 settle 回 CSS 便于中断接续
- 老机型兜底：检测 prefers-reduced-motion 与低端机 UA 降级为淡入淡出，砍掉复杂动画

```javascript
// WAAPI: 可编排且可中断接续
const anim = el.animate(
  [{ transform: 'translateX(0)' }, { transform: 'translateX(100vw)' }],
  { duration: 300, easing: 'cubic-bezier(.2,.8,.2,1)', fill: 'forwards' }
);
await anim.finished.catch(() => {});   // 取消也不抛未处理
anim.pause(); anim.playbackRate = 0.5; // 编排能力
const cur = el.getAnimations()[0]?.currentTime ?? 0; // 中断接续读当前值
// 跟手场景仍走 JS: touchmove 更新值 + rAF 写 transform
```
