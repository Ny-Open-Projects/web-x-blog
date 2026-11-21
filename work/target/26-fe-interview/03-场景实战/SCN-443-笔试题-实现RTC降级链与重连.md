---
title: [SCN-443] 笔试题——实现会议弱网降级链（分辨率→帧率→音频优先+重连）？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-443：手写弱网降级链：质量监测、分级降级、ICE 重启与全量重连

**需求与边界**：
- 输入：PC 统计流；输出：降级控制器。
- 边界要求：① 质量分（RTT/丢包/抖动加权）；② 连续降级确认（防单次抖动误切）；③ 降级链顺序（分辨率→帧率→关视频保音频）；④ ICE restart→全量重连两级恢复；⑤ 重连后状态恢复。

**答**：
```javascript
class QualityGuard {
  constructor({ chain = ['1080p', '720p', '360p', 'audioOnly'] }) {
    this.chain = chain; this.level = 0;
    this.badStreak = 0; this.snapshot = null;
  }
  async onStats(stats) {                       // 每 3s getStats
    const q = score({ rtt: stats.rtt, loss: stats.loss,
      jitter: stats.jitter });
    if (q < 0.4) this.badStreak++;             // 防抖确认
    else this.badStreak = 0;
    if (this.badStreak >= 2 && this.level < this.chain.length - 1) {
      this.level++;
      await this.apply(this.chain[this.level]);
      notify('网络较差，已调整画质');
    }
    if (q > 0.7 && this.level > 0) this.recover();  // 恢复升档
  }
  async apply(level) {
    if (level === 'audioOnly')
      return disableVideo();                   // 保音频最后才关
    await setResolution(level);                // encoder 参数调整
  }
  async onIceFailed() {                        // 两级恢复
    await pc.restartIce();                     // 1. ICE 重启
    if (stillFailed()) await fullReconnect({   // 2. 全量重连
      onRestore: () => restoreState(this.snapshot) });
  }
  captureState() {                             // 重连状态快照
    this.snapshot = { mic: micOn, sharing, layout };
  }
}
```

**评分点**:
- 降级链顺序正确（分辨率→帧率→audioOnly，音频最后才关）。
- 连续 2 次确认防抖动误切；恢复升档路径存在。
- 两级恢复：ICE restart→全量重连+状态快照恢复。
- 降级时用户告知（体验透明）。
