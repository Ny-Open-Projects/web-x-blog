---
title: [H5-229] 音频可视化的频谱怎么画（AnalyserNode）
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 音视频]
type: 面试题
---

## H5-229：音频可视化的频谱怎么画（AnalyserNode）

**答**：
- 链路：audio/video → createMediaElementSource → AnalyserNode → destination；Analyser 挂在中间不改声音只旁路数据
- 两类数据：getByteFrequencyData（频谱，柱状图）与 getByteTimeDomainData（波形，示波器曲线）
- 参数理解：fftSize（默认 2048 → 1024 个频点）决定频率分辨率；smoothingTimeConstant 控制帧间平滑
- 渲染循环：rAF 里每帧取数据重画；与 audio 播放状态联动（暂停时衰减而非定格）
- 坑：一个媒体元素只能 createMediaElementSource 一次，重复创建没声音

```javascript
const ac = new AudioContext();
const src = ac.createMediaElementSource(audio); // 只能一次
const analyser = ac.createAnalyser();
analyser.fftSize = 256;
src.connect(analyser); analyser.connect(ac.destination);

const data = new Uint8Array(analyser.frequencyBinCount);
(function draw() {
  requestAnimationFrame(draw);
  analyser.getByteFrequencyData(data);
  ctx.clearRect(0, 0, w, h);
  [...data].forEach((v, i) => {
    ctx.fillRect(i * 6, h - (v / 255) * h, 4, (v / 255) * h);
  });
})();
```
