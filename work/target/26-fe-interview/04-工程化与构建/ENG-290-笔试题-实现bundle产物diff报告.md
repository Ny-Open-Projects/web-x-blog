---
title: [ENG-290] 笔试题——实现 bundle 产物 diff 报告（PR 注释生成）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-290：手写 bundle diff 报告

**需求与边界**：
- 输入：基线与当前 manifest（chunk → { files: [{path,size,gzip}] }）；输出 markdown 报告：总量变化、Top 增减 chunk、超标告警。
- 边界：① 按入口聚合（入口总 size 才是用户真实下载量）；② 新增/删除 chunk 分别列出；③ 超 Ratchet 预算的入口标 ⚠️；④ gzip 与 raw 分开报告（传输看 gzip）。

**答**：
```javascript
function bundleDiff(base, current, budgets) {
  const entries = new Set([...Object.keys(base), ...Object.keys(current)]);
  const rows = [];
  for (const entry of entries) {
    const b = sumEntry(base, entry), c = sumEntry(current, entry);   // 入口聚合
    const delta = c.gzip - b.gzip;
    const over = budgets[entry] && c.gzip > budgets[entry];
    rows.push({ entry, rawDelta: c.raw - b.raw, delta, over });
  }
  rows.sort((a, b) => b.delta - a.delta);
  const md = [
    '| entry | raw Δ | gzip Δ | budget |',
    '|---|---|---|---|',
    ...rows.map(r => `| ${r.entry} | ${fmt(r.rawDelta)} | ${sign(r.delta)} | ${r.over ? '⚠️' : '✅'} |`),
  ].join('\n');
  const newChunks = Object.keys(current).filter(k => !(k in base));
  const removed = Object.keys(base).filter(k => !(k in current));
  return { md, newChunks, removed, blocking: rows.some(r => r.over) };
}
const sumEntry = (m, entry) => (m[entry]?.files ?? []).reduce(
  (acc, f) => ({ raw: acc.raw + f.size, gzip: acc.gzip + f.gzip }), { raw: 0, gzip: 0 });
const sign = (n) => n > 0 ? `+${kb(n)}` : kb(n);
const kb = (n) => `${(n / 1024).toFixed(1)}KB`;
```

**评分点**:
- 入口聚合（用户真实下载量，非单 chunk 视角）。
- gzip 与 raw 分开（传输判断用 gzip）。
- Ratchet 超标 blocking 语义（可拦截 PR）。
- 新增/删除 chunk 独立列出（重构/拆包可见）。
