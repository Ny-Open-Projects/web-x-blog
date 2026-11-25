---
title: [VIZ-353] 抖动（Jitter）与 TAA 的时间累积数学
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-353：抖动（Jitter）与 TAA 的时间累积数学

**答**：
- TAA：每帧在像素内亚像素抖动采样，历史帧与当前帧加权混合，等效超采样。
- 关键：抖动序列（Halton(2,3)）低差异分布，混合因子 ~0.1-0.2；运动时需 motion vector 重投影历史帧。
- 瑕疵：重投影失败产生鬼影（ghosting），需邻域裁剪（neighborhood clamp）限制历史帧颜色。

```javascript
// TAA 抖动序列（Halton）
function halton(index, base) {
  let f = 1, r = 0;
  while (index > 0) { f /= base; r += f * (index % base); index = Math.floor(index / base); }
  return r;
}
function jitterFrame(frameIdx) {
  return [halton(frameIdx % 16 + 1, 2) - 0.5,
          halton(frameIdx % 16 + 1, 3) - 0.5];
}
// 投影矩阵偏移：proj[8] += jx*2/width; proj[9] += jy*2/height
// 混合：color = lerp(history, current, 0.15)，历史先经 clamp
```
