---
title: [DP-305] 笔试题：手写性能预算 CI 检查器？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-305：笔试题：手写性能预算 CI 检查器？
**题目**：实现 budgetCheck(buildStats, budget)：1) 体积预算逐 chunk 对比（gzip 后）；2) 预算继承（page 继承 base 预算，可覆盖）；3) 冻结期规则（date 在冻结窗口 → 超预算即 fail，平时 warn）；4) 输出报告结构（violations 列表）。
**评分点**：
- 预算合并（继承+覆盖）正确。
- 级别判定正确（冻结期 error / 平时 warn）。
- 报告含超预算百分比与建议。
- gzip 体积来源处理（stats 已含或计算）。
```javascript
function budgetCheck(buildStats, budget, { today, freezeWindows = [] } = {}) {
  const merged = { ...(budget.base ?? {}), ...budget.page };    // 2) 继承+覆盖
  const frozen = freezeWindows.some(([s, e]) => today >= s && today <= e);
  const violations = [];
  for (const [page, limits] of Object.entries(merged)) {
    const stat = buildStats.pages[page];
    if (!stat) continue;
    for (const [metric, limit] of Object.entries(limits)) {
      const actual = stat[metric];
      if (actual > limit) {
        const pct = ((actual / limit - 1) * 100).toFixed(1);
        violations.push({ page, metric, actual, limit, pct, level: frozen ? 'error' : 'warn' });  // 3)
      }
    }
  }
  const report = { frozen, violations,
    summary: violations.filter(v => v.level === 'error').length ? 'CI FAIL' : 'CI PASS' };   // 4)
  return report;
}
// budget 示例：{ base: { jsGzip: 180KB }, page: { home: { jsGzip: 150KB, lcpLab: '2.5s' } } }
// freezeWindows: [['11-05','11-11']]（大促冻结期，超线即 fail）
```
