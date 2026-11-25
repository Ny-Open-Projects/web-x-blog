---
title: [AV-220] WebRTC 音频可视化：音量条与频谱图
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 笔试题, 26]
type: 笔试题
---

## AV-220：WebRTC 音频可视化：音量条与频谱图

**答**：
- 题目：会议音频可视化——音量条（实时音量电平）与频谱图（AnalyserNode FFT）。完整实现。
- 思路：AudioContext + AnalyserNode（fftSize 256）；getByteTimeDomainData 算 RMS 音量；getByteFrequencyData 画频谱条。
- 评分点：AnalyserNode 接线；RMS 音量计算；频谱绘制性能。

```javascript
class AudioVisualizer {
  constructor(stream, canvas) {
    this.ctx = new AudioContext();
    this.analyser = this.ctx.createAnalyser();
    this.analyser.fftSize = 256;
    this.ctx.createMediaStreamSource(stream).connect(this.analyser);
    this.canvas = canvas; this.loop();
  }
  loop() {
    const data = new Uint8Array(this.analyser.fftSize);
    this.analyser.getByteTimeDomainData(data);
    let sum = 0;
    for (const v of data) sum += (v - 128) ** 2;
    const rms = Math.sqrt(sum / data.length) / 128;        // RMS 音量 0~1
    this.onVolume?.(rms);                                   // 音量条
    const freq = new Uint8Array(this.analyser.frequencyBinCount);
    this.analyser.getByteFrequencyData(freq);               // 频谱
    const c = this.canvas.getContext('2d');
    freq.forEach((v, i) => {
      c.fillStyle = `hsl(${i * 2}, 80%, 50%)`;
      c.fillRect(i * 4, this.canvas.height - v / 255 * this.canvas.height, 3, v / 255 * this.canvas.height);
    });
    requestAnimationFrame(() => this.loop());
  }
}
```
