---
title: [PER-973] scroll 事件监听如何迁移到合成器友好方案
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-973：scroll 事件监听如何迁移到合成器友好方案

**答**：
- scroll 监听每次滚动都跑在主线程，若回调含布局读/样式写即卡顿源；scroll-driven CSS / IntersectionObserver 是零主线程成本替代。
- 迁移映射：滚动进度条→animation-timeline: scroll()；元素入场→animation-timeline: view()；吸顶/懒加载→IntersectionObserver；视差→CSS 变量 + timeline。
- 必须用 scroll 事件时： passive: true（不阻塞滚动）+ rAF 合帧 + 只读不写布局。
- 深水：合成器线程处理滚动本身，主线程忙不会让滚动卡，但会拖慢"滚动触发的视觉反馈"。

```javascript
/* 滚动进度条：无 JS */
.topbar { position: fixed; height: 3px; background: var(--accent);
  transform-origin: 0 50%;
  animation: progress linear forwards;
  animation-timeline: scroll(root); }
@keyframes progress { from { transform: scaleX(0) } to { transform: scaleX(1) } }
// 兼容检测
if (!CSS.supports('animation-timeline: scroll()')) {
  // 回退：rAF 节流监听
  let ticking = false;
  addEventListener('scroll', () => {
    if (ticking) return; ticking = true;
    requestAnimationFrame(() => {
      bar.style.transform = `scaleX(${scrollY / (document.body.scrollHeight - innerHeight)})`;
      ticking = false;
    });
  }, { passive: true });
}
```
