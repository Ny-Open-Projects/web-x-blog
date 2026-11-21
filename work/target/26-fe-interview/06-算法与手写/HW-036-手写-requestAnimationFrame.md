---
title: [HW-036] 手写 requestAnimationFrame 动画（缓动）
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-036：手写 requestAnimationFrame 动画（缓动）

**答**：
- 评分点：rAF 回调拿到的 `now` 时间戳要用它**按时间算进度** `p = min((now - start) / duration, 1)`，绝不能用帧数累加（掉帧时不同步）；进度 p ∈ [0,1] 传给缓动函数（easeOutCubic 等要会写一两个），再映射到 from→to 的插值；p === 1 时结束并调 onDone，返回 cancel 函数内部 `cancelAnimationFrame`；动画值 onUpdate 每帧回调；能说出 rAF 在页面不可见时自动暂停、比 setInterval 不丢帧不掉频。

```javascript
// ===== 5 分钟速写版 =====
function animate({ from = 0, to = 100, duration = 300, easing = t => t, onUpdate, onDone }) {
  let rafId;
  const step = now => {
    const p = Math.min((now - start) / duration, 1); // 时间驱动进度
    onUpdate(from + (to - from) * easing(p));
    if (p < 1) rafId = requestAnimationFrame(step);
    else onDone && onDone();
  };
  let start;
  rafId = requestAnimationFrame(now => { start = now; step(now); }); // 首帧定起点
  return () => cancelAnimationFrame(rafId);
}

// ===== 标准完整版（含边界处理）=====
// 常用缓动函数（面试会要求现场写一个）
const easings = {
  linear: t => t,
  easeInQuad: t => t * t,
  easeOutCubic: t => 1 - Math.pow(1 - t, 3),
  easeInOutQuad: t => (t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2)
};
function animatePro({ from = 0, to = 100, duration = 300, easing = easings.easeOutCubic,
                      onUpdate, onDone, onAbort }) {
  if (duration <= 0) throw new TypeError('duration must be positive');
  if (typeof onUpdate !== 'function') throw new TypeError('onUpdate is required');
  let rafId = null;
  let start = null;
  let finished = false;
  const step = now => {
    if (start === null) start = now;                 // 首帧才确定起始时间，避免 setTimeout 抖动
    const p = Math.min((now - start) / duration, 1); // 永远用时间戳算进度
    onUpdate(from + (to - from) * easing(p));
    if (p >= 1) {
      finished = true;
      rafId = null;
      onDone && onDone(from + (to - from) * easing(1));
      return;
    }
    rafId = requestAnimationFrame(step);
  };
  rafId = requestAnimationFrame(step);
  return function cancel() {
    if (rafId === null || finished) return;
    cancelAnimationFrame(rafId);
    rafId = null;
    onAbort && onAbort(); // 取消回调：组件卸载时清理状态
  };
}
// 用法：滚动到顶部
// animatePro({ from: window.scrollY, to: 0, duration: 500,
//   onUpdate: v => window.scrollTo(0, v) });
```

---
