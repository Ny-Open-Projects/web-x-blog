---
title: [AV-241] WebAudio 混音：多路音频合成与音量控制
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 笔试题, 26]
type: 笔试题
---

## AV-241：WebAudio 混音：多路音频合成与音量控制

**答**：
- 题目：WebRTC 多人会议客户端混音（本地录制场景：把 N 路远端音频 + 本地混成一路）——AudioContext 接线 + 每路增益控制。
- 思路：每路 MediaStream → MediaStreamSource → GainNode（音量）→ DestinationNode（合并）；录制用 MediaStreamDestination。
- 评分点：接线图正确；GainNode 音量控制；录制输出流获取。

```javascript
class AudioMixer {
  constructor() {
    this.ctx = new AudioContext();
    this.destination = this.ctx.createMediaStreamDestination();
    this.gains = new Map();
  }
  addStream(stream, peerId, volume = 1) {                   // 接入一路
    const source = this.ctx.createMediaStreamSource(stream);
    const gain = this.ctx.createGain();
    gain.gain.value = volume;
    source.connect(gain).connect(this.destination);          // 源→增益→合并
    this.gains.set(peerId, gain);
    return () => { source.disconnect(); gain.disconnect(); this.gains.delete(peerId); };   // 拆除函数
  }
  setVolume(peerId, v) { this.gains.get(peerId)?.gain.setTargetAtTime(v, this.ctx.currentTime, 0.05); }   // 平滑音量
  getMixedStream() { return this.destination.stream; }       // 混合流（供 MediaRecorder）
}
```
