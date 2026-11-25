---
title: [AIC-120] 「AI 产出的抽检复审」流程怎么做？谁抽、抽多少、抽出来问题怎么处理？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-120：「AI 产出的抽检复审」流程怎么做？谁抽、抽多少、抽出来问题怎么处理？
**答**:
- 三层抽检分工：PR 内 owner 抽（每 PR 1 个高风险文件，AIC-078）+ 团队周抽查（每人 1 个已合并 PR 复盘）+ 季度专项审计（核心模块全量细查）。
- 抽样策略：风险加权 + 时间衰减——刚引入 AI 的团队高频抽，数据稳定后降频；事故后临时提频。
- 问题处理分级：个体错误（当事人修复+进失败样本库）、系统性错误（改规则/清单/prompt，AIC-042）、工具缺陷（供应商工单或换工具）。
- 结果记录：抽检登记（文件、发现、分类、处理 action），月度聚合看趋势——抽检没有记录就等于没抽。
- 追问钩子：抽检的制度价值是「保持人对产出的手感」——它同时是质量手段和判断力保持手段（AIC-115）。

```javascript
// 周抽查轮盘（公平分配 + 风险加权）
function weeklySample(mergedPRs, team) {
  const scored = mergedPRs.map(p => ({ p, w: p.riskScore + p.aiScopeLines / 500 }));
  const pick = weightedSample(scored, team.length);   // 每人一个，权重抽样
  return pick.map(({ p, assignee }) => ({ pr: p, reviewer: team.shift() }));
}
```
