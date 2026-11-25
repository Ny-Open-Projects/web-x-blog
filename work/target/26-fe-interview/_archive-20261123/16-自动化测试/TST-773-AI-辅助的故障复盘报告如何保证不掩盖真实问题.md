---
title: [TST-773] AI 辅助的「故障复盘报告」如何保证不掩盖真实问题
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-773：AI 辅助的「故障复盘报告」如何保证不掩盖真实问题

**答**：
- 结论：AI 写复盘要「只做结构化整理与事实聚合，不做根因定性」，根因与责任由人确认，防止 AI 用流畅叙事掩盖真相。
- 报告区分「事实层」（时间线、指标、日志）与「判断层」（根因、改进），AI 只生成事实层，判断层留空给人填。
- 强制包含「未解决问题」与「证据不足项」字段，避免 AI 把不确定写成确定。
- 追问钩子：AI 生成的复盘看起来很专业但避重就轻，如何识别？

```javascript
// 复盘报告结构：AI 填事实，人填判断
function buildPostmortem(aiFacts) {
  return {
    timeline: aiFacts.timeline,       // AI 聚合
    metrics: aiFacts.metrics,         // AI 聚合
    rootCause: null,                  // 人填
    unresolved: aiFacts.uncertainties || [], // 必须保留不确定项
    approved: false,                  // 人确认后才可发布
  };
}
console.log(buildPostmortem({ timeline: ['10:00 注入'], metrics: {}, uncertainties: ['日志缺失'] }));
```
