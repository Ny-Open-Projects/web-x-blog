---
title: [PER-1164] 如何管理"隐私债"（Privacy Debt）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1164：如何管理"隐私债"（Privacy Debt）

**答**：
- 定义：已知但未整改的隐私问题（超期保留/未脱敏日志/未登记字段）——同安全债务管理（1112）。
- 台账：字段+负责人+期限+风险等级；高等级限期清零。
- 防新增：审计管线（1160）拦截新增，台账只减不增。
- 升级：逾期未整改自动升级（团队 lead → 部门），与绩效挂钩的止损机制。

```javascript
// 隐私债台账
function privacyDebtScore(debts) {
  const w = { high: 4, medium: 2, low: 1 };
  return debts.map(d => ({ ...d,
    overdue: d.dueAt < Date.now(),
    score: w[d.level] * (d.dueAt < Date.now() ? 2 : 1) }))
    .sort((a, b) => b.score - a.score);
}
// score >= 8 -> 本周必须出整改计划，否则升级
```
