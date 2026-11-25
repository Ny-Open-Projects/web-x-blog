---
title: [AV-367] WebAudio 与 WebRTC 的集成（音效/混音）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-367：WebAudio 与 WebRTC 的集成（音效/混音）

**答**：
- 链路：getUserMedia -> WebAudio 处理链（混音/音效/Ducking）-> MediaStreamDestination -> WebRTC 发送。
- 用途：连麦混音（背景音乐+人声）、礼物音效 ducking（音量闪避）、AI 变声。
- 延迟：WebAudio 处理增加 20~40ms——实时场景注意预算。

```javascript
// WebAudio 混音发送
async function mixedSend(micStream, musicUrl) {
  const ctx = new AudioContext();
  const dest = ctx.createMediaStreamDestination();
  const mic = ctx.createMediaStreamSource(micStream);
  mic.connect(dest);
  const music = ctx.createBufferSource();
  music.buffer = await fetchDecode(musicUrl, ctx);
  const gain = ctx.createGain(); gain.gain.value = 0.3;
  music.connect(gain).connect(dest);
  music.start();
  return dest.stream;                                  // 给 RTCPeerConnection
}
async function fetchDecode(url, ctx) {
  return ctx.decodeAudioData(await (await fetch(url)).arrayBuffer());
}
```
