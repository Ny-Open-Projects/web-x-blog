---
title: [AV-341] MSE（Media Source Extensions）工作原理与坑
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-341：MSE（Media Source Extensions）工作原理与坑

**答**：
- MSE：JS 拼装 MP4/WebM 片段喂给 SourceBuffer，video 播放——HLS/DASH 播放器核心。
- 坑集：SourceBuffer 必须 updateend 后 appendNext、时间戳不单调会报错、codec 与容器必须匹配（fMP4）。
- 内存：buffer 超限要手动 remove（按时间区间清理），否则内存涨爆。

```javascript
// MSE 播放器骨架
class MSEPlayer {
  constructor(video, mime) {
    this.ms = new MediaSource();
    video.src = URL.createObjectURL(this.ms);
    this.mime = mime;
  }
  async init() {
    await new Promise(r => this.ms.addEventListener('sourceopen', r, { once: true }));
    this.sb = this.ms.addSourceBuffer(this.mime);
    await this.append(await fetchInit());
  }
  append(buf) {
    return new Promise(r => {
      this.sb.addEventListener('updateend', () => r(), { once: true });
      this.sb.appendBuffer(buf);
    });
  }
  evict(keepBehind = 30) {                            // 内存治理
    const ranges = this.sb.buffered;
    if (ranges.length && video.currentTime > keepBehind)
      this.sb.remove(0, video.currentTime - keepBehind);
  }
}
```
