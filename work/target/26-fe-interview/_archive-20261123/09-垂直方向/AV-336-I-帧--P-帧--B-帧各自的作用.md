---
title: [AV-336] I 帧 / P 帧 / B 帧各自的作用
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-336：I 帧 / P 帧 / B 帧各自的作用

**答**：
- I 帧（关键帧）：独立编码可解，是随机访问点（seek 起点）；体积最大（≈ 原始 5~10 倍压缩）。
- P 帧：参考前面帧预测，体积小；B 帧：双向预测（前后参考），压缩率最高但增加延迟。
- 参数影响：GOP 越长整体码率越低但 seek 慢/丢包扩散大；直播低延迟倾向 GOP 短或无 B 帧。

```javascript
// GOP 结构示意
function gopPlan({ gopSec = 2, fps = 30, hasB = false } = {}) {
  const frames = [];
  for (let g = 0; g < 3; g++) {
    frames.push({ type: 'I', idx: g * gopSec * fps });    // 每 GOP 一个 I
    for (let i = 1; i < gopSec * fps; i++) {
      const t = g * gopSec * fps + i;
      frames.push(hasB && i % 2 === 0
        ? { type: 'B', idx: t, ref: [t - 2, t + 1] }
        : { type: 'P', idx: t, ref: [t - 1] });
    }
  }
  return { frames, seekLatency: gopSec };   // 最坏 seek = GOP 长度
}
```
