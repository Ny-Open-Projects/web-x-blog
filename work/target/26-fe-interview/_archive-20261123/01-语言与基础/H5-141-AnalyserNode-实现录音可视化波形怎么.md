---
title: [H5-141] AnalyserNode 实现录音可视化波形怎么做？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-141：AnalyserNode 实现录音可视化波形怎么做？
**答**：
- 链路：`getUserMedia` → `AudioContext` → `createAnalyser(fftSize)` → `createMediaStreamSource.connect(analyser)`；`fftSize` 决定时域数据点数。
- 每帧 rAF 里 `getByteTimeDomainData` 画波形（128 是静音中线），或 `getByteFrequencyData` 画频谱柱状图。
- `AudioContext` 必须在用户手势内 `resume()`，否则 iOS 上静默无输出。
- 停止时三步都要做：断开源节点、`track.stop()` 释放麦克风（指示灯熄灭）、`close()` AudioContext。

```html
<canvas id="wave" width="400" height="100"></canvas>
<button id="start">开始录音可视化</button>
<script>
document.getElementById('start').onclick = async function () {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  const actx = new AudioContext();
  await actx.resume();                       // 必须在用户手势内 resume
  const analyser = actx.createAnalyser();
  analyser.fftSize = 2048;                   // 时域数据点数 = fftSize
  actx.createMediaStreamSource(stream).connect(analyser);

  const data = new Uint8Array(analyser.fftSize);
  const canvas = document.getElementById('wave');
  const ctx = canvas.getContext('2d');

  function draw() {
    analyser.getByteTimeDomainData(data);    // 波形；getByteFrequencyData 是频谱
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = '#34d399';
    ctx.beginPath();
    const step = canvas.width / data.length;
    for (let i = 0; i < data.length; i++) {
      const y = (data[i] / 255) * canvas.height;   // 128 是静音中线
      i === 0 ? ctx.moveTo(0, y) : ctx.lineTo(i * step, y);
    }
    ctx.stroke();
    if (stream.getAudioTracks()[0].readyState === 'live') requestAnimationFrame(draw);
  }
  draw();

  // 停止三件套：断源 + stop tracks + close context
  this.onclick = () => {
    stream.getTracks().forEach((t) => t.stop());   // 麦克风指示灯熄灭
    actx.close();
  };
};
</script>
```
