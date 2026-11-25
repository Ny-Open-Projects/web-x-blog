---
title: [PER-1254] 手写一个 INP 目标元素分析器
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1254：手写一个 INP 目标元素分析器

**答**：
- 需求：实现 inpTargets(interactions, slowMs=200)。interactions 为 [{ name: click/keydown, target, dur }]；输出慢交互 { targets: [{ selector, count, p75, worst }], rate }（慢交互占总交互比率）；p75 用简单取整分位；同 selector 聚合。
- 边界：空输入返回空 targets；dur 缺失按 0；selector 生成规则同 1011（最多 3 层）。
- 评分点：阈值过滤；聚合；p75 分位；占比

```javascript
function inpTargets(interactions, slowMs = 200) {
  const slow = interactions.filter(i => (i.dur ?? 0) >= slowMs);
  const bySel = {};
  for (const i of slow) {
    (bySel[i.target] ??= { durs: [], count: 0 });
    bySel[i.target].count++;
    bySel[i.target].durs.push(i.dur ?? 0);
  }
  const q75 = a => { const s = [...a].sort((x, y) => x - y);
    return s[Math.min(s.length - 1, Math.floor(s.length * 0.75))]; };
  return {
    targets: Object.entries(bySel).map(([selector, v]) =>
      ({ selector, count: v.count, p75: Math.round(q75(v.durs)),
        worst: Math.round(Math.max(...v.durs)) }))
      .sort((a, b) => b.worst - a.worst),
    rate: interactions.length
      ? +(slow.length / interactions.length * 100).toFixed(1) + '%' : '0%',
  };
}
```
