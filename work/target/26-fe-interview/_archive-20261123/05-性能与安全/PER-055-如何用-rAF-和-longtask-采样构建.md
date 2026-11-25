---
title: [PER-055] 如何用 rAF 和 longtask 采样构建 FPS/流畅度指标体系？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-055：如何用 rAF 和 longtask 采样构建 FPS/流畅度指标体系？

**答**：
- 流畅度三层指标：**FPS**（rAF 回调频率，低于 50 连续 N 帧记为掉帧段）、**长任务占比**（>50ms 的任务数/总时长）、**输入延迟**（pointerdown 到下一次 rAF 的间隔）。
- rAF 采样注意：页面在后台时 rAF 停发，要结合 `visibilitychange` 标记会话态，避免后台数据污染统计。
- 掉帧不能只算平均 FPS（会被好帧稀释），要用**最差连续 3 秒的最低帧率**或掉帧秒占比作为指标。
- 上报量控制：只在“发生劣化段”时上报现场（前后 1 秒的帧耗时序列 + 同时段长任务），否则每页只上报一条汇总。

```javascript
// 帧率采样器：记录每帧耗时，检测掉帧段并上报现场
const frames = [];
let last = performance.now();

function loop(now) {
  frames.push({ t: now, dt: now - last });
  last = now;
  if (frames.length > 600) frames.shift(); // 最多保留约 10 秒 @60fps
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);

// 长任务与 FPS 同窗观测，才能回答“是谁卡了帧”
new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    frames.push({ t: e.startTime, dt: e.duration, longTask: true });
  }
}).observe({ type: 'longtask', buffered: true });

// 每秒检查一次：最近 3 秒平均帧率低于 50 则视为劣化段，上报前后现场
setInterval(() => {
  const now = performance.now();
  const recent = frames.filter((f) => now - f.t < 3000 && !f.longTask);
  const fps = recent.length / 3;
  if (fps < 50) {
    const scene = frames.filter((f) => now - f.t < 1000);
    navigator.sendBeacon('/api/jank', JSON.stringify({ fps: Math.round(fps), scene }));
  }
}, 1000);

document.addEventListener('visibilitychange', () => {
  if (document.hidden) frames.push({ t: performance.now(), dt: 0, hidden: true }); // 后台段打标，统计时剔除
});
```
