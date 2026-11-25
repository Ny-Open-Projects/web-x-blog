---
title: [AV-415] 手写一个 HLS 播放器加载器（hls.js 简化版）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## AV-415：手写一个 HLS 播放器加载器（hls.js 简化版）

**答**：
- 需求：实现 HlsLite.load(url)。解析 master（多码率选最高不超过带宽估计）-> 拉 media playlist -> 循环 appendBuffer 播放；buffer 低于 10s 时加载下一分片；输出 state 事件（loading/ready/stalled）。
- 边界：playlist 无分片时报错；fetch 失败重试 2 次后 emit error；video.currentTime 接近已缓冲末尾触发追帧。
- 评分点：清单解析；MSE 初始化；缓冲水位；追帧循环

```javascript
class HlsLite {
  constructor(video) { this.video = video; this.state = 'idle'; }
  async load(url) {
    const master = await fetchText(url);
    const list = parseHLS(master);                   // 342
    const level = list[0] ?? list;
    this.levelUrl = level.url ?? url;
    await this.initMSE();
    this.loop();
  }
  async initMSE() {
    this.ms = new MediaSource();
    this.video.src = URL.createObjectURL(this.ms);
    await new Promise(r => this.ms.addEventListener('sourceopen', r, { once: true }));
    this.sb = this.ms.addSourceBuffer('video/mp2t');
    this.state = 'ready';
  }
  async loop() {
    const pl = await fetchText(this.levelUrl);
    const { segments } = parseHLS(pl);
    let idx = 0;
    while (idx < segments.length) {
      const buffered = this.sb.buffered.length
        ? this.sb.buffered.end(this.sb.buffered.length - 1) : 0;
      if (buffered - this.video.currentTime > 10) {   // 缓冲充足
        await sleep(500); continue;
      }
      const seg = await fetchBuf(segments[idx++].url);
      await this.append(seg);
    }
  }
  append(buf) {
    return new Promise(r => {
      this.sb.addEventListener('updateend', () => r(), { once: true });
      this.sb.appendBuffer(buf);
    });
  }
}
```
