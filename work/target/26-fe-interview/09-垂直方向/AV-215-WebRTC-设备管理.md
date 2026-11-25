---
title: [AV-215] WebRTC 设备管理：设备热插拔与切换
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 笔试题, 26]
type: 笔试题
---

## AV-215：WebRTC 设备管理：设备热插拔与切换

**答**：
- 题目：实现摄像头/麦克风热插拔处理——设备变更事件监听、无设备降级提示、设备切换（换 track 不重协商）。
- 思路：navigator.mediaDevices.ondevicechange 监听；enumerateDevices 枚举；切换 = getUserMedia 新 track → sender.replaceTrack（免重协商）；无设备 → 只听模式。
- 评分点：replaceTrack 免重协商；devicechange 处理；无设备降级。

```javascript
class DeviceManager {
  constructor(pc) { this.pc = pc; this.listen(); }
  listen() {
    navigator.mediaDevices.ondevicechange = async () => {
      const devices = await navigator.mediaDevices.enumerateDevices();
      const cams = devices.filter(d => d.kind === 'videoinput');
      if (!cams.length) this.onNoCamera?.();               // 无摄像头：只听模式
      else if (cams[0].deviceId !== this.currentCamId) this.switchCamera(cams[0].deviceId);
    };
  }
  async switchCamera(deviceId) {                            // 切换：replaceTrack 免重协商
    const stream = await navigator.mediaDevices.getUserMedia({
      video: { deviceId: { exact: deviceId } } });
    const newTrack = stream.getVideoTracks()[0];
    const sender = this.pc.getSenders().find(s => s.track?.kind === 'video');
    await sender.replaceTrack(newTrack);                    // 不触发重新协商
    this.currentCamId = deviceId;
  }
}
```
