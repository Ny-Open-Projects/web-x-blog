---
title: [PER-679] 手写一个移动端 FPS 与卡顿采样上报器：rAF 测帧间隔 + Native FPS 桥接对齐，输出分档卡顿率
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-679：手写一个移动端 FPS 与卡顿采样上报器：rAF 测帧间隔 + Native FPS 桥接对齐，输出分档卡顿率

**答**：
- JS 侧：rAF 循环测帧间隔，> 32ms 算掉一帧，> 250ms 算严重卡顿；Native 侧 FPS 通过 bridge 周期获取，双源对齐时间窗后合并。
- 要点：采样窗口（如每 10 秒汇总一次掉帧比例）减少上报量；页面不可见时暂停（后台 rAF 停走，样本失真）；卡顿率输出分档（流畅/轻卡/重卡会话占比）。
- 边界：低端机 rAF 本身开销，采样率可配置（低端 0.5）；rAF 不可用（后台）时靠 Native 数据兜底。
- 评分点：不可见暂停与分档卡顿率。

```javascript

class FpsMonitor {
  constructor(bridge, { windowMs = 10000 } = {}) {
    this.bridge = bridge; this.jank = 0; this.frames = 0; this.visible = true;
    document.addEventListener('visibilitychange', () => this.visible = document.visibilityState === 'visible');
    let last = performance.now();
    const loop = (t) => {
      if (this.visible) {
        const gap = t - last;
        this.frames++;
        if (gap > 32) this.jank++;                              // 掉一帧
        if (gap > 250) reportHeavyJank(gap);                    // 严重卡顿单报
      }
      last = t; requestAnimationFrame(loop);
    };
    requestAnimationFrame(loop);
    setInterval(() => this.flush(), windowMs);
  }
  async flush() {
    const nativeFps = await this.bridge.getFps?.() ?? null;      // Native UI 线程 FPS
    const rate = this.frames ? this.jank / this.frames : 0;
    const tier = rate < 0.05 ? 'smooth' : rate < 0.2 ? 'light' : 'heavy';
    navigator.sendBeacon('/collect/fps', JSON.stringify({
      route: location.pathname, jankRate: +rate.toFixed(3),
      tier, nativeFps,                                          // 双线程合并
      deviceTier: navigator.hardwareConcurrency >= 8 ? 'flag' : 'low',
    }));
    this.jank = 0; this.frames = 0;
  }
}
```
