---
title: [AV-052] 音频录制与处理链（MediaStreamSource → Destination）怎么搭？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-052：音频录制与处理链（MediaStreamSource → Destination）怎么搭？
**答**：
- 录制带处理效果的音频：麦克风 → 处理链（EQ/压缩/降噪）→ MediaStreamDestination（把 Web Audio 图转回 MediaStream）→ MediaRecorder 录制。
- `MediaStreamAudioDestinationNode` 是关键桥梁：Web Audio 图的输出重新变回 MediaStream，可录制、可推流（WebRTC addTrack）。
- 直播场景推"处理后的声音"：PC.addTrack(destNode.stream.getAudioTracks()[0])，观众听到的是调过音的。
- 双路录制：原始流与处理流各录一份（后期重制用原始）。
- 时钟对齐：录制的分片时间戳以 AudioContext 时钟为准，与视频合并时按实际时长对齐。

```javascript
// 麦克风 → 处理链 → 重新变 MediaStream → 录制 + 推流
async function processedRecording() {
  const raw = await navigator.mediaDevices.getUserMedia({ audio: true });
  const ctx = new AudioContext();
  const src = ctx.createMediaStreamSource(raw);

  const hp = ctx.createBiquadFilter(); hp.type = 'highpass'; hp.frequency.value = 100;
  const eq = ctx.createBiquadFilter(); eq.type = 'peaking'; eq.frequency.value = 3000; eq.gain.value = 3; // 提亮人声
  const comp = ctx.createDynamicsCompressor();

  const dest = ctx.createMediaStreamDestination(); // Web Audio → MediaStream 桥
  src.connect(hp).connect(eq).connect(comp).connect(dest);

  // 1. 录制处理后的声音
  const rec = new MediaRecorder(dest.stream, { mimeType: 'audio/webm;codecs=opus' });
  const chunks = [];
  rec.ondataavailable = (e) => chunks.push(e.data);
  rec.start();
  setTimeout(() => rec.stop(), 10000);

  // 2. 同时把处理后的流推给 WebRTC
  pc.addTrack(dest.stream.getAudioTracks()[0], dest.stream);
  return { stop: () => { rec.stop(); raw.getTracks().forEach((t) => t.stop()); ctx.close(); } };
}
```
