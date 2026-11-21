---
title: [AV-078] 请设计一个亚秒延迟互动直播（Half-Second 方案概览）。
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-078：请设计一个亚秒延迟互动直播（Half-Second 方案概览）。
**答**：
- 目标：观众端延迟 <800ms 且保留弹幕/投票互动，成本介于 RTC 与 CDN 之间。
- 路线一（主流）：RTC 网做"一对多扇出"——主播推 RTMP/WebRTC 进 RTC 服务，服务端用 WebRTC 向观众直推（SFU 大扇出 + 级联），延迟 500ms~1s。
- 路线二：CDN 侧 WebRTC 化（厂商提供 WHEP 拉流 + 边缘 SFU），观众走 HTTP 信令就近接入。
- 播放端要点：禁大 buffer（jitter buffer 50~150ms）、关 ABR 改 simulcast 选层、延迟超标追帧（0.95/1.1 倍速微调）。
- 互动同步：互动事件（投票/红包）带服务器时间戳，观众端按时间戳对齐展示，避免与画面错位。

```javascript
// 亚秒直播观众端：WHEP 拉流 + 低延迟参数
class HalfSecondViewer {
  async play(whepUrl) {
    this.pc = new RTCPeerConnection({
      iceServers: ICE_CONF,
      // RTCRtpReceiver 抖动缓冲在浏览器内部，能控的是播放侧
    });
    this.pc.addTransceiver('video', { direction: 'recvonly' });
    this.pc.addTransceiver('audio', { direction: 'recvonly' });
    this.pc.ontrack = (e) => (this.video.srcObject = e.streams[0]);
    const offer = await this.pc.createOffer();
    await this.pc.setLocalDescription(offer);
    const res = await fetch(whepUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/sdp' },
      body: this.pc.localDescription.sdp,
    });
    await this.pc.setRemoteDescription({ type: 'answer', sdp: await res.text() });
    this.keepLowLatency();
  }
  keepLowLatency() { // 延迟测量与追帧
    setInterval(() => {
      const b = this.video.buffered;
      if (!b.length) return;
      const latency = b.end(b.length - 1) - this.video.currentTime;
      if (latency > 1.0) this.video.playbackRate = 1.1;       // 加速追
      else if (latency < 0.3) this.video.playbackRate = 0.95; // 防追过头
      else this.video.playbackRate = 1;
    }, 1000);
  }
}
```
