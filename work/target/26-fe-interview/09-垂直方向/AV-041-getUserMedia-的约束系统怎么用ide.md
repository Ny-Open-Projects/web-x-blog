---
title: [AV-041] getUserMedia 的约束系统怎么用？ideal 和 exact 区别？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-041：getUserMedia 的约束系统怎么用？ideal 和 exact 区别？
**答**：
- 约束分理想值（ideal，尽量满足）与硬性值（exact，不满足直接失败 OverconstrainedError）；默认是 ideal。
- 常用维度：width/height/frameRate（可用 {min, max, ideal} 区间）、facingMode（user/environment，手机前后摄）、deviceId（exact 才能锁定设备）。
- `getSupportedConstraints()` 探测浏览器支持哪些约束键；`track.getSettings()` 查询实际生效值；`applyConstraints()` 运行时动态调整（热切换分辨率/帧率）。
- 采集性能经验：请求 720p/30fps 让浏览器选择最近能力，比 exact 1080p 成功率高得多。
- 顺序陷阱：`deviceId` 在用户授权前不可枚举，首帧授权流程要处理。

```javascript
// 约束实战：区间理想值 + 动态调整 + 失败降级
async function openCamera() {
  const base = {
    video: {
      width: { ideal: 1280 }, height: { ideal: 720 }, // 理想，浏览器就近选
      frameRate: { ideal: 30, max: 30 },
      facingMode: 'user',
    },
  };
  try {
    return await navigator.mediaDevices.getUserMedia(base);
  } catch (e) {
    if (e.name === 'OverconstrainedError') {
      console.warn('约束过紧', e.constraint, '，降级到宽松模式');
      return navigator.mediaDevices.getUserMedia({ video: true });
    }
    throw e;
  }
}

// 运行时动态降分辨率（不重开摄像头）
const [track] = (await openCamera()).getVideoTracks();
await track.applyConstraints({ width: { ideal: 640 }, frameRate: 15 });
console.log('实际生效', track.getSettings()); // width 可能仍是 1280，浏览器尽力

// 探测能力
console.log(navigator.mediaDevices.getSupportedConstraints());
// { width: true, height: true, frameRate: true, facingMode: true, ... }
```
