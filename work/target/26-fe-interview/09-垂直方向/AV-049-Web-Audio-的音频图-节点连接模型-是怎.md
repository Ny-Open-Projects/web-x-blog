---
title: [AV-049] Web Audio 的音频图（节点连接模型）是怎样的？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-049：Web Audio 的音频图（节点连接模型）是怎样的？
**答**：
- 模型：一切皆 Node，`connect()` 组成有向无环图（允许 fan-out/fan-in）；源节点（oscillator/mediaStream/buffer）→ 处理节点（gain/filter/pannner/analyser）→ destination。
- 调度基于 audio clock：`start(when)`、`setValueAtTime` 等支持亚毫秒精确调度，且不受主线程卡顿影响（音频渲染线程独立）。
- 节点是幂等复用的：一个 GainNode 可接多个目标；断开用 `disconnect(target)` 精确断或全断。
- Channel 处理：`channelCount/channelCountMode/interpretation` 决定上下混音行为。
- 设计意义：复杂链路（混音+特效+可视化）就是搭积木，比裸 audio 元素强大一个量级。

```javascript
// 音频图示例：麦克风 → 降噪模拟 → 混响 → 增益 → 输出 + 旁路可视化
async function buildAudioGraph(stream) {
  const ctx = new AudioContext();
  const src = ctx.createMediaStreamSource(stream);
  const biquad = ctx.createBiquadFilter();     // 高通滤掉低频隆隆声
  biquad.type = 'highpass'; biquad.frequency.value = 120;
  const compressor = ctx.createDynamicsCompressor(); // 动态压缩防爆音
  const gain = ctx.createGain(); gain.gain.value = 0.8;
  const analyser = ctx.createAnalyser(); analyser.fftSize = 512;

  // 主链
  src.connect(biquad).connect(compressor).connect(gain).connect(ctx.destination);
  // 旁路（不发声只观测）：fan-out 的体现
  gain.connect(analyser);

  // 定时淡入淡出：AudioParam 精确调度
  const t = ctx.currentTime;
  gain.gain.setValueAtTime(0.001, t);
  gain.gain.exponentialRampToValueAtTime(0.8, t + 0.5);
  return { ctx, analyser, gain };
}
```
