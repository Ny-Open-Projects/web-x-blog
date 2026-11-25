---
title: [SCN-1143] IoT 设备控制台的告警确认与静默管理
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1143：IoT 设备控制台的告警确认与静默管理

**答**：
- 确认：告警确认（认领人/备注），静默（已知问题窗口期静默，带过期）。
- 升级：静默期告警仍升级（严重度提升时穿透静默）。
- 复盘：静默策略复盘（静默期间发生的问题归因）。

```javascript
// 静默管理
function silenceAlarm(alarm, silence, { durationMs = 4 * 3600_000 } = {}) {
  return {
    silenced: true, until: Date.now() + durationMs,
    penetrate: alarm.level === 'critical',             // 严重告警穿透静默
    review: () => silenceReview(alarm, silence),
    note: '静默须备注原因，复盘归档',
  };
}
function silenceReview(a, s) { return true; }
```
