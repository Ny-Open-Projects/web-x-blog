---
title: [AV-212] WebRTC 弱网体验降级：视频关闭与音频优先
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-212：WebRTC 弱网体验降级：视频关闭与音频优先

**答**：
- 弱网降级阶梯：高码率 → 降分辨率 → 降帧率 → 关视频留音频 → 提示重连。音频优先（带宽 30kbps 即可通话）。
- 实现：sender.setParameters 动态降 maxBitrate/framerate；track.enabled = false 关视频（不再发流）。
- 恢复阶梯：带宽恢复反向逐级升——防抖（连续 5 秒好网络才升级）。

```javascript
class NetworkDegrader {
  constructor(sender, levels) {
    this.sender = sender; this.levels = levels; this.idx = 0;
    this.stableCount = 0;
  }
  onStats(stats) {
    const rtt = stats.roundTripTime, loss = stats.packetsLost;
    const bad = rtt > 0.25 || loss > 0.05;
    if (bad) { this.downgrade(); this.stableCount = 0; }
    else if (++this.stableCount > 5) this.upgrade();       // 连续 5 秒好才升级
  }
  async downgrade() {
    if (this.idx >= this.levels.length - 1) return;
    const next = this.levels[++this.idx];
    if (next.videoOff) this.track.enabled = false;          // 关视频
    else {
      const p = this.sender.getParameters();
      p.encodings[0].maxBitrate = next.bitrate;
      p.encodings[0].scaleResolutionDownBy = next.scale;
      await this.sender.setParameters(p);
    }
  }
}
```
