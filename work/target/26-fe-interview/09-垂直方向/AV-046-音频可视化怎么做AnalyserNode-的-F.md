---
title: [AV-046] 音频可视化怎么做？AnalyserNode 的 FFT 怎么用？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-046：音频可视化怎么做？AnalyserNode 的 FFT 怎么用？
**答**：
- 链路：MediaStreamAudioSourceNode → AnalyserNode → （不连 destination，只"旁听"）；video 元素音频用 `createMediaElementSource`。
- `getByteFrequencyData`（频谱柱状图）与 `getByteTimeDomainData`（波形图）；`fftSize` 决定频率分辨率（bins = fftSize/2）。
- 渲染用 requestAnimationFrame，柱高 = freqData[i]/255 * 高度；smoothingTimeConstant 平滑动画。
- 麦克风音量检测（说话人高亮）：时域数据求 RMS，超阈值即"正在说话"。
- 注意：createMediaElementSource 后音频会改走 Web Audio 图，必须连回 destination 否则没声音（经典坑）。

```javascript
// 麦克风频谱可视化 + 说话检测
class AudioVisualizer {
  constructor(stream, canvas) {
    this.ctx2d = canvas.getContext('2d');
    const ac = new AudioContext();
    this.analyser = ac.createAnalyser();
    this.analyser.fftSize = 256;
    this.analyser.smoothingTimeConstant = 0.8;
    ac.createMediaStreamSource(stream).connect(this.analyser); // 旁听，不连 destination
    this.freq = new Uint8Array(this.analyser.frequencyBinCount);
    this.time = new Uint8Array(this.analyser.fftSize);
  }
  draw() {
    const { width: w, height: h } = this.ctx2d.canvas;
    this.analyser.getByteFrequencyData(this.freq);
    this.ctx2d.clearRect(0, 0, w, h);
    const barW = w / this.freq.length;
    this.freq.forEach((v, i) => {
      const barH = (v / 255) * h;
      this.ctx2d.fillStyle = `rgb(${v},120,255)`;
      this.ctx2d.fillRect(i * barW, h - barH, barW - 1, barH);
    });
    // 说话检测：时域 RMS
    this.analyser.getByteTimeDomainData(this.time);
    const rms = Math.sqrt(
      this.time.reduce((s, x) => s + ((x - 128) / 128) ** 2, 0) / this.time.length);
    if (rms > 0.06) this.onSpeaking?.(rms);
    requestAnimationFrame(() => this.draw());
  }
}
```
