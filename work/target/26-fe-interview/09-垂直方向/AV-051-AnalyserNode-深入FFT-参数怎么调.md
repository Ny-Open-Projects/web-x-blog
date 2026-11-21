---
title: [AV-051] AnalyserNode 深入：FFT 参数怎么调？波形图怎么画？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-051：AnalyserNode 深入：FFT 参数怎么调？波形图怎么画？
**答**：
- FFT 基础：fftSize 是窗口采样点数（32~32768，2 的幂），frequencyBinCount = fftSize/2；fftSize 越大频率分辨率越高、时间响应越慢。
- 频率轴映射：bin i 对应 i × sampleRate/fftSize Hz；人声频段（85~255Hz 基频）在前几个 bin，可视化常做对数频率轴。
- getFloatFrequencyData 返回 dB 值（负数），getByteFrequencyData 已映射到 0-255（min/maxDecibels 可调对比度）。
- 波形图：getByteTimeDomainData，128 为中线，逐点连线；频谱图：柱状/热度图。
- 两个 Analyser 可并行挂不同 fftSize：大窗口画精细频谱，小窗口做实时音量。

```javascript
// 对数频率轴频谱 + 波形双视图
class SpectrumView {
  constructor(analyser, canvas) {
    this.an = analyser; this.ctx2d = canvas.getContext('2d');
    this.freq = new Float32Array(analyser.frequencyBinCount);
    this.wave = new Uint8Array(analyser.fftSize);
  }
  draw() {
    const { width: w, height: h } = this.ctx2d.canvas;
    const sampleRate = this.an.context.sampleRate;
    this.an.getFloatFrequencyData(this.freq);
    this.an.getByteTimeDomainData(this.wave);
    this.ctx2d.clearRect(0, 0, w, h);

    // 频谱：对数频率轴（20Hz - 20kHz 分 64 段）
    const bands = 64;
    this.ctx2d.fillStyle = '#4a9eff';
    for (let b = 0; b < bands; b++) {
      const f0 = 20 * (1000) ** (b / bands);      // 对数取频带
      const i0 = Math.floor(f0 / (sampleRate / this.an.fftSize));
      const i1 = Math.max(i0 + 1, Math.floor((f0 * 1000 ** (1 / bands)) / (sampleRate / this.an.fftSize)));
      let peak = -100;
      for (let i = i0; i < Math.min(i1, this.freq.length); i++) peak = Math.max(peak, this.freq[i]);
      const barH = ((peak + 100) / 100) * (h / 2); // -100dB~0dB 映射
      this.ctx2d.fillRect((b / bands) * w, h / 2 - barH, w / bands - 1, barH);
    }
    // 波形：下半区
    this.ctx2d.beginPath();
    this.wave.forEach((v, i) => {
      const x = (i / this.wave.length) * w, y = h / 2 + (h / 4) * ((v - 128) / 128) + h / 4;
      i ? this.ctx2d.lineTo(x, y) : this.ctx2d.moveTo(x, y);
    });
    this.ctx2d.strokeStyle = '#ff6b6b'; this.ctx2d.stroke();
    requestAnimationFrame(() => this.draw());
  }
}
```
