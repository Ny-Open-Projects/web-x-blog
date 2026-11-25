---
title: [AIC-487] 笔试：A/B 两个提示词版本的产出对比判定。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-487：笔试：A/B 两个提示词版本的产出对比判定。
**题目**：两版各跑 n 次，结果 pass 布尔。判定：B 通过率比 A 高 ≥ 10pt 且样本 ≥ 20 → adopt；低 ≥ 10pt → reject；否则 keep-testing。输出判定与两版通过率。

```javascript
function abVerdict(aResults, bResults, { minN = 20, mde = 0.1 } = {}) {
  const rate = r => r.length ? r.filter(Boolean).length / r.length : 0;
  const pa = rate(aResults), pb = rate(bResults);
  if (aResults.length < minN || bResults.length < minN)
    return { verdict: 'insufficient', pa, pb };
  const d = pb - pa;
  return { pa: +pa.toFixed(2), pb: +pb.toFixed(2),
           verdict: d >= mde ? 'adopt-b' : d <= -mde ? 'reject-b' : 'keep-testing' };
}
console.log(abVerdict(
  Array(30).fill(true).concat(Array(20).fill(false)),   // A 0.6
  Array(40).fill(true).concat(Array(10).fill(false)))); // B 0.8 → adopt-b

```

**评分点**：
- 双门槛（效应量 10pt + 样本 20）。
- 中间区间 keep-testing（不过早决策）。
- 率计算除零保护。
- 输出可执行结论。
