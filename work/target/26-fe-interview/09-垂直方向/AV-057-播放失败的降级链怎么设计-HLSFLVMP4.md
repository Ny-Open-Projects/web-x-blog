---
title: [AV-057] 播放失败的降级链怎么设计？（HLS→FLV→MP4）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-057：播放失败的降级链怎么设计？（HLS→FLV→MP4）
**答**：
- 源列表按优先级编排：HLS（自适应+生态好）→ HTTP-FLV（延迟低）→ MP4（点播兜底），同一内容服务端通常多协议同出。
- 触发降级的条件：连续 N 次网络错误、当前协议不支持（isTypeSupported 失败）、错误码 MEDIA_ERR_SRC_NOT_SUPPORTED。
- 降级要点：记录当前播放进度，新源 ready 后 seek 回原位（直播则跳到边缘）；每个源尝试时限（如 10s 超时算失败）。
- 配置中心下发源列表：事故时可热切换顺序，无需发版。
- 全链失败：展示错误页 + 重试按钮 + 客服入口，同时上报完整降级轨迹。

```javascript
// 多协议降级播放器
class FallbackPlayer {
  constructor(video, sources) {
    this.video = video;
    this.sources = sources; // [{ type:'hls', url }, { type:'flv', url }, { type:'mp4', url }]
    this.idx = 0; this.trail = [];
  }
  async play(fromSec = 0) {
    while (this.idx < this.sources.length) {
      const src = this.sources[this.idx];
      try {
        await this.attach(src, fromSec); // 挂载源（hls.js/flv.js/原生）
        await Promise.race([
          new Promise((r) => this.video.addEventListener('playing', r, { once: true })),
          new Promise((_, rej) => setTimeout(() => rej(new Error('timeout')), 10_000)),
        ]);
        return src.type; // 成功
      } catch (e) {
        this.trail.push({ type: src.type, url: src.url, err: String(e) });
        this.destroyEngine(); this.idx++; // 换下一个源
      }
    }
    this.showFatal(); // 全链失败
  }
  async attach({ type, url }, fromSec) {
    if (type === 'hls' && !this.video.canPlayType('application/vnd.apple.mpegurl')) {
      this.engine = new Hls.default({ maxBufferLength: 10 });
      this.engine.loadSource(url);
      this.engine.attachMedia(this.video);
    } else if (type === 'flv') {
      this.engine = flvjs.createPlayer({ type: 'flv', url, isLive: true });
      this.engine.attachMediaElement(this.video); this.engine.load();
    } else {
      this.video.src = url;
    }
    this.video.currentTime = fromSec;
    await this.video.play();
  }
  destroyEngine() { this.engine?.destroy?.(); this.engine = null; this.video.removeAttribute('src'); }
}
```
