---
title: [AV-004] 音频三要素采样率、位深、声道是什么？CD 音质一秒多少数据？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-004：音频三要素采样率、位深、声道是什么？CD 音质一秒多少数据？
**答**：
- 采样率：每秒采样次数，奈奎斯特定理要求 ≥ 信号最高频率的 2 倍；人耳上限 20kHz，故 44.1kHz/48kHz 覆盖全频段。
- 位深（bit depth）：每个采样点的量化精度，16bit 是 CD 标准，8bit 有明显噪声；WebRTC 内部常用 16bit PCM。
- 声道数：mono/stereo，数据量线性乘以声道数。
- 未压缩码率 = 采样率 × 位深 × 声道数，CD 音质 44100×16×2 ≈ 1.41 Mbps。
- 语音场景 16kHz 采样 + 单声道已够用（ASR、WebRTC 语音优先模式），这是降级省带宽的依据。

```javascript
// 音频原始码率与体积计算器
function audioBitrate({ sampleRate, bitDepth, channels }) {
  const bps = sampleRate * bitDepth * channels;
  return {
    bps,
    kbps: +(bps / 1000).toFixed(1),
    mbPerMin: +((bps / 8 / 1024 / 1024) * 60).toFixed(2),
  };
}
// CD 音质
console.log(audioBitrate({ sampleRate: 44100, bitDepth: 16, channels: 2 })); // ~1411kbps, ~10MB/min
// WebRTC 语音优先模式
console.log(audioBitrate({ sampleRate: 16000, bitDepth: 16, channels: 1 })); // ~256kbps 原始，Opus 压后 16~32kbps

// 用 Web Audio 采集时声明约束
const constraints = {
  audio: {
    sampleRate: { ideal: 48000 },
    channelCount: { ideal: 1 },
    echoCancellation: true,
    noiseSuppression: true,
  },
};
navigator.mediaDevices.getUserMedia(constraints).then((stream) => {
  console.log('实际采样率以 track 设置为准:', stream.getAudioTracks()[0].getSettings());
});
```
