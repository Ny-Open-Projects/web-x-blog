---
title: [SCN-156] 聊天 App 的 H5 版要发语音消息：录音、实时波形、时长限制，如何实现？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-156：聊天 App 的 H5 版要发语音消息：录音、实时波形、时长限制，如何实现？
**答**：
- 录音用 `MediaRecorder`（浏览器原生，输出 webm/ogg），按住说话模式：touchstart 开始、touchend 停止，上滑取消要区分"取消区"和"发送区"。
- 波形不靠猜：接 `AnalyserNode`（Web Audio）每帧取时域数据算振幅，采样存成数组，发送时随音频一起上传，播放端按数据画静态波形，播放进度染色的体验一致。
- 时长限制双保险：录到 60s 自动停；MediaRecorder 的 timeslice 分片输出，方便边录边显示已录时长。
- 权限与降级：麦克风授权被拒给引导；`MediaRecorder` 不可用的老设备降级提示改用文字。

```javascript
// 语音消息：MediaRecorder + AnalyserNode 波形采样
export class VoiceRecorder {
  constructor({ maxDuration = 60_000 } = {}) { this.maxDuration = maxDuration; }

  async start() {
    this.stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const ctx = new AudioContext();
    const source = ctx.createMediaStreamSource(this.stream);
    this.analyser = ctx.createAnalyser();
    this.analyser.fftSize = 256;
    source.connect(this.analyser);

    this.recorder = new MediaRecorder(this.stream);
    this.chunks = [];
    this.recorder.ondataavailable = e => this.chunks.push(e.data);
    this.recorder.start(500);                          // timeslice：500ms 一片，可边录边计时

    this.samples = [];                                 // 振幅采样，随消息上传
    this.tick = requestAnimationFrame(this.sampleAmplitude);
    this.autoStop = setTimeout(() => this.stop(), this.maxDuration); // 60s 自动停
  }

  sampleAmplitude = () => {
    const data = new Uint8Array(this.analyser.frequencyBinCount);
    this.analyser.getByteTimeDomainData(data);
    let peak = 0;
    for (const v of data) peak = Math.max(peak, Math.abs(v - 128));
    this.samples.push(Math.round(peak / 128 * 100));   // 0~100 振幅
    renderWaveform(this.samples, { live: true });      // 实时波形
    this.tick = requestAnimationFrame(this.sampleAmplitude);
  };

  async stop() {
    clearTimeout(this.autoStop); cancelAnimationFrame(this.tick);
    const blob = await new Promise(r => { this.recorder.onstop = () => r(new Blob(this.chunks)); this.recorder.stop(); });
    this.stream.getTracks().forEach(t => t.stop());
    const duration = this.chunks.length ? estimateDuration(blob) : 0;
    if (duration < 1000) throw new Error('TOO_SHORT');  // 1 秒内视为误触
    return { blob, duration, samples: this.samples };   // samples 上传后供播放端画静态波形
  }
}

// 播放端：静态波形按进度染色
export function renderWaveform(samples, { progress = 0, live = false } = {}) {
  const bars = samples.map((v, i) => {
    const played = live || i / samples.length <= progress;
    return `<i style="height:${Math.max(4, v * 0.4)}px" class="${played ? 'on' : ''}"></i>`;
  });
  waveEl.innerHTML = bars.join('');
}
```
