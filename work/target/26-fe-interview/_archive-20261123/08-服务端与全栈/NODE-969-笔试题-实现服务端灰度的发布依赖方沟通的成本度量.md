---
title: [NODE-969] 笔试题——实现沟通成本度量（通知的 ROI 评估）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-969：手写沟通成本

**需求与边界**：
- 需求：沟通成本（SCN-OPS-969/267）——① 沟通成本构成（通知次数/人工确认耗时——SCN-OPS-267 人力）；② 沟通的 ROI（通知带来的避免损失——SCN-OPS-969）；③ 成本与收益的平衡（降噪优化——SCN-OPS-320）；④ 度量的消费（通知策略优化——SCN-OPS-959）。
- 边界：① 成本的人力折算（SCN-OPS-267）；② ROI 的假设声明（SCN-OPS-969）；③ 度量的反博弈（SCN-OPS-284）。

**答**：
```javascript
function commCostAnalysis(notifications) {
  const cost = {
    human: sum(notifications.map(n => n.ackTime ?? 0)) / 3600 * HOURLY_RATE,   // 人力（SCN-OPS-267）
    count: notifications.length,
  };
  const avoided = estimateAvoidedIncidents(notifications);   // 避免损失（假设声明——SCN-OPS-969）
  return { cost, avoided, roi: avoided / cost,
    optimize: cost.count > 100 && roi < 1 ? '增加降噪/合并' : null };   // 优化建议（SCN-OPS-320）
}
```

**评分点**:
- 成本人力折算（SCN-OPS-267）。
- ROI 假设声明（SCN-OPS-969）。
- 降噪优化建议（SCN-OPS-320）。
- 反博弈意识（SCN-OPS-284）。
