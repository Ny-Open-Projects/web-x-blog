---
title: [SCN-1066] 物流时效承诺的进度条展示（EMS 式进度）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1066：物流时效承诺的进度条展示（EMS 式进度）

**答**：
- 展示：承诺时效进度条（已用/承诺时间比例），超时变色提示。
- 补偿：超时赔付规则自动触发（运费券）。
- 构成：各环节耗时拆分（揽收/干线/派送）。

```javascript
// 时效进度
function slaProgress(waybill, promiseH) {
  const usedH = (Date.now() - waybill.createdAt) / 3600_000;
  const pct = Math.min(100, usedH / promiseH * 100);
  return { pct: +pct.toFixed(1),
    state: pct >= 100 ? 'overdue' : pct > 80 ? 'warning' : 'ok',
    segments: segmentTimes(waybill.nodes),             // 各环节耗时
    compensation: pct >= 100 ? autoCompensate(waybill) : null };
}
function segmentTimes(nodes) { return []; }
function autoCompensate(w) { return { coupon: 5 }; }
```
