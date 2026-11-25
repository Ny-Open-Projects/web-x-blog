---
title: [AV-343] ABR（自适应码率）算法：buffer-based vs throughput-based
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-343：ABR（自适应码率）算法：buffer-based vs throughput-based

**答**：
- throughput：估计最近网络吞吐，选不超过它的档位（保守留 20% 余量）。
- buffer-based：缓冲水位决定档位（BBA），吞吐波动时更稳。
- 混合（如 MPC）：动态规划权衡卡顿与质量，主流播放器（dash.js/hls.js）都用混合策略。

```javascript
// ABR 决策
function abrPick({ bufferSec, throughputKbps, levels, current }) {
  const safe = throughputKbps * 0.8;                  // 吞吐余量
  const byNet = levels.filter(l => l.kbps <= safe).pop();
  // buffer 水位修正：缓冲少时保守
  let target = byNet;
  if (bufferSec < 5) target = levels[Math.max(0, levels.indexOf(byNet) - 1)];
  if (bufferSec > 20) target = levels[levels.length - 1];   // 缓冲足冲高
  return { target,
    switchUp: target.kbps > levels[current].kbps,
    note: bufferSec < 3 ? '缓冲告急，禁止升档' : 'ok' };
}
```
