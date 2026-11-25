---
title: [OPS-219] Feature Flag 的分级权限与审计怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## OPS-219：Flag 权限与审计怎么做的？
**答**：
- 权限分级：flag 读取（开发者）/变更（flag owner）/高危 flag 变更（owner + 平台双审）/紧急全量开关（值班经理）——操作影响力决定权限级别。
- 变更审计：每次 flag 变更记录（谁/何时/旧值→新值/变更原因必填）——flag 变更是「生产变更」，与代码发布同级治理。
- 批量操作防护：批量开关（一键全量）需二次确认 + 影响面预览（涉及多少 flag/多少用户）。
- 审计消费：flag 变更历史与事故时间线交叉——「事故前 10 分钟有 flag 变更」是排障第一线索。
- 追问钩子：为什么 flag 变更要强制填「变更原因」——flag 是「不部署就改变行为」的通道，变更无原因等于生产变更无变更单；原因字段让事后审计（事故归因）能快速回答「为什么当时这么改」，这是 flag 治理与发布治理的对齐。

```javascript
flag.set('checkout-v2', true, { by: currentUser, reason: required('变更原因'),
  approval: isHighRisk ? dualApproval() : ownerApproval(),
  audit: { from: oldValue, to: true, ts: now() } });
// 事故排障第一查
const suspect = flagChanges.within(incidentWindow(-10, 0));
```
