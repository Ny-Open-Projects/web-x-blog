---
title: [OPT-161] 如何发现并上报第三方 SDK 的内存泄漏？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-161：如何发现并上报第三方 SDK 的内存泄漏？

**答**：
- 第三方 SDK（聊天客服、埋点、广告）是内存泄漏重灾区，且代码不可改，只能"发现 + 隔离 + 上报施压"。
- 发现手段：①定期 heap snapshot 对比（两次快照间做相同操作，看哪类对象单调增长、retainer 链指向谁）；②`performance.measureUserAgentSpecificMemory()`（跨域隔离后可用）按周期采样趋势；③SDK 隔离运行——iframe/Worker 里跑 SDK，泄漏被关在笼子里。
- 上报要带证据：泄漏对象构造栈（Allocation stack）、增长速率、SDK 版本号，形成可直接转给 SDK 厂商的 issue 材料。
- 兜底策略：确认泄漏且短期无修复时，对该 SDK 做"定时重建"（销毁重初始化）或按需加载。

```javascript
// 一一对应：SDK 内存泄漏自动巡检 + 证据上报
async function sampleMemory() {
  // 需要 COOP/COEP 跨域隔离头；不支持则退化 performance.memory
  if (performance.measureUserAgentSpecificMemory) {
    return (await performance.measureUserAgentSpecificMemory()).bytes;
  }
  return performance.memory?.usedJSHeapSize ?? null;
}

class LeakSentinel {
  constructor(interval = 10 * 60_000, samples = 12) {  // 2 小时采样 12 次
    this.interval = interval; this.samples = []; this.samplesLimit = samples;
    this.timer = setInterval(() => this.tick(), interval);
  }
  async tick() {
    // 采样前做一次 GC 提示（需 --js-flags=--expose-gc 仅 dev），生产用"稳定值法"
    const bytes = await sampleMemory();
    if (bytes == null) return;
    this.samples.push(bytes);
    if (this.samples.length < this.samplesLimit) return;
    // 12 个采样点做线性回归：斜率显著为正 = 疑似泄漏
    const n = this.samples.length, xs = this.samples.map((_, i) => i);
    const meanX = (n - 1) / 2, meanY = this.samples.reduce((a, b) => a + b) / n;
    const slope = xs.reduce((s, x) => s + (x - meanX) * (this.samples[x] - meanY), 0)
                / xs.reduce((s, x) => s + (x - meanX) ** 2, 0);
    if (slope > 2 * 1024 * 1024) {  // 每个采样周期涨超 2MB
      navigator.sendBeacon('/api/perf/leak-report', JSON.stringify({
        slope_mb_per_tick: +(slope / 1024 / 1024).toFixed(2),
        series_mb: this.samples.map(b => +(b / 1024 / 1024).toFixed(1)),
        sdk_versions: window.__sdkVersions,   // 各 SDK 版本号，方便厂商定位
        url: location.pathname,
      }));
    }
    this.samples = [];
  }
}
new LeakSentinel();
```
