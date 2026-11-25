---
title: [TST-741] AI 如何辅助「性能回归归因」：从指标异常到代码变更的因果链
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-741：AI 如何辅助「性能回归归因」：从指标异常到代码变更的因果链

**答**：
- 结论：AI 归因是「候选生成 + 证据排序」——先用规则/Idea 找出可能变更，再用 LLM 结合 diff、火焰图、历史给出排序，不直接下结论。
- 因果链要有证据：变更时间早于指标拐点、变更文件在热点路径、同类变更历史上引发过回归。
- LLM 输出必须可验证，给出「证据引用」让人复核，避免幻觉归因。
- 追问钩子：AI 排除了真凶却指向无关变更，如何设计兜底？

```javascript
// 候选变更打分：时间邻近 + 路径相关 + 历史命中
function rankCandidates(changes, regression) {
  return changes.map(c => {
    const timeScore = Math.max(0, 1 - (regression.at - c.at) / 3600000);
    const pathScore = c.files.some(f => regression.hotFiles.includes(f)) ? 1 : 0;
    const histScore = c.tags.includes('perf-sensitive') ? 1 : 0;
    return { id: c.id, score: +(timeScore * 0.5 + pathScore * 0.3 + histScore * 0.2).toFixed(3) };
  }).sort((a, b) => b.score - a.score);
}
console.log(rankCandidates([
  { id: 'c1', at: 1000, files: ['cart.js'], tags: [] },
  { id: 'c2', at: 2000, files: ['ui.css'], tags: ['perf-sensitive'] },
], { at: 4000, hotFiles: ['cart.js'] }));
```
