---
title: [AV-222] WebRTC 大规模直播：SFU 级联与边缘节点
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-222：WebRTC 大规模直播：SFU 级联与边缘节点

**答**：
- 万人直播：单 SFU 扇出上限（约 500 观众）→ 级联（源 SFU → 边缘 SFU 树）；观众就近接入边缘节点。
- 前端关注：接入节点选择（HTTPDNS/地域调度）、断流重连到备用边缘、CDN 混合（HLS 大规模 + WebRTC 低延迟分层）。
- 延迟分层：WebRTC 300ms（互动观众）+ HLS 10s（海量观众）——同内容双协议输出。

```javascript
class LiveViewer {
  async join(streamId) {
    const edge = await pickEdgeNode(streamId);               // 就近边缘节点
    try {
      await this.connectWebRTC(edge, streamId);              // 低延迟 WebRTC
      this.latency = '300ms';
    } catch {
      await this.connectHLS(streamId);                        // 降级 HLS
      this.latency = '10s';
    }
    this.monitorStall();                                     // 卡顿监控
  }
  async reconnect() {                                        // 断流重连：备用边缘
    const backup = await pickEdgeNode(this.streamId, { exclude: this.currentEdge });
    await this.connectWebRTC(backup, this.streamId);
  }
}
// 分层架构：推流端 → 源 SFU → 边缘 SFU 树（WebRTC 互动层）+ RTMP → CDN（HLS 大规模层）
```
