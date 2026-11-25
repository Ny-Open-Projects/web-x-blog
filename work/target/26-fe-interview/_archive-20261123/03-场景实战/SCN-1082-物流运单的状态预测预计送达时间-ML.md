---
title: [SCN-1082] 物流运单的状态预测（预计送达时间 ML 特征）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1082：物流运单的状态预测（预计送达时间 ML 特征）

**答**：
- 预测：ETA 模型特征（线路历史/天气/大促/网点效率），前端展示置信区间。
- 展示：预计送达时间段（如"明天 14:00-18:00"）+ 延误风险标注。
- 更新：节点事件驱动重估（分拨完成刷新 ETA）。

```javascript
// ETA 预测展示
function etaDisplay(prediction) {
  return {
    window: `${prediction.from}~${prediction.to}`,
    confidence: prediction.confidence,                 // 置信度
    risk: prediction.delayRisk > 0.3 ? '延误风险较高' : null,
    factors: prediction.factors,                       // 影响因子透明
  };
}
// factors: ['线路历史时效', '当前天气', '网点积压']
```
