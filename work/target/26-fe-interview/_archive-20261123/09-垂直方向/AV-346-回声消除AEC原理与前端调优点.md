---
title: [AV-346] 回声消除（AEC）原理与前端调优点
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-346：回声消除（AEC）原理与前端调优点

**答**：
- 原理：自适应滤波器建模回声路径，从远端参考信号预测并抵消回声（WebRTC AEC3）。
- 前端问题：外放音量过大（回声强）、设备时钟漂移（滤波器失配）导致"残留回声"。
- 调优：getUserMedia 约束 echoCancellation/noiseSuppression/autoGainControl；连麦场景关软件 AEC 用系统级（避免二次处理劣化）。

```javascript
// 音频约束配置
function audioConstraints(scene) {
  if (scene === 'connect')                            // 连麦
    return { audio: { echoCancellation: false,       // 关 WebRTC AEC
      noiseSuppression: false,
      autoGainControl: false,
      channelCount: 1 }, note: '系统级 AEC 处理' };
  return { audio: { echoCancellation: true,
    noiseSuppression: true, autoGainControl: true } };
}
// 残留回声排查：外放 > 70% 音量时必现，提示戴耳机
```
