---
title: [H5-189] 设计一个验证码组件（滑块/点选/canvas 图形）
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-189：设计一个验证码组件（滑块/点选/canvas 图形）
**答**：
- 三类组件：canvas 图形码（前端绘制干扰线/旋转字符）、滑块（采集拖动轨迹）、点选（采集点击坐标序列）——**共同原则：前端只采集与展示，判定在服务端**（缺口真值、轨迹特征都在服务端校验）。
- 图形码绘制：字符随机旋转/基线抖动/颜色 + 干扰线噪点对抗 OCR；答案由服务端生成下发。
- 滑块：pointermove 采样轨迹 `{x, t}` 序列上送，服务端判断是否人手特征（匀速直线 = 机器）；缺口位置是服务端下发的随机值。
- 安全口径：任何纯前端验证码都可被绕过，前端组件的价值是"采集高质量行为数据 + 用户体验"。

```html
<canvas id="cap" width="260" height="80"></canvas>
<div class="slider"><div class="handle" id="handle"></div></div>
<script>
// 1) 图形验证码（服务端生成答案，前端仅展示；这里演示绘制）
function drawCaptcha(text) {
  const c = document.getElementById('cap').getContext('2d');
  c.fillStyle = '#f1f5f9';
  c.fillRect(0, 0, 260, 80);
  for (let i = 0; i < text.length; i++) {
    c.save();
    c.translate(30 + i * 52, 40 + (Math.random() * 16 - 8));   // 基线抖动
    c.rotate((Math.random() - 0.5) * 0.6);                      // 随机旋转
    c.font = `${28 + Math.random() * 10}px serif`;
    c.fillStyle = `hsl(${Math.random() * 360},60%,35%)`;
    c.fillText(text[i], 0, 0);
    c.restore();
  }
  for (let i = 0; i < 5; i++) {                                 // 干扰线
    c.strokeStyle = 'rgba(0,0,0,.15)';
    c.beginPath();
    c.moveTo(Math.random() * 260, Math.random() * 80);
    c.lineTo(Math.random() * 260, Math.random() * 80);
    c.stroke();
  }
}
drawCaptcha('K7QX');   // 真实答案在服务端，这里只演示展示层

// 2) 滑块：pointermove 采样轨迹，判定在服务端
const handle = document.getElementById('handle');
let dragging = false, start = 0;
const track = [];
handle.addEventListener('pointerdown', (e) => {
  dragging = true; start = e.clientX;
  handle.setPointerCapture(e.pointerId);
});
handle.addEventListener('pointermove', (e) => {
  if (!dragging) return;
  handle.style.transform = `translateX(${e.clientX - start}px)`;
  track.push({ x: e.clientX - start, t: performance.now() });   // 轨迹采样
});
handle.addEventListener('pointerup', () => {
  dragging = false;
  // 上送：轨迹（速度曲线特征）、耗时、缺口位置 —— 真值与判定都在服务端
  fetch('/api/captcha/verify', {
    method: 'POST',
    body: JSON.stringify({ track, duration: performance.now() }),
  });
});
// 点选验证码：canvas 渲染图片 + 按顺序采集点击坐标 [{x,y},...] 上送
// 安全口径：任何纯前端验证码都可被绕过，前端只负责"采集与展示"
</script>
```
