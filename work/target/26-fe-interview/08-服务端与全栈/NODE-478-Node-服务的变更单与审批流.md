---
title: [NODE-478] Node 服务的变更单（变更管理）与审批分级如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-478：变更单与审批分级
**答**:
- 变更分级：标准变更（预审批的常规发布——模板化免审）、常规变更（1 人审批 + 自动门禁）、高危变更（架构评审 + 双人审批 + 冻结窗口检查：大促/月末资金期禁变更）、紧急变更（hotfix 快速通道——事后 24h 补单复盘）。
- 变更单要素：变更内容/影响面（自动生成 NODE-428）/回滚方案（必填，一键可执行——"回滚方案"写不了说明没想清楚）/验证方案/时间窗口。
- 协调：变更日历（同服务变更互斥——防两变更叠加出问题无法归因；依赖方变更顺序 ARC-164 服务端版）、跨团队变更会签（改共享组件要通知依赖方）。
- 自动化执行：变更单状态驱动流水线（批准 → 自动触发发布 → 完成回填结果），变更与告警/事故关联（事故复盘时能看到变更时间线 ARC-407）。
- 度量：变更成功率、紧急变更占比（高 = 计划性差）、变更导致的事故占比（变更管理有效性的直接指标）。
```javascript
// 变更分级判定
function classify(change) {
  if (change.hotfix) return 'emergency';
  if (change.affects.tier === 'core' || change.isSchema) return 'high'; // 核心链路/DB 变更
  if (isPreApproved(change.template)) return 'standard';
  return 'normal';
}
// 高危校验：inFreezeWindow(now) → reject('冻结期')；双人审批 + 变更日历互斥检查
```
