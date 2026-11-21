---
title: [AV-180] 回声问题深挖：为什么开了 AEC 还有回声？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-180：回声问题深挖：为什么开了 AEC 还有回声？（高频）
**答**：
- AEC 原理：以"远端播放信号"为参考，自适应滤波抵消扬声器→麦克风的声学路径；参考信号缺失或失真，AEC 必失效。
- 原因一：用 Web Audio 图重路由（createMediaStreamSource→Destination）产出的新流绕过了浏览器 AEC——RTC 推流必须用原始 track。
- 原因二：外放音量过大产生非线性失真，超出滤波器建模能力；声学路径突变（挪设备/戴摘耳机）后需要重新收敛。
- 原因三：多方会议中有端未静音互为回声源；还有系统混音回录类软件引起。
- 排查顺序：确认 echoCancellation 生效 → 排查 Web Audio 绕行 → 单人外放复测 → 换耳机定位（戴耳机无声即确认声学回声）。

```javascript
// 回声排查与规避：确认 AEC 生效 + 不绕过浏览器处理
async function echoSafePublish() {
  // 正确：直接用 getUserMedia 的 track，浏览器 AEC/ANS 在 track 内部生效
  const stream = await navigator.mediaDevices.getUserMedia({
    audio: { echoCancellation: true, noiseSuppression: true, autoGainControl: true },
  });
  // 错误示范: new AudioContext() → createMediaStreamSource(stream) → destination
  // 产出的新 stream 已脱离 AEC 参考链 连麦必回声
  // 若确需 Web Audio 处理（如电音），保留原 track 给 RTC，处理流只用于本地监听
  const usesAec = stream.getAudioTracks()[0].getSettings().echoCancellation;
  if (!usesAec) report({ level: 'warn', msg: 'AEC 未生效 检查约束与设备' });
  return stream;
}
```
