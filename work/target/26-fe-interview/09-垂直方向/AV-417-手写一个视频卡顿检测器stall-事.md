---
title: [AV-417] 手写一个视频卡顿检测器（stall 事件统计）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## AV-417：手写一个视频卡顿检测器（stall 事件统计）

**答**：
- 需求：implement stallTracker(video)。监听 waiting/playing 统计 stall：{ count, totalMs, maxMs, ratio }（ratio = stallMs / 观看时长）；连续 stall（间隔 < 1s）合并为一次；report() 输出指标。
- 边界：页面隐藏期间不计时；watchedMs 用 currentTime 增量累计（seek 不计）；空数据返回零值。
- 评分点：事件配对；合并连续；观看时长；QoE 分

```javascript
class stallTracker {
  constructor(video) {
    this.count = 0; this.totalMs = 0; this.maxMs = 0;
    this.watchedMs = 0; this._stallAt = null; this._lastTime = null;
    video.addEventListener('waiting', () => {
      if (this._stallAt && Date.now() - this._stallAt < 1000) return;   // 合并
      this._stallAt = Date.now();
      this.count++;
    });
    video.addEventListener('playing', () => {
      if (this._stallAt) {
        const ms = Date.now() - this._stallAt;
        this.totalMs += ms; this.maxMs = Math.max(this.maxMs, ms);
        this._stallAt = null;
      }
    });
    video.addEventListener('timeupdate', () => {
      if (this._lastTime != null && video.currentTime > this._lastTime)
        this.watchedMs += (video.currentTime - this._lastTime) * 1000;
      this._lastTime = video.currentTime;
    });
  }
  report() {
    return { count: this.count, totalMs: this.totalMs, maxMs: this.maxMs,
      ratio: +(this.totalMs / (this.watchedMs || 1)).toFixed(3),
      qoe: Math.max(0, 100 - this.count * 10
        - (this.totalMs / (this.watchedMs || 1)) * 100) };
  }
}
```
