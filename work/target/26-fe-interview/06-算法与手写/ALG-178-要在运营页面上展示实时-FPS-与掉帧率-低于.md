---
title: [ALG-178] 要在运营页面上展示实时 FPS 与掉帧率（低于 45 报警）。如何用 rAF 计数实现，并算出最严重掉帧？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-178：要在运营页面上展示实时 FPS 与掉帧率（低于 45 报警）。如何用 rAF 计数实现，并算出最严重掉帧？
**答**：rAF 每帧回调一次，窗口期（如 5s）内计数得 FPS；掉帧率 = `max(0, 1 - fps / 60)`（按设备刷新率基准更严谨）；同时记录相邻两帧的最大间隔 `worstGap`，定位最严重的单次卡顿（如一次 300ms 的 GC）。注意：rAF 在后台标签页被暂停，采样窗口自动"冻结"而非堆积回调。O(帧数)。

```javascript
function trackFPS(durationMs = 5000, onReport) {
  let frames = 0;
  let start = performance.now(), last = start, worstGap = 0;
  function loop(now) {
    frames++;
    worstGap = Math.max(worstGap, now - last); // 相邻两帧最大间隔 = 最严重掉帧
    last = now;
    if (now - start < durationMs) {
      requestAnimationFrame(loop);
    } else {
      const fps = frames / ((now - start) / 1000);
      const dropped = Math.max(0, 1 - fps / 60); // 60Hz 基准的掉帧率
      onReport({
        fps: Math.round(fps),
        dropped: +dropped.toFixed(2),
        worstGap: Math.round(worstGap),
      });
    }
  }
  requestAnimationFrame(loop);
}
// trackFPS(5000, r => { if (r.fps < 45) reportPerformanceIssue(r) })
```
