---
title: [AV-037] 屏幕共享怎么实现？getDisplayMedia 有哪些实用选项？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-037：屏幕共享怎么实现？getDisplayMedia 有哪些实用选项？
**答**：
- 采集：`getDisplayMedia({ video, audio })`，用户在浏览器选择器中决定共享整屏/窗口/标签页；Chrome 还支持 `preferCurrentTab`、`selfBrowserSurface: 'exclude'` 防止共享自己。
- 推送：`sender.replaceTrack(screenTrack)` 无缝切换不重协商；停止共享触发 track 的 `ended` 事件要恢复摄像头。
- 音频：Chrome 支持标签页音频采集（system audio 仅 Windows），`audio: true` 可把演示视频声音一起共享。
- 帧率与清晰度权衡：PPT 场景 `frameRate: 5` 省带宽，视频播放场景 30fps；`contentHint: 'detail'/'motion'` 告诉编码器优化方向。
- 隐私提示：必须显著提示"正在共享屏幕"，并提供一键停止。

```javascript
// 屏幕共享完整管理器
class ScreenShare {
  constructor(pc) { this.pc = pc; this.videoSender = pc.getSenders().find((s) => s.track?.kind === 'video'); }
  async start() {
    this.screenStream = await navigator.mediaDevices.getDisplayMedia({
      video: { frameRate: { ideal: 15 }, width: { ideal: 1920 }, contentHint: 'detail' },
      audio: true, // Chrome 标签页音频
      preferCurrentTab: false,
      selfBrowserSurface: 'exclude', // 不让自己出现在选择列表
      surfaceSwitching: 'include',   // 允许用户中途切换共享目标
    });
    const [track] = this.screenStream.getVideoTracks();
    track.contentHint = 'detail'; // 文档型内容
    await this.videoSender.replaceTrack(track);
    this.screenStream.getAudioTracks().forEach((a) => this.pc.addTrack(a, this.screenStream));
    track.addEventListener('ended', () => this.stop()); // 用户点浏览器停止按钮
    return this.screenStream;
  }
  async stop() {
    this.screenStream?.getTracks().forEach((t) => t.stop());
    const cam = await navigator.mediaDevices.getUserMedia({ video: true });
    await this.videoSender.replaceTrack(cam.getVideoTracks()[0]); // 切回摄像头
  }
}
```
