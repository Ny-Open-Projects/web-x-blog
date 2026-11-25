---
title: [AV-370] 卡顿率与 QoE 指标体系
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-370：卡顿率与 QoE 指标体系

**答**：
- 卡顿定义：缓冲事件（buffer 且时长 > 200ms）；卡顿率 = 卡顿用户/总用户 或 卡顿时长占比。
- QoE 指标：起播时间、卡顿率、码率均值、退出率（卡顿与流失强相关）。
- 关联分析：卡顿 2 次以上用户流失率 ×3——QoE 直接挂钩业务。

```javascript
// QoE 采集
class QoETracker {
  constructor(player) {
    this.bufferEvents = 0; this.bufferMs = 0;
    this.startAt = Date.now();
    player.on('waiting', () => this.bufferEvents++);
    player.on('playing', () => this.bufferMs = Date.now() - this._waitingAt);
    player.on('waiting', () => this._waitingAt = Date.now());
  }
  report(playerDuration) {
    const ratio = this.bufferMs / (playerDuration * 1000 || 1);
    return { bufferEvents: this.bufferEvents, stallRatio: +ratio.toFixed(3),
      qoeScore: Math.max(0, 100 - this.bufferEvents * 10 - ratio * 200) };
  }
}
```
