---
title: [TST-603] 选测试框架时，POC 评估怎么量化而不是拍脑袋？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-603：选测试框架时，POC 评估怎么量化而不是拍脑袋？

**答**：
- 结论：先定不可妥协的硬约束（一票否决），再加权打分，最后用真实项目切片 POC 验证。
- 硬约束如 ESM 原生支持、CI 总时长上限、团队学习成本；软项按权重 1~5 打分。
- 分数接近时看「可逆性」：迁移成本低的方案优先，避免被框架锁定。
- 追问钩子：POC 结果和厂商 benchmark 差 3 倍，你怎么判断谁可信？

```javascript
function pickFramework(cands, hard, weights) {
  const pass = cands.filter(c => hard.every(h => h.ok(c)));
  const scored = pass.map(c => ({
    name: c.name,
    total: Object.entries(weights)
      .reduce((s, [k, wt]) => s + (c.scores[k] || 0) * wt, 0),
    reversible: c.migrationCost <= 5,
  }));
  return scored.sort((a, b) => b.total - a.total || a.reversible - b.reversible);
}
console.log(pickFramework(
  [{ name: 'Vitest', scores: { speed: 5, dx: 4 }, migrationCost: 3 }],
  [{ ok: c => !!c.name }], { speed: 0.6, dx: 0.4 }));
```
