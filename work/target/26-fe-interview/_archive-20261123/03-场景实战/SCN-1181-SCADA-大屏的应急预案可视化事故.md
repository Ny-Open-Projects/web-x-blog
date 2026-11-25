---
title: [SCN-1181] SCADA 大屏的应急预案可视化（事故处理流程图）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1181：SCADA 大屏的应急预案可视化（事故处理流程图）

**答**：
- 预案：事故应急预案流程图（步骤/责任人/时间要求）嵌入大屏（报警时自动显示对应预案）。
- 演练：预案演练记录与修订版本管理。
- 执行：预案执行进度勾选（处理过程留痕）。

```javascript
// 应急预案
function emergencyPlan(alarm) {
  const plan = PLANS[alarm.type];
  return {
    steps: plan.steps.map(s => ({ ...s, done: false,
      owner: s.owner, timeLimit: s.timeLimit })),
    check: (i) => api('/plan/check', { alarmId: alarm.id, step: i }),   // 执行留痕
    version: plan.version, drills: plan.drillRecords,
  };
}
const PLANS = { overheat: { steps: [{ name: '降负荷', owner: '操作员', timeLimit: '5min' }], version: 'v3', drillRecords: [] } };
```
