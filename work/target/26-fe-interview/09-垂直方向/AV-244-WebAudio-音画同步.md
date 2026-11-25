---
title: [AV-244] WebAudio 音画同步：背景音乐与直播流的混合播放
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-244：WebAudio 音画同步：背景音乐与直播流的混合播放

**答**：
- 场景：播放器内背景音乐与直播流共存（音量避让/切换）；或视频回放时 BGM 与人声分离控制。
- 实现：直播流 track → MediaStreamSource → GainNode；BGM → 另一 GainNode → 同一 destination；两路独立音量。
- 坑：AudioContext 采样率与流采样率不一致 → 自动重采样（浏览器处理）；AudioContext resume 手势要求。

```javascript
class AudioMixer2 {
  constructor() {
    this.ctx = new AudioContext();                           // 需手势 resume
    this.streamGain = this.ctx.createGain();                 // 直播流增益
    this.bgmGain = this.ctx.createGain();                    // BGM 增益
    this.master = this.ctx.createGain();                     // 总控
    this.streamGain.connect(this.master);
    this.bgmGain.connect(this.master);
    this.master.connect(this.ctx.destination);
  }
  attachStream(track) {                                      // 直播流接入
    const src = this.ctx.createMediaStreamSource(new MediaStream([track]));
    src.connect(this.streamGain);
  }
  playBGM(buffer, { loop = true, volume = 0.3 } = {}) {
    const src = this.ctx.createBufferSource();
    src.buffer = buffer; src.loop = loop;
    this.bgmGain.gain.value = volume;
    src.connect(this.bgmGain); src.start();
    return src;                                            // 停止 = src.stop()
  }
}
```
