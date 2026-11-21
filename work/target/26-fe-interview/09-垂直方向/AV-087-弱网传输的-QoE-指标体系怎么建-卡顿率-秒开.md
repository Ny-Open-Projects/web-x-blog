---
title: [AV-087] 弱网传输的 QoE 指标体系怎么建？（卡顿率/秒开率/延迟）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-087：弱网传输的 QoE 指标体系怎么建？（卡顿率/秒开率/延迟）
**答**：
- 核心指标五件套：首帧时间（秒开率 = 首帧 <1s 的会话占比）、卡顿率（stall 次数/分钟 或 stall 时长占比）、延迟（直播端到端延迟分布）、清晰度（实际播放档位分布）、错误率（播放失败/建连失败）。
- 维度切分：网络类型（WiFi/4G/5G）、地区与运营商、CDN 厂商、机型档位、协议类型，任何指标不看维度都是误导。
- 采集实现：播放器生命周期事件打点（loadstart/first-frame/stall/error）+ getStats 周期采样 + beacons 上报（unload 前 sendBeacon 防丢）。
- 指标联动分析：秒开率降 → 查 CDN 首包与预加载命中率；卡顿率升 → 查分片下载耗时分布与 buffer 水位。
- 目标基线参考：秒开率 >85%、卡顿率 <1 次/分钟、直播延迟 FLV <3s、建连成功率 >99%。

```javascript
// QoE 指标采集 SDK（播放器侧）
class QoeTracker {
  constructor(video, meta) {
    this.meta = meta; // { cdn, region, protocol, netType, device }
    this.metrics = { firstFrameMs: 0, stalls: 0, stallMs: 0, errors: 0, bytes: 0 };
    let t0 = 0;
    video.addEventListener('loadstart', () => (t0 = performance.now()));
    if (video.requestVideoFrameCallback) {
      video.requestVideoFrameCallback(() => { this.metrics.firstFrameMs = performance.now() - t0; });
    }
    video.addEventListener('waiting', () => (this.stallT = performance.now()));
    video.addEventListener('playing', () => {
      if (this.stallT) { this.metrics.stalls++; this.metrics.stallMs += performance.now() - this.stallT; this.stallT = 0; }
    });
    video.addEventListener('error', () => this.metrics.errors++);
    window.addEventListener('pagehide', () => this.flush(), { once: true }); // 离开前必报
  }
  flush() {
    navigator.sendBeacon('/api/qoe', JSON.stringify({
      ...this.meta, ...this.metrics,
      stallRate: this.metrics.stallMs / Math.max(1, playSec) * 100,
    }));
  }
}
```
