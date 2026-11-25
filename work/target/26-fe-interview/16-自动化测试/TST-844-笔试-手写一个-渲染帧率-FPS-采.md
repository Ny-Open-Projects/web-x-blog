---
title: [TST-844] 笔试：手写一个「渲染帧率(FPS)采样器」，基于 requestAnimationFrame
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-844：笔试：手写一个「渲染帧率(FPS)采样器」，基于 requestAnimationFrame
**答**：
- 需求：实现 sampleFPS(durationMs) —— 用 requestAnimationFrame 采样回调间隔，统计平均 FPS 与掉帧数（间隔 > 32ms 记一次掉帧）。
- 规则：durationMs 内持续采样；FPS = 帧数 / 实际时长(秒)；掉帧数 = 间隔 > 32ms 的次数。
- 边界：在 Node 无 rAF 环境返回 Promise.reject 或空结果；时长 <= 0 返回 0。

```javascript
function sampleFPS(durationMs = 1000) {
  return new Promise(resolve => {
    if (typeof requestAnimationFrame === 'undefined') {
      return resolve({ fps: 0, dropped: 0, unsupported: true });
    }
    if (durationMs <= 0) return resolve({ fps: 0, dropped: 0 });
    let frames = 0, dropped = 0, last = 0, start = 0;
    function tick(now) {
      if (!start) start = now;
      if (last && now - last > 32) dropped++;
      frames++; last = now;
      if (now - start < durationMs) requestAnimationFrame(tick);
      else resolve({
        fps: Number((frames / ((now - start) / 1000)).toFixed(1)), dropped,
      });
    }
    requestAnimationFrame(tick);
  });
}
sampleFPS(1000).then(console.log); // { fps: ~60, dropped: 0 }
```
**评分点**：
- 用 rAF 采样并计算 FPS（帧数/实际时长），正确。
- 掉帧判定（间隔 > 32ms）与统计正确。
- 无 rAF 环境降级、时长<=0 返回 0，边界处理到位。
- 能点出 FPS 用于动画/滚动流畅度性能回归这一场景。
