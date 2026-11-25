---
title: [PER-1015] 手写一个滚动驱动进度组件（含 timeline 回退）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1015：手写一个滚动驱动进度组件（含 timeline 回退）

**答**：
- 需求：实现 ScrollProgress(el)。优先用 CSS animation-timeline: scroll()（注入样式，零 JS 每帧成本）；不支持时用 rAF + passive scroll 回退，并保证回退实现读写不抖动（只读 scrollTop/scrollHeight，只写 transform）。
- 边界：el 必须有滚动溢出否则进度恒 0；卸载函数清理回退监听；进度 clamp [0,1]。
- 评分点：特性检测分支；回退无抖动；clamp；卸载清理

```javascript
function ScrollProgress(el) {
  const bar = document.createElement('div');
  bar.style.cssText = 'position:sticky;top:0;height:3px;transform-origin:0 50%';
  el.prepend(bar);
  let cleanup = null;
  if (CSS.supports('animation-timeline: scroll()')) {
    bar.style.animation = 'grow linear forwards';
    bar.style.animationTimeline = 'scroll(nearest)';
  } else {
    let ticking = false;
    const onScroll = () => {
      if (ticking) return; ticking = true;
      requestAnimationFrame(() => {
        const max = el.scrollHeight - el.clientHeight;
        bar.style.transform =
          `scaleX(${Math.min(1, Math.max(0, el.scrollTop / max))})`;
        ticking = false;
      });
    };
    el.addEventListener('scroll', onScroll, { passive: true });
    cleanup = () => el.removeEventListener('scroll', onScroll);
  }
  return { destroy: () => { cleanup?.(); bar.remove(); } };
}
```
