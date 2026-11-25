---
title: [SCN-1132] IoT 设备控制台的视频监控接入（摄像头联动）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1132：IoT 设备控制台的视频监控接入（摄像头联动）

**答**：
- 联动：设备详情页关联附近摄像头（空间映射），告警时弹出实时画面。
- 协议：HLS/WebRTC 拉流（低延迟用 WebRTC），录像回放（时间轴对齐告警）。
- 权限：摄像头查看权限与设备权限独立。

```javascript
// 视频联动
function cameraLink(device, cameras) {
  const near = cameras.filter(c => c.spaceId === device.spaceId);
  return {
    live: near[0] ? webrtcPull(near[0].id) : null,
    playback: (alarmTs) => hlsPlayback(near[0].id, alarmTs - 60_000),
    note: near.length ? null : '该空间无摄像头',
  };
}
function webrtcPull(id) { return 'stream'; }
function hlsPlayback(id, from) { return 'hls'; }
```
