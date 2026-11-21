---
title: [OPT-130] 手势/拖动跟随类动画如何稳定 60fps？给出保障清单。
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-130：手势/拖动跟随类动画如何稳定 60fps？给出保障清单。

**答**：
- 清单①：事件回调里只做"记录坐标 + rAF 调度"，不在 pointermove 里直接改 DOM（一帧可能触发 120+ 次事件）。
- 清单②：样式变更只用 transform/opacity（composite only），禁止改 left/top/width 触发重排。
- 清单③：给跟手元素加 `will-change: transform` 提升图层，手势结束及时移除释放内存。
- 清单④：回调做无副作用优化（passive: true 阻止滚动阻塞），并加 pointercancel 处理防止半途卡死。

```javascript
// 一一对应：pointer events + rAF 节流的跟手拖动（60fps 模板）
const el = document.querySelector('.draggable');
let pending = null, startX = 0, startY = 0, baseX = 0, baseY = 0;

el.addEventListener('pointerdown', e => {
  el.setPointerCapture(e.pointerId);            // 捕获，移出元素也持续收事件
  startX = e.clientX; startY = e.clientY;
  el.style.willChange = 'transform';            // 手势期间提升图层
});

el.addEventListener('pointermove', e => {
  if (pending) return;                          // 一帧只排一次任务
  pending = { x: e.clientX - startX, y: e.clientY - startY };
  requestAnimationFrame(() => {
    // rAF 里只做 composite 属性变更，不会触发 layout
    el.style.transform = `translate3d(${baseX + pending.x}px, ${baseY + pending.y}px, 0)`;
    pending = null;
  });
}, { passive: true });                          // passive 不阻塞滚动合成线程

function endGesture() {
  // 记录最终位移作为下次基准，并释放图层，避免常驻内存
  const m = new DOMMatrixReadOnly(getComputedStyle(el).transform);
  baseX = m.m41; baseY = m.m42;
  el.style.willChange = 'auto';
}
el.addEventListener('pointerup', endGesture);
el.addEventListener('pointercancel', endGesture); // 系统打断也要收尾
```
