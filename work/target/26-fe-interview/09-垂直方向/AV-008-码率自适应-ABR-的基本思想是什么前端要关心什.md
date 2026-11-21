---
title: [AV-008] 码率自适应 ABR 的基本思想是什么？前端要关心什么？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-008：码率自适应 ABR 的基本思想是什么？前端要关心什么？
**答**：
- 核心循环：测量（吞吐/缓冲水位）→ 决策（选下一个分片的码率档位）→ 执行（下载该档分片）。
- 两类经典策略：基于吞吐（估计带宽选不高于它的档）与基于缓冲（buffer 少则保守、多则激进，如 BBA）；MPC/DASH 引入预测优化。
- 播放端buffer 水位是关键信号：低于 2 个分片立即降档防卡顿；接近满档且带宽富余才升档。
- 前端职责：hls.js/dash.js 已内置 ABR，但需要会调参数（abrEwmaFastLive、maxBufferLength）、会手动 setLevel、会做自定义规则。
- 升档需对齐 I 帧 + 双 buffer 平滑切换，避免闪屏；直播场景还要兼顾延迟追帧。

```javascript
// 简化版 ABR 决策器：吞吐估计 + 缓冲水位双因子
class SimpleABR {
  constructor(levels) {
    this.levels = levels; // [{ bitrate: 500000, name: '360p' }, ...] 升序
    this.ewma = 2_000_000; // 吞吐指数加权估计，初始 2Mbps
    this.current = 0;
  }
  onSegmentDownloaded(bytes, durationMs) {
    const throughput = (bytes * 8) / (durationMs / 1000); // bps
    this.ewma = 0.7 * this.ewma + 0.3 * throughput; // 平滑
  }
  decide(bufferSec) {
    const levels = this.levels;
    let target = levels.findIndex((l) => l.bitrate > this.ewma * 0.9) - 1;
    if (target < 0) target = levels.length - 1;
    // 缓冲告急立即降档
    if (bufferSec < 2) target = 0;
    else if (bufferSec > 12 && target < levels.length - 1) target++; // 缓冲充足才升档
    target = Math.max(0, Math.min(target, levels.length - 1));
    this.current = target;
    return levels[target];
  }
}
const abr = new SimpleABR([
  { bitrate: 400_000, name: '360p' },
  { bitrate: 1_000_000, name: '720p' },
  { bitrate: 3_000_000, name: '1080p' },
]);
abr.onSegmentDownloaded(500_000, 4000); // 下载 500KB 用了 4s
console.log(abr.decide(1.5)); // 缓冲告急 → 360p
```

---

## 二、媒体标签与播放器（AV-009 ~ AV-015）
