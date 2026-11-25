---
title: [SCN-1068] 物流 cold chain 冷链运输的温度监控展示
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1068：物流 cold chain 冷链运输的温度监控展示

**答**：
- 监控：车厢温度实时上报（IoT 温度计），超温告警（药品/生鲜）。
- 记录：全程温度曲线（合规留档），异常区间标注。
- 处置：超温件隔离与质检流程。

```javascript
// 冷链监控
function coldChainMonitor(shipment) {
  const breaches = shipment.tempLog.filter(t =>
    t.value < shipment.range.min || t.value > shipment.range.max);
  return {
    curve: shipment.tempLog,
    breaches,                                          // 超温区间
    action: breaches.length ? '隔离质检' : 'ok',
    compliance: breaches.length === 0,                 // 合规留档
  };
}
```
