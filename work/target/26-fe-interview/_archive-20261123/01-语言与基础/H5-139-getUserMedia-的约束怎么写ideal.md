---
title: [H5-139] getUserMedia 的约束怎么写？ideal 与 exact 有什么区别？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-139：getUserMedia 的约束怎么写？ideal 与 exact 有什么区别？
**答**：
- 约束分三档：`ideal`（尽量满足，取最近支持值）、`min/max`（硬边界）、`exact`（必须满足，否则抛 `OverconstrainedError`）。
- 常用字段：`width/height/frameRate`、`facingMode`（'user'/'environment' 前后摄）、音频的 `echoCancellation/noiseSuppression`。
- 运行时调整用 `track.applyConstraints()`（软约束热生效），`track.getSettings()` 查真实生效参数。
- 错误要分类处理：`NotAllowedError` 权限拒绝、`NotFoundError` 无设备、`OverconstrainedError` 约束冲突——给用户的提示完全不同。
- 移动端切换前后摄：必须先 `stop` 旧 track 再重新 `getUserMedia`，摄像头无法被两个流同时占用。

```html
<video id="cam" autoplay playsinline muted></video>
<button id="switch">切换前后摄像头</button>
<script>
let stream, facing = 'user';

async function open(mode = 'user') {
  // ideal：尽量满足；exact：必须满足否则 OverconstrainedError；min/max：硬边界
  const constraints = {
    video: {
      width: { ideal: 1280 },
      height: { ideal: 720 },
      frameRate: { ideal: 30, min: 15 },     // min 是硬底线
      facingMode: mode,                      // 'user' | 'environment'
    },
    audio: { echoCancellation: true, noiseSuppression: true },
  };
  try {
    stream = await navigator.mediaDevices.getUserMedia(constraints);
  } catch (e) {
    // NotAllowedError 权限拒绝 / NotFoundError 无设备 / OverconstrainedError 约束冲突
    if (e.name === 'NotAllowedError') alert('请在浏览器设置中授权摄像头');
    else if (e.name === 'NotFoundError') alert('未检测到摄像头');
    else throw e;
  }
  document.getElementById('cam').srcObject = stream;
}

// 运行时热调整（不重开设备）：applyConstraints 软约束
async function upgrade() {
  const track = stream.getVideoTracks()[0];
  await track.applyConstraints({ width: { ideal: 1920 } });
  console.log('实际生效参数', track.getSettings());   // 真实能力
}

// 切换前后摄：旧 track 必须 stop，移动端无法同时占用
document.getElementById('switch').onclick = async () => {
  stream?.getTracks().forEach((t) => t.stop());
  facing = facing === 'user' ? 'environment' : 'user';
  await open(facing);
};
open();
</script>
```
