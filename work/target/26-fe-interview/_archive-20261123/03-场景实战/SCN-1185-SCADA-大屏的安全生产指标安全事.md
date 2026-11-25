---
title: [SCN-1185] SCADA 大屏的安全生产指标（安全事故看板）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1185：SCADA 大屏的安全生产指标（安全事故看板）

**答**：
- 指标：安全运行天数/隐患整改率/应急演练完成率/未遂事件记录。
- 展示：安全看板独立分区（安全数据醒目位置）。
- 闭环：隐患上报 → 整改 → 验收闭环流程。

```javascript
// 安全看板
function safetyBoard(safety) {
  return {
    days: safety.daysWithoutIncident,
    hazards: { open: safety.hazardsOpen, closed: safety.hazardsClosed,
      rate: +(safety.hazardsClosed / (safety.hazardsOpen + safety.hazardsClosed || 1) * 100).toFixed(1) + '%' },
    drills: safety.drillCompletion,
    nearMiss: safety.nearMissReports,                  // 未遂事件上报鼓励
  };
}
```
