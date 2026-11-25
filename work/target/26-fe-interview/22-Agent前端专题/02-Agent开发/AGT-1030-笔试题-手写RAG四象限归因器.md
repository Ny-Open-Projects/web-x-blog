---
title: [1030] 笔试手写：实现 RAG 检索/生成两段归因统计
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, RAG, 归因]
type: 笔试题
---

## 1030：笔试手写：实现 RAG 检索/生成两段归因统计

**答**：实现 attribute(cases, { retrieve, answer, grade })：cases 为 { query, evidence: Set, gold }[]。对每例：检索取 topK，判断证据命中（任一 evidence id 在结果里）→ 生成答案 → 打分。输出四象限计数与占比（保留 3 位）+ 建议（retrieval_fail 占比最高返回 'fix retrieval'；gen_fail 最高返回 'fix generation'；hidden_risk > 0.2 返回 'audit knowledge dependency'；否则 'ok'）。

```js
function attribute(cases, { retrieve, answer, grade }, topK = 5) {
  const q = { ok: 0, gen_fail: 0, retrieval_fail: 0, hidden_risk: 0 };
  for (const c of cases) {
    const hits = retrieve(c.query, topK);
    const hasEv = hits.some(h => c.evidence.has(h.id));
    const correct = grade(answer(c.query, hits), c.gold);
    if (hasEv) correct ? q.ok++ : q.gen_fail++;
    else correct ? q.hidden_risk++ : q.retrieval_fail++;
  }
  const n = cases.length || 1;
  const pct = x => +(x / n).toFixed(3);
  const r = { ok: pct(q.ok), gen_fail: pct(q.gen_fail),
    retrieval_fail: pct(q.retrieval_fail), hidden_risk: pct(q.hidden_risk) };
  const max = Object.entries(r).filter(([k]) => k !== 'ok' && k !== 'hidden_risk')
    .sort((a, b) => b[1] - a[1])[0];
  const advice = r.hidden_risk > 0.2 ? 'audit knowledge dependency'
    : max[1] === 0 ? 'ok' : max[0] === 'gen_fail' ? 'fix generation' : 'fix retrieval';
  return { ...r, advice };
}
```

**评分点**：
- 四象限判定逻辑与命名清晰（hidden_risk 的「证据不在但答对」最易漏）
- 除零保护与占比精度统一
- 建议优先级明确：hidden_risk 红线优先于最大项
- 能讨论：hidden_risk 高说明评估集混入「模型自带知识题」，会掩盖检索缺陷，应拆分评估集

