---
title: [AV-376] 播放器内核抽象：多协议（HLS/DASH/MP4）统一接口
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-376：播放器内核抽象：多协议（HLS/DASH/MP4）统一接口

**答**：
- 内核分层：传输层（协议 loader）→ 拼装层（MSE/direct）→ 播放层（video 控制）。
- 统一接口：load(url)/play/pause/seek/setQuality + 事件总线——上层 UI 与协议解耦。
- 选型：自研内核成本高（dash.js/hls.js/xgplayer），通常二次封装。

```javascript
// 播放器内核接口
class PlayerKernel {
  async load(src) {
    const loader = pickLoader(src);      // hls/dash/mp4 by 扩展名/manifest
    this.feed = await loader.init();
    this.feed.on('segment', buf => this.mse.append(buf));
  }
  seek(t) { this.feed.seek(t); }
  setQuality(level) { this.feed.switchLevel(level); }
  destroy() { this.mse.detach(); this.feed.destroy(); }
}
function pickLoader(src) {
  if (src.includes('.m3u8')) return HLSLoader;
  if (src.includes('.mpd')) return DASHLoader;
  return FileLoader;
}
```
