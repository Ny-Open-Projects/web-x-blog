---
title: [SCN-1107] IoT 设备详情页的实时遥测曲线（高频数据）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1107：IoT 设备详情页的实时遥测曲线（高频数据）

**答**：
- 数据：遥测（温度/电压）高频上报（1s 级）——前端曲线节流渲染（LTTB 降采样 + rAF）。
- 窗口：实时窗口（最近 1h）+ 历史查询（降采样后查询，服务端聚合）。
- 性能：曲线增量追加（不是全量重绘）。

```javascript
// 遥测实时曲线
class TelemetryChart {
  constructor(chart, { windowMs = 3600_000 } = {}) {
    this.chart = chart; this.win = windowMs; this.data = [];
  }
  push(point) {
    this.data.push(point);
    const cutoff = Date.now() - this.win;
    this.data = this.data.filter(p => p.ts >= cutoff);
    requestAnimationFrame(() => this.chart.update(lttb(this.data, 500)));
  }
}
function lttb(data, n) { return data.filter((_, i) => i % Math.ceil(data.length / n) === 0); }
```
