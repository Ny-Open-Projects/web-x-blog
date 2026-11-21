---
title: [H5-219] getUserMedia 的约束怎么写：分辨率/前后摄
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 音视频]
type: 面试题
---

## H5-219：getUserMedia 的约束怎么写：分辨率/前后摄

**答**：
- constraints 三种严格度：ideal（期望值，尽量满足）、exact（必须满足否则报错）、min/max（范围）
- 前后摄切换：`facingMode: 'user' | 'environment'`；移动端务必配 ideal 而不是 exact，部分设备不支持会直接失败
- 分辨率：`width: { ideal: 1280 }`——exact 写死 1080p 在低端机会 OverconstrainedError
- 枚举设备：先授权再用 `enumerateDevices()` 列出具体摄像头/麦克风，做设备选择器
- 权限状态查询：`navigator.permissions.query({ name: 'camera' })` 判断是否已授权，避免重复弹窗

```javascript
const stream = await navigator.mediaDevices.getUserMedia({
  video: { width: { ideal: 1280 }, height: { ideal: 720 }, facingMode: 'user' },
  audio: { echoCancellation: true, noiseSuppression: true },
});
document.querySelector('video').srcObject = stream;
// 切换后摄
function flip() {
  stream.getTracks().forEach(t => t.stop());
  navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } });
}
```
