---
title: [XP-330] 跨端 WebRTC 连麦的移动端专项
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-330：跨端 WebRTC 连麦的移动端专项

**答**：
- 专项：前后台切换（视频冻结/恢复）、听筒扬声器切换、来电中断处理（释放/恢复）。
- 性能：硬编硬解（移动端必开）、分辨率按网络自适应（356）。
- 度量：连麦卡顿率/首帧/中断恢复时长。

```javascript
// 连麦生命周期
class CallSession {
  onAppStateChange(active) {
    if (!active) { this.pc.getSenders().forEach(s => s.track?.enabled = false);
      report({ type: 'call-background' }); }
    else { this.pc.getSenders().forEach(s => s.track?.enabled = true);
      this.renegotiate(); }                          // 恢复重协商
  }
  onAudioInterrupt(type) {                            // 来电/闹钟
    if (type === 'began') this.pc.close();           // 释放
    if (type === 'ended') this.rebuild();             // 重建会话
  }
}
```
