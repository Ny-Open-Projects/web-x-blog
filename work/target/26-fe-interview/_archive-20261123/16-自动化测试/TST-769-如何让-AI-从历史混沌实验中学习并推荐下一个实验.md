---
title: [TST-769] 如何让 AI 从历史混沌实验中学习并推荐下一个实验
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-769：如何让 AI 从历史混沌实验中学习并推荐下一个实验

**答**：
- 结论：推荐系统要「基于已覆盖的故障空间找盲区」，而不是简单重复历史实验；用故障维度矩阵表示覆盖度。
- 把实验记录映射到维度（网络/计算/状态/依赖/时钟 × 注入强度），未覆盖或低覆盖组合作为候选推荐。
- 推荐要说明「为什么」（补哪个盲区、历史上类似实验发现了什么），并排除近期已做的避免重复。
- 追问钩子：AI 推荐了高价值盲区实验但风险很高，如何平衡？

```javascript
// 故障空间覆盖度 → 盲区推荐
function recommendNext(history, dimensions) {
  const covered = new Set(history.map(h => `${h.dim}:${h.level}`));
  const candidates = [];
  for (const d of dimensions.dims) for (const lv of dimensions.levels) {
    if (!covered.has(`${d}:${lv}`)) candidates.push({ dim: d, level: lv, novelty: 1 });
  }
  return candidates.sort((a, b) => b.novelty - a.novelty).slice(0, 3);
}
console.log(recommendNext(
  [{ dim: 'network', level: 'high' }],
  { dims: ['network', 'state'], levels: ['low', 'high'] }
));
```
