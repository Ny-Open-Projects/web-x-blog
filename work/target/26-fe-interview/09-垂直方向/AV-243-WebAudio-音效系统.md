---
title: [AV-243] WebAudio 音效系统：礼物特效音与队列
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-243：WebAudio 音效系统：礼物特效音与队列

**答**：
- 礼物音效：多音效并发冲突（连发礼物）→ 音效队列（同类合并）+ 音量避让（音效压低背景 BGM ducking）。
- 实现：AudioBuffer 预加载（HW-AV-740 思想）；播放队列限并发；Ducking：礼物音效时 BGM gain 自动降 50%。
- 移动端：AudioContext 需手势激活（HW-740 联动）。

```javascript
class EffectSoundManager {
  constructor() { this.pool = new Map(); this.queue = []; this.bgmGain = null; }
  async preload(sounds) {                                   // 预加载解码
    for (const [name, url] of Object.entries(sounds)) {
      const buf = await fetch(url).then(r => r.arrayBuffer());
      this.pool.set(name, await ctx.decodeAudioData(buf));
    }
  }
  play(name, { duck = true } = {}) {
    if (duck && this.bgmGain) {                             // Ducking：BGM 避让
      this.bgmGain.gain.setTargetAtTime(0.3, ctx.currentTime, 0.05);
      setTimeout(() => this.bgmGain.gain.setTargetAtTime(1, ctx.currentTime, 0.3), 800);
    }
    const src = ctx.createBufferSource();
    src.buffer = this.pool.get(name);
    src.connect(ctx.destination);
    src.start();                                            // 同类连发：WebAudio 自动混音
  }
}
```
