---
title: [AV-128] 卡顿率优化：buffer 策略与预测下载怎么做？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-128：卡顿率优化：buffer 策略与预测下载怎么做？（高频）
**答**：
- 卡顿根因两类：网速跟不上码率（供血不足）、buffer 策略激进（储备不足）；优化 = 多囤 + 少耗 + 提前预判。
- buffer 策略：直播要平衡追帧与流畅（目标 3-5s，超了加速播放追延迟）；点播大 buffer 无害但要防内存膨胀。
- 预测下载：按滚动窗口估计网速，预测"下一个分片耗时"，在卡顿发生前降档——不要等卡了才反应。
- 移动网络：切网（WiFi↔蜂窝）会断流，用 Network Information API + visibilitychange 提前加大 buffer（关联 AV-150）。
- 度量：卡顿率用"时长占比"与"频次"双口径，P90 卡顿时长比均值更贴近体验。

```javascript
// 预测式降档：不等卡顿先反应
class PredictiveStallGuard {
  constructor(player) { this.player = player; }   // player.levels / currentLevel 由 SDK 提供
  onSegmentDownloaded(bytes, ms, bufferSec, nextSegSeconds) {
    const observedBps = (bytes * 8) / (ms / 1000);
    const needBps = this.player.levels[this.player.currentLevel].bitrate;
    const headroom = observedBps / needBps;       // 网速相对当前码率的余量
    // 余量不足且 buffer 撑不过下一个分片 → 提前降档
    if (headroom < 1.3 && bufferSec < nextSegSeconds + 1) {
      this.player.switchLevel(Math.max(0, this.player.currentLevel - 1), 'predictive');
    }
    // 余量充足且 buffer 健康 → 恢复升档（升档冷却由上层控制）
    if (headroom > 2 && bufferSec > 12) {
      this.player.switchLevel(this.player.currentLevel + 1, 'recover');
    }
  }
}
```
