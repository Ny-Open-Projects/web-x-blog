---
title: [AV-357] 视频质量控制：QP 与关键帧间隔的动态调整
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-357：视频质量控制：QP 与关键帧间隔的动态调整

**答**：
- 拥塞时：优先降码率（增 QP）→ 降帧率 → 降分辨率（感知影响从小到大）。
- 关键帧：拥塞后立即请求 IDR（恢复锚点），但 IDR 体积大（瞬间峰值）——权衡网络突发。
- 实现：WebRTC sender 内置拥塞控制，自定义需 WebCodecs + 自研拥塞。

```javascript
// 降级阶梯
function congestionLadder(step, current) {
  const steps = [
    () => ({ qpBump: 2, note: 'QP+2 码率 -20%' }),
    () => ({ fps: current.fps * 0.75, note: '降帧 25%' }),
    () => ({ resScale: 0.75, note: '分辨率 75%' }),
    () => ({ resScale: 0.5, fps: 15, note: '极限档' }),
  ];
  return steps[Math.min(step, steps.length - 1)]();
}
// 恢复：网络好转 30s 后逐级回升（防抖动）
```
