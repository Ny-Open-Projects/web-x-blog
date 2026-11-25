---
title: [1201] 笔试手写：实现检索漏斗的分级归因统计
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, RAG]
type: 笔试题
---

## 1201：笔试手写：实现检索漏斗的分级归因统计

**答**：实现 funnel(cases, retrieve, answer, grade)：cases 为 { query, evidence: Set, gold }[]。逐例计算漏斗阶段：retrieved（返回非空）> evidenceInTopK（证据进 top-k）> cited（答案引用了证据）> correct（评分通过）。输出各阶段计数与相邻转化率（3 位，除零 null），并返回 bottleneck（转化率最低的相邻阶段名）。

```js
function funnel(cases, retrieve, answer, grade, topK = 5) {
  const stages = ['retrieved', 'evidenceInTopK', 'cited', 'correct'];
  const counts = { retrieved: 0, evidenceInTopK: 0, cited: 0, correct: 0 };
  for (const c of cases) {
    const hits = retrieve(c.query, topK);
    if (!hits.length) continue;                        // 未过第一级不计入后续
    counts.retrieved++;
    const evHit = hits.slice(0, topK).some(h => c.evidence.has(h.id));
    if (!evHit) continue;
    counts.evidenceInTopK++;
    const ans = answer(c.query, hits);
    const cited = (ans.citations || []).some(id => c.evidence.has(id));
    if (!cited) continue;
    counts.cited++;
    if (grade(ans.text, c.gold)) counts.correct++;
  }
  const conv = {};
  for (let i = 1; i < stages.length; i++) {
    const p = stages[i - 1], cur = stages[i];
    conv[p + '->' + cur] = counts[p] ? +(counts[cur] / counts[p]).toFixed(3) : null;
  }
  const entries = Object.entries(conv).filter(([, v]) => v !== null);
  const bottleneck = entries.length
    ? entries.sort((a, b) => a[1] - b[1])[0][0] : null;
  return { counts, conv, bottleneck };
}
```

**评分点**：
- 漏斗的「逐级 continue」语义正确（未过上级不计入下级分母）
- 除零返回 null；bottleneck 取最低相邻转化率
- cited 判定基于答案引用与证据集交集
- 能讨论：与四象限归因的关系（漏斗定位阶段、象限定位组合）、bottleneck 驱动的修复优先级

