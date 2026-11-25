---
title: [NODE-538] Node 服务的业务对账告警（差异率的告警与分级）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-538：业务对账告警分级
**答**:
- 对账告警不是"有差异就报"（日差异几百条正常——重试/延迟）——分级响应：差异率阈值分级（< 0.01% 观察 / 0.01~0.1% 日报 / > 0.1% 立即告警 / 单边大额差异（金额 > X）立即电话）。
- 分级依据：金额敏感度（涉资对账比计数对账阈值严 10 倍）、趋势（差异率突增比绝对值重要——新 bug 信号）、方向（我方多记 vs 对方多记——方向不同根因不同：我方多记可能重复计费是事故，对方多记可能是对方漏）。
- 告警内容：差异摘要（笔数/金额/典型样例/对账日/方向）+ 自动初诊（差异按类型分布：时间边界类/重复类/丢失类——初诊定位到根因类别 ARC-432 下钻）、处理入口（工单/补偿任务链接）。
- 闭环：差异处理时效 SLA（按级别：大额 1h/一般 24h）、根因分布统计（Top 差异原因——流程改进依据 ARC-407）、误报治理（对账规则调优——阈值与切片合理性）。
- 联动：差异率与发布关联（新发布后差异率突增 → 发布回滚评估 NODE-446）。
```javascript
function classifyReconDiff(diff) {
  if (diff.amount > LARGE) return 'P0-immediate';                // 单边大额 → 电话
  if (diff.rate > 0.001 || diff.trend === 'surge') return 'P1';
  if (diff.rate > 0.0001) return 'P2-report';
  return 'observe';
}
// 初诊：diffs.groupBy(rootCause) → {timeBoundary: 60%, duplicate: 30%, lost: 10%}
```
