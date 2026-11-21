---
title: [AIC-381] 前端基础设施（CDN 预算/构建集群/Agent 算力）的容量规划如何让 AI 参与？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-381：前端基础设施（CDN 预算/构建集群/Agent 算力）的容量规划如何让 AI 参与？
**答**：
- 用量预测：AI 基于历史趋势 + 业务日历（大促/活动）预测构建时长与 Agent token 需求。
- 瓶颈识别：从构建日志识别慢节点与排队热点，给出扩容或优化建议。
- 成本-容量曲线：不同并发度下的吞吐与成本测算，辅助选采购方案。
- 季节性预案：大促前 AI 生成「容量预案」（扩容清单 + 降级开关），人审批执行。

```javascript
const capacityAI = {
  forecast: 'usage(t) ← history + bizCalendar(大促)',
  bottleneck: 'build-log 热点分析',
  plan: '大促预案：扩容清单 + 降级开关，人审批',
};
r
```
