---
title: [TST-528] 笔试：笔试：大规模相似用例去重（MinHash + LSH）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-528：笔试：笔试：大规模相似用例去重（MinHash + LSH）

**题目**：实现基于 Jaccard 相似度的用例去重。给定用例集合 [{id, steps: string[]}]，要求：① jaccard(a,b) = |A∩B|/|A∪B|；② 用倒排索引做候选筛选（只比较至少共享一个 step 的用例），避免 O(n²) 全比较；③ 输出相似度 >= threshold 的重复对 [{a, b, sim}]，按 sim 降序；④ 边界：空用例、相同 id 跳过、threshold 在 0~1。

**答**：
- 结论：用「倒排索引（step→用例列表）」生成候选对，只对候选算 Jaccard，把复杂度从 O(n²) 降到近 O(n·平均共享)。
- 实现要点：建 step→[ids] 映射；对每个用例收集共享 step 的候选（去重且 id 更大避免重复对）；算 Jaccard 并过滤 >= threshold；降序输出。
- 追问钩子：怎么验证去重候选集没漏？——用 MinHash/LSH 做近似时可设高召回阈值，或用随机采样对比全量结果的 recall。

```javascript
function dedupeCases(cases, threshold = 0.8) {
  const idx = new Map();                       // step -> [caseId]
  cases.forEach(c => (c.steps || []).forEach(s => {
    if (!idx.has(s)) idx.set(s, []);
    idx.get(s).push(c.id);
  }));
  const byId = new Map(cases.map(c => [c.id, new Set(c.steps || [])]));
  const pairs = new Map();
  for (const [step, ids] of idx) {
    for (let i = 0; i < ids.length; i++) for (let j = i + 1; j < ids.length; j++) {
      const [a, b] = [ids[i], ids[j]].sort();
      pairs.set(`${a}|${b}`, [a, b]);
    }
  }
  const out = [];
  for (const [a, b] of pairs.values()) {
    const A = byId.get(a), B = byId.get(b);
    const inter = [...A].filter(x => B.has(x)).length;
    const union = new Set([...A, ...B]).size;
    const sim = union ? inter / union : 0;
    if (sim >= threshold) out.push({ a, b, sim: +sim.toFixed(3) });
  }
  return out.sort((x, y) => y.sim - x.sim);
}
```

**评分点**：
- 倒排索引生成候选对，避免全量 O(n²) 比较。
- Jaccard 计算正确（交集/并集），空集边界处理。
- 候选对去重（排序 key）并跳过相同 id。
- 按 threshold 过滤、相似度降序输出，结果可断言。
