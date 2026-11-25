---
title: [SCN-1120] IoT 设备的维保管理（保养计划/工单）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1120：IoT 设备的维保管理（保养计划/工单）

**答**：
- 计划：保养计划（周期任务）到期生成工单，逾期告警。
- 工单：维保工单状态机（待接/处理中/完成验收），维修记录归档设备档案。
- 统计：维保成本/故障率趋势（设备健康度评估）。

```javascript
// 维保管理
function maintenancePlan(device, plan) {
  const due = plan.nextDueAt <= Date.now();
  return {
    due, ticket: due ? createMaintTicket(device) : null,
    history: plan.records,                             // 维保记录归档
    healthScore: faultRate(device) < 0.05 ? 'good' : 'watch',
  };
}
function faultRate(d) { return 0.03; }
function createMaintTicket(d) { return 'MT-1'; }
```
