---
title: [OPT-162] 内存指标如何接入监控告警（JS heap 趋势与 OOM 防护）？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-162：内存指标如何接入监控告警（JS heap 趋势与 OOM 防护）？

**答**：
- 指标源：`performance.memory`（Chrome，usedJSHeapSize/jsHeapSizeLimit）与 `performance.measureUserAgentSpecificMemory()`；移动端 WebView 可用 Native 桥上报。
- 上报设计：不逐请求传原始值，端上算"滚动窗口斜率 + 峰值占比"（heap / jsHeapSizeLimit），只在越界或趋势异常时上报，降噪 95%。
- 告警阈值三级：峰值占比 > 70% 预警、> 85% 严重 + 立即采样快照线索、OOM 崩溃（crash 上报）P0。
- 归因关联：内存告警聚合时带上页面路由、会话时长、SDK 版本分布，直接回答"哪类页面驻留多久最容易爆"。

```javascript
// 一一对应：内存趋势上报与三级告警
class MemoryMonitor {
  constructor() {
    this.window = [];                          // 滚动窗口：最近 10 次采样
    this.tick();
  }
  tick() {
    const m = performance.memory;
    if (m) {
      const usage = m.usedJSHeapSize / m.jsHeapSizeLimit;   // 峰值占比
      this.window.push(m.usedJSHeapSize);
      if (this.window.length > 10) this.window.shift();
      this.evaluate(usage, m);
    }
    setTimeout(() => this.tick(), 60_000);     // 每分钟采样
  }
  evaluate(usage, m) {
    // 三级判定
    if (usage > 0.85) {
      this.report('critical', usage, m);       // 严重：附最近操作序列
      this.snapshotBreadcrumb();
    } else if (usage > 0.70) {
      this.report('warning', usage, m);        // 预警
    } else if (this.window.length === 10) {
      // 趋势斜率：10 分钟内稳定上涨超 40% 也值得看（未到阈值但趋势坏）
      const growth = (this.window[9] - this.window[0]) / this.window[0];
      if (growth > 0.4) this.report('trend', growth, m);
    }
  }
  report(level, value, m) {
    navigator.sendBeacon('/api/metrics/memory', JSON.stringify({
      level, value: +value.toFixed(3),
      used_mb: Math.round(m.usedJSHeapSize / 1048576),
      route: location.pathname,
      session_min: Math.round((Date.now() - +sessionStorage.ts) / 60000),
      stay_seq: window.__opSeq || 0,           // 最近操作序号，关联回放
    }));
  }
  snapshotBreadcrumb() { /* 触发 rrweb 最近 30s 回放片段上传，配合 OPT-164 */ }
}
if (performance.memory) new MemoryMonitor();
```

## 二十五、性能监控与归因进阶
