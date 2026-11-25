---
title: [TST-669] AI 生成测试数据的「真实性 vs 合规性」怎么平衡？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-669：AI 生成测试数据的「真实性 vs 合规性」怎么平衡？

**答**：
- 结论：用「合成数据 + 脱敏样本 + 约束生成」三层——敏感字段一律合成，非敏感字段保持真实分布。
- 生成后做分布校验（均值/分位数与生产接近）与合规校验（无 PII、无真实 ID）。
- 合规闸门不通过的数据不进测试环境。
- 追问钩子：合成数据分布对得上，但关联关系错了（订单和用户不匹配），怎么发现？

```javascript
function validateSynthetic(rows, { dist, forbidden }) {
  const issues = [];
  rows.forEach((r, i) => {
    forbidden.forEach(k => { if (r[k] != null)
      issues.push({ row: i, why: `含敏感字段 ${k}` }); });
  });
  const amount = rows.map(r => r.amount).sort((a, b) => a - b);
  const p50 = amount[Math.floor(amount.length * 0.5)] || 0;
  if (Math.abs(p50 - dist.amountP50) / dist.amountP50 > 0.2)
    issues.push({ row: 'all', why: '分布漂移' });
  return { pass: issues.length === 0, issues };
}
```
