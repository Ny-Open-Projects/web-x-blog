---
title: [TST-750] AI 生成测试的性能成本如何评估——别让 AI 用例拖垮 CI
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-750：AI 生成测试的性能成本如何评估——别让 AI 用例拖垮 CI

**答**：
- 结论：AI 容易生成「量大但冗余」的用例，必须给生成结果算「性价比」= 缺陷发现概率 / 执行成本，低性价比用例不入库。
- 成本维度：执行时长、资源占用、维护成本（脆弱度）；价值维度：覆盖新分支、历史缺陷关联。
- 平台上限保护：AI 用例单独配额、超时与并发限制，超出自动转夜间跑。
- 追问钩子：某批 AI 用例性价比高但很慢，如何安排执行？

```javascript
// AI 用例性价比评分
function valueScore(test) {
  const cost = test.durationMs / 1000 + test.flaky * 5;
  const value = test.newBranches * 2 + test.linkedBugs * 3;
  const score = cost > 0 ? value / cost : 0;
  return { id: test.id, score: +score.toFixed(2), keep: score >= 1 };
}
console.log(valueScore([
  { id: 't1', durationMs: 1000, flaky: 0, newBranches: 2, linkedBugs: 0 },
  { id: 't2', durationMs: 30000, flaky: 3, newBranches: 1, linkedBugs: 0 },
]));
```
