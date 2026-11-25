---
title: [TST-969] 笔试：手写「AI 用例 flake 统计器」——按用例聚合多轮结果并标注波动模式
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-969：笔试：手写「AI 用例 flake 统计器」——按用例聚合多轮结果并标注波动模式
**答**：
- 需求：实现 flakeReport(results)，results = [{ caseId, run, passed, durationMs }][]。
- 规则：按 caseId 聚合，统计 runs/通过率；结果不一致标记为 flaky 并判定模式（首次失败后成功=预热型、间歇性=随机型、全程失败=broken）；返回按 flake 严重度降序。
- 边界：只有 1 轮的用例标记 insufficient；durationMs 波动超过均值 2 倍标注 slow-flake。

```javascript
function flakeReport(results) {
  const byCase = new Map();
  for (const r of results) {
    if (!byCase.has(r.caseId)) byCase.set(r.caseId, []);
    byCase.get(r.caseId).push(r);
  }
  const out = [];
  for (const [caseId, rs] of byCase) {
    const pass = rs.filter(r => r.passed).length;
    const passes = rs.map(r => r.passed);
    let pattern = 'stable';
    if (rs.length < 2) pattern = 'insufficient';
    else if (pass === 0) pattern = 'broken';
    else if (pass === rs.length) pattern = 'stable';
    else pattern = !passes[0] && passes.slice(1).every(Boolean) ? 'warmup' : 'random';
    const avg = rs.reduce((s, r) => s + r.durationMs, 0) / rs.length;
    const slowFlake = rs.some(r => r.durationMs > avg * 2);
    out.push({ caseId, runs: rs.length, passRate: +(pass / rs.length).toFixed(2),
      pattern, ...(slowFlake ? { slowFlake: true } : {}) });
  }
  return out.sort((a, b) => (a.pattern === 'stable') - (b.pattern === 'stable'));
}
console.log(flakeReport([
  { caseId: 'c1', run: 1, passed: false, durationMs: 100 },
  { caseId: 'c1', run: 2, passed: true, durationMs: 500 },
]).map(x => x.pattern)); // ['warmup']
```
**评分点**：
- 按 caseId 正确聚合多轮结果并算通过率。
- 区分 warmup/random/broken/stable/insufficient 五种模式。
- durationMs 超均值 2 倍标注 slowFlake。
- 按严重度降序，便于优先治理 flaky 用例。
