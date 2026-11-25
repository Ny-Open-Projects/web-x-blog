---
title: [SCN-707] SLA 看板的值班视图（oncall dashboard）与日常视图有什么不同？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-707：值班视图怎么设计？
**答**：
- 值班视图三要素：现在怎么样（当前 burn rate/活跃告警）、最近有没有恶化（1h 对比）、我要做什么（未认领告警列表置顶）——信息密度为「快速决策」服务。
- 日常视图不同：趋势/周报/预算消耗曲线/改进项追踪，服务于复盘与规划。
- 值班视图的时间窗短：最近 1h~6h 主导，30 天趋势收进侧栏；颜色语义统一（绿=正常/黄=关注/红=行动）且每屏不超过 3 个红。
- 交接友好：视图带「班次摘要」自动生成（值班期间触发过什么/处理了什么/遗留什么），交接时一键分享。
- 追问钩子：为什么值班视图要把未认领告警置顶——值班第一职责是「所有火都有人认」，列表排序就是流程引导。

```javascript
const oncallView = {
  primary: [
    { widget: 'burn-rate', window: '1h', compare: 'prev_1h' },
    { widget: 'unclaimed-alerts', sort: 'severity', max: 5 },   // 未认领置顶
    { widget: 'recent-deploys', window: '2h' },                 // 最近发版（排障上下文）
  ],
  shiftSummary: async (shift) => ({
    fired: await alerts.fired(shift), resolved: await alerts.resolved(shift),
    carryOver: await alerts.open(shift.endTs),          // 遗留交接
  }),
};
```
