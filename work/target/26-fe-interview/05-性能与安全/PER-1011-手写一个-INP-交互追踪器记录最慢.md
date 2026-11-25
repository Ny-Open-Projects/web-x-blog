---
title: [PER-1011] 手写一个 INP 交互追踪器：记录最慢交互并关联慢帧
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1011：手写一个 INP 交互追踪器：记录最慢交互并关联慢帧

**答**：
- 需求：实现 trackINP()。监听 pointerdown/keydown（capture）记录交互开始时间与目标选择器；interaction 结束（下一帧渲染完成）计算 duration = frameStart - start；维护 Top3 最慢交互 { target, dur, hadLoaf }；返回 getTop()。用 rAF 与 event.timeStamp 精确测量，忽略 duration < 50ms。
- 边界：同一交互的多个事件类型只记一次（pointerdown 与 click 合并）；目标选择器最多 3 层；页面隐藏后停止采集。
- 评分点：timeStamp 基准；去重合并；Top3 维护；隐藏停止

```javascript
function trackINP() {
  const top = []; let pending = null; let seen = new Set();
  function sel(el, depth = 3) {
    let s = el.tagName?.toLowerCase();
    while (el.parentElement && --depth > 0) {
      el = el.parentElement;
      s = el.tagName.toLowerCase() + '>' + s;
    }
    return s;
  }
  ['pointerdown', 'keydown'].forEach(t =>
    addEventListener(t, e => {
      if (document.visibilityState === 'hidden') return;
      const id = `${e.type}@${e.timeStamp}`;
      if (seen.has(id)) return; seen.add(id);
      pending = { start: e.timeStamp, target: sel(e.target), t0: performance.now() };
    }, { capture: true, passive: true }));
  function frame(now) {
    if (pending) {
      const dur = now - pending.t0;        // 含处理+延时+渲染
      if (dur >= 50)
        top.push({ target: pending.target, dur: Math.round(dur) }),
        top.sort((a, b) => b.dur - a.dur), top.splice(3);
      pending = null;
    }
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
  return { getTop: () => [...top] };
}
```
