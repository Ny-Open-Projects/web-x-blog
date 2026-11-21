---
title: [AV-013] 播放器 buffer 管理怎么做？seek 时如何处理？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-013：播放器 buffer 管理怎么做？seek 时如何处理？
**答**：
- `video.buffered` 是 TimeRanges，用 `buffered.start(i)/end(i)` 遍历出已缓存区间；播放点距区间末尾 < 若干秒即认为将卡顿。
- 内存控制：只保留播放点前后窗口（如前 30s 后 5min），用 `sourceBuffer.remove(start, end)` 主动清理，监听 updateend 后再继续 append。
- seek 处理：目标在 buffered 内直接设 currentTime（立即起播）；在 buffer 外要先 abort 当前 append、清理或保留旧数据、下载包含目标点关键帧的分片再 append。
- seek 抖动（拖动条连续事件）要 debounce，避免风暴式请求。
- 直播 seek 一般被禁止或限制在"回到直播边缘"（liveEdge）。

```javascript
// buffer 清理器 + seek 处理
class BufferManager {
  constructor(sb, { backSec = 30, frontSec = 300 } = {}) {
    this.sb = sb; this.backSec = backSec; this.frontSec = frontSec;
  }
  async evict(currentTime) {
    const { sb } = this;
    if (sb.updating || !sb.buffered.length) return;
    const start = sb.buffered.start(0);
    if (currentTime - start > this.backSec) {
      sb.remove(start, currentTime - this.backSec); // 清理过旧的已播数据
      await new Promise((r) => sb.addEventListener('updateend', r, { once: true }));
    }
  }
  async seek(video, target, fetchSegment) {
    const { buffered } = video;
    for (let i = 0; i < buffered.length; i++) {
      if (target >= buffered.start(i) && target <= buffered.end(i)) {
        video.currentTime = target; // 命中缓存，直接跳
        return;
      }
    }
    // 未命中：等当前 append 完，下载目标点所在分片
    const sb = this.sb;
    if (sb.updating) {
      sb.abort();
      await new Promise((r) => sb.addEventListener('updateend', r, { once: true }));
    }
    video.currentTime = target;          // 先跳，UI 立即响应
    const buf = await fetchSegment(target); // 内部需对齐关键帧
    sb.appendBuffer(buf);
  }
}
```
