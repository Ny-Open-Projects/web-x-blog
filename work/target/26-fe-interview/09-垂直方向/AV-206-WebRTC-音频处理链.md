---
title: [AV-206] WebRTC 音频处理链：AEC/NS/AGC 三件套
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-206：WebRTC 音频处理链：AEC/NS/AGC 三件套

**答**：
- 浏览器内置音频处理：回声消除（AEC）、噪声抑制（NS）、自动增益（AGC）——getUserMedia constraints 控制。
- 回声消除原理：参考信号（播放的远端音频）+ 麦克风信号自适应滤波抵消回声——外放场景必开。
- 约束失效场景：蓝牙耳机（AEC 参考延迟漂移）→ 回声明显，提示用耳机。

```javascript
const stream = await navigator.mediaDevices.getUserMedia({
  audio: {
    echoCancellation: true,                              // AEC 回声消除
    noiseSuppression: true,                              // NS 噪声抑制
    autoGainControl: true,                               // AGC 自动增益
    channelCount: 1,                                     // 会议场景单声道
    sampleRate: 48000,
  },
});
// 检测实际生效值（浏览器可能降级）：
const track = stream.getAudioTracks()[0];
const settings = track.getSettings();                     // 实际生效的约束
if (!settings.echoCancellation) warn('设备不支持回声消除，请佩戴耳机');
// 蓝牙 HFP 协议音质差（麦克风 16kHz）——高保真场景提示切换 A2DP（但不能采集）
```
