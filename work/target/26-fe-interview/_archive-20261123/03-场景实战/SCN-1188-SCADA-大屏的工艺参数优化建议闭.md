---
title: [SCN-1188] SCADA 大屏的工艺参数优化建议（闭环优化）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1188：SCADA 大屏的工艺参数优化建议（闭环优化）

**答**：
- 建议：参数偏离最优工况提示（模型建议参数），采纳后效果对比（能耗/良率）。
- 权限：建议不自动执行（操作员确认），执行记录归因。
- 学习：建议采纳率反馈优化模型。

```javascript
// 参数优化建议
function paramSuggestion(device, model) {
  const suggest = model.optimal(device.state);
  return {
    suggest,
    current: device.params,
    apply: (confirmed) => confirmed ? api('/param/apply', { device: device.id, ...suggest }) : null,
    compare: () => beforeAfter(device.id),             // 采纳前后效果对比
    adoptionRate: model.adoptionStats,
  };
}
function beforeAfter(id) { return { energy: -0.03, quality: 0.01 }; }
```
