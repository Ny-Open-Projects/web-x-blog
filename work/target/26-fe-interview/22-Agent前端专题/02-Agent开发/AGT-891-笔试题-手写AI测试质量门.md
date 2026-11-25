---
title: [AGT-891] 手写 aiTestGate：变异分数、脆弱选择器、永绿检测、flaky隔离？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-891：手写 aiTestGate：变异分数、脆弱选择器、永绿检测、flaky隔离

**需求与边界**：
- 实现 aiTestGate(tests, { mutationBudget = 20 } = {})。
- 边界要求：① 变异测试抽样（budget 限制变异数），分数 <60% 报浅断言；② 脆弱选择器清单（nth-child/纯文本定位/CSS 类哈希）；③ 永绿检测：对 stub 实现跑测试，通过率 >90% 报无效；④ flaky 率 >5% 的用例进隔离；⑤ 输出按严重度排序。

**答**：
```javascript
const FRAGILE = [/nth-child/, /text=.*$/, /css-[a-z0-9]{6,}/];
async function aiTestGate(tests, { mutationBudget = 20 } = {}) {
  const mut = await runMutation(tests, { limit: mutationBudget });
  const issues = [];
  if (mut.score < 60)
    issues.push({ sev: 1, kind: 'weak-assert', score: mut.score });
  const weak = tests.flatMap(t => t.selectors
    .filter(s => FRAGILE.some(re => re.test(s)))
    .map(s => ({ sev: 2, kind: 'fragile-selector', test: t.name, s })));
  const green = await runAgainstStub(tests);
  if (green.passRate > 0.9)
    issues.push({ sev: 1, kind: 'always-green', passRate: green.passRate });
  const flaky = tests.filter(t => flipRate(t.history) > 0.05)
    .map(t => ({ sev: 3, kind: 'flaky', test: t.name,
      action: 'quarantine' }));
  return [...issues, ...weak, ...flaky]
    .sort((a, b) => a.sev - b.sev);                // 严重度排序
}
```

**评分点**:
- 变异抽样控制成本（budget）且阈值明确（<60% 浅断言）。
- 永绿检测（stub 实现 >90% 通过=无效测试）是 AI 测试特有风险。
- flaky 隔离处置；严重度排序（可行动顺序）。

