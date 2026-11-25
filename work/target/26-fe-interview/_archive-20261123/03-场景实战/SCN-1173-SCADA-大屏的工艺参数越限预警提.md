---
title: [SCN-1173] SCADA 大屏的工艺参数越限预警（提前干预）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1173：SCADA 大屏的工艺参数越限预警（提前干预）

**答**：
- 预警：参数接近工艺上限（90%）预警（黄色），越限（100%）报警（红色）——提前干预减少停机。
- 趋势：逼近速度计算（预计何时越限）。
- 联动：预警时建议操作（降速/调参数）推送操作员。

```javascript
// 越限预警
function limitApproach(value, { low, high }, history) {
  const range = high - low;
  const pct = (value - low) / range;
  if (pct > 0.9) {
    const rate = trendRate(history);                   // 变化速率
    return { level: 'warn', pct: +(pct * 100).toFixed(1) + '%',
      etaMin: rate > 0 ? Math.round((high - value) / rate / 60) : null,
      suggest: '参数接近上限，建议提前干预' };
  }
  return { level: 'ok' };
}
function trendRate(h) { return 0.5; }
```
