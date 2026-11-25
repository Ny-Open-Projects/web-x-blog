---
title: [TST-580] AI 测试落地的 ROI 与预期管理
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-580：AI 测试落地的 ROI 与预期管理

**答**：
- 结论：AI 提效是「生成时间下降 + 覆盖边界增加」，但评审与治理成本会上升；ROI 要算总账（生成省的时间 - 评审治理成本 - 工具成本）。
- 预期管理：明确 AI 不是「全覆盖/零维护」，而是「初稿生成与提效」；设合理目标（如用例编写时间 -30%、边界覆盖 +20%），用试点数据说话再扩面。
- 追问钩子：老板期待「AI 取代测试」怎么沟通？——用数据与边界说明：AI 提升效率但不承担质量责任；把目标对齐到「更快交付 + 更少逃逸」而非「裁人」。

```javascript
// AI 落地 ROI：生成节省 - 评审治理 - 工具成本
function aiRoi({ cases, manualMinPerCase, aiMinPerCase, reviewMinPerCase, toolCost, hourly }) {
  const saved = cases * (manualMinPerCase - aiMinPerCase - reviewMinPerCase) / 60 * hourly;
  const net = saved - toolCost;
  return { savedMinutes: cases * (manualMinPerCase - aiMinPerCase), net,
    positive: net > 0, breakevenCases: Math.ceil(toolCost /
      ((manualMinPerCase - aiMinPerCase - reviewMinPerCase) / 60 * hourly)) };
}
console.log(aiRoi({ cases: 100, manualMinPerCase: 20, aiMinPerCase: 5,
  reviewMinPerCase: 5, toolCost: 1000, hourly: 100 }));
```
