---
title: [AV-040] 回声消除 AEC 与噪声抑制 ANS 是什么？前端要注意什么？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-040：回声消除 AEC 与噪声抑制 ANS 是什么？前端要注意什么？（高频）
**答**：
- 回声原理：扬声器播出的远端声音被麦克风再次采集传回，形成"我说话自己听到"；AEC 用参考信号自适应滤波抵消。
- ANS（噪声抑制）： stationary 噪声谱估计 + 谱减法/WebRTC NS 模块；AGC 自动增益统一音量。
- 浏览器已内建：`getUserMedia` 约束 `echoCancellation/noiseSuppression/autoGainControl`，Chrome 走 AEC3，质量足够。
- 前端陷阱：外放 + 不开 AEC 必炸麦；用 `getUserMedia` 拿到的是处理后的流，专业需求可关约束拿原始流自研处理。
- 排查口诀：戴耳机不回声、外放回声 → AEC 问题；双方同时听到"机器人声"→ 双端都开了 AEC 且参考信号接错。

```javascript
// 音频约束的分级配置：普通通话 vs 音乐直播
const PRESETS = {
  voice: { // 默认通话：全开浏览器 DSP
    echoCancellation: true, noiseSuppression: true, autoGainControl: true,
  },
  music: { // 音乐模式：关 DSP 保留原声（WebRTC 内 opus 也建议 stereo+低复杂度）
    echoCancellation: false, noiseSuppression: false, autoGainControl: false,
    channelCount: 2, sampleRate: 48000,
  },
};
async function getMic(preset = 'voice') {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: PRESETS[preset] });
  const settings = stream.getAudioTracks()[0].getSettings();
  console.log('生效的 DSP 设置', settings); // 验证约束是否被浏览器接受
  return stream;
}

// 检测回声风险：远端正在播放 + 本端外放 → 提示戴耳机
function echoRiskDetector(remoteVideo) {
  const ctx = new AudioContext();
  remoteVideo.addEventListener('play', () => {
    if (navigator.mediaDevices.getSupportedConstraints().echoCancellation && !remoteVideo.muted) {
      // 提示逻辑：外放播放远端音频且本端要开口说话时
      console.info('提示：请佩戴耳机以获得最佳连麦体验');
    }
  });
}
```

---

## 六、采集与处理（AV-041 ~ AV-047）
