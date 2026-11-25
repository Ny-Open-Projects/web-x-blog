---
title: [SCN-1191] SCADA 大屏的与视频监控联锁（故障时自动调画面）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1191：SCADA 大屏的与视频监控联锁（故障时自动调画面）

**答**：
- 联动：设备故障自动调取对应摄像头画面（弹窗/分屏切换）。
- 录像：报警前后录像自动标记（取证）。
- 布局：视频窗口与工艺图共存（画中画）。

```javascript
// 视频联锁
function cameraInterlock(alarm, cameras) {
  const cam = cameras.find(c => c.spaceId === alarm.spaceId);
  if (!cam) return { note: '无对应摄像头' };
  return {
    live: popupStream(cam.id),                         // 弹窗实时画面
    clip: markClip(cam.id, alarm.at - 60_000, alarm.at + 300_000),   // 录像标记
    pip: true,
  };
}
function popupStream(id) { return 'live'; }
function markClip(id, a, b) { return true; }
```
