---
title: [AV-226] WebRTC 带宽探测与自适应启动：首帧质量策略
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-226：WebRTC 带宽探测与自适应启动：首帧质量策略

**答**：
- 首帧质量策略：初始码率试探（从保守 500kbps 起步，BWE 快速上升）vs 高质量起步（可能首帧卡）。
- 实现：sender.setParameters 初始 maxBitrate 低 → BWE 上升后逐步提升（每 2 秒 +200kbps 直到 target）。
- 指标：首帧时间 vs 首帧清晰度权衡。

```javascript
class RampUpStrategy {
  constructor(sender) { this.sender = sender; this.current = 500000; }
  async start() {
    await this.setBitrate(this.current);                     // 保守起步：首帧快
    this.ramp();
  }
  async ramp() {
    const stats = await this.sender.getParameters();
    const target = stats.encodings[0].maxBitrate ?? 1500000;
    if (this.current >= target) return;                     // 到目标码率
    setTimeout(async () => {
      this.current = Math.min(target, this.current + 200000);   // 每 2s +200k
      await this.setBitrate(this.current);
      this.ramp();
    }, 2000);
  }
  async setBitrate(b) {
    const p = this.sender.getParameters();
    p.encodings[0].maxBitrate = b;
    await this.sender.setParameters(p);
  }
}
```
