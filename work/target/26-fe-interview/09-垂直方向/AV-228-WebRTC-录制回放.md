---
title: [AV-228] WebRTC 录制回放：时间戳与索引设计
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 笔试题, 26]
type: 笔试题
---

## AV-228：WebRTC 录制回放：时间戳与索引设计

**答**：
- 题目：会议录制回放——服务端录制文件按时间分片（5 分钟/片），前端回放器支持「按时间跳转（seek 跨片）+ 事件对齐（白板/聊天同步回放）」。
- 思路：分片索引（每片起始时间戳）；seek = 定位分片 → 加载该片 → 对齐偏移；事件流（白板操作/聊天）按录制时间戳重放。
- 评分点：分片索引与 seek；事件流对齐；片间无缝拼接。

```javascript
class PlaybackSession {
  constructor(recording) {
    this.segments = recording.segments;                     // [{url, startTs, duration}]
    this.events = recording.events;                         // [{ts, type, payload}]
  }
  seek(ts) {                                                 // 跨片 seek
    const seg = this.segments.find(s =>
      ts >= s.startTs && ts < s.startTs + s.duration);
    this.player.load(seg.url);
    this.player.currentTime = ts - seg.startTs;             // 片内偏移
    this.playEventsAfter(ts);
  }
  playEventsAfter(ts) {                                      // 事件流对齐重放
    const pending = this.events.filter(e => e.ts >= ts);
    const start = performance.now();
    const replay = () => {
      const elapsed = performance.now() - start;
      while (pending.length && pending[0].ts - ts <= elapsed)
        applyEvent(pending.shift());                        // 白板/聊天按录制节奏重放
      if (pending.length) requestAnimationFrame(replay);
    };
    requestAnimationFrame(replay);
  }
}
```
