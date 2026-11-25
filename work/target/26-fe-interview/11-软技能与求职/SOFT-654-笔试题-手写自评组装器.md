---
title: [SOFT-654] 手写 buildSelfReview：核心成果挑选、数据看板生成、证言引用、不足配额强制？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-654：手写 buildSelfReview：核心成果挑选、数据看板生成、证言引用、不足配额强制

**需求与边界**：
- 实现 buildSelfReview(period)。
- 边界要求：① 核心成果取 2~3 条（领导视角排序——按与对齐目标的匹配度），不足段强制 1 条真实不足（无则从改进项生成，防止全优点自评）；② 数据看板表格输出（指标/期初/期末/基线）；③ 证言段引用原文（截断 80 字）；④ 空周期抛错；⑤ 输出 markdown 自评。

**答**：
```javascript
function buildSelfReview(period, { goals, evidences, testimonials, gaps }) {
  const picked = evidences
    .filter(e => e.week >= period.from && e.week <= period.to);
  if (!picked.length) throw new Error('周期内无证据');
  const core = picked.filter(e => e.kind === 'result')
    .sort((a, b) => matchScore(b, goals) - matchScore(a, goals))
    .slice(0, 3);                                   // 领导视角排序
  const board = core.map(e => e.metric).filter(Boolean)
    .map(m => `| ${m.name} | ${m.from} | ${m.to} | ${m.baseline ?? '-'} |`)
    .join('\n');
  const quote = (t) => t.length > 80 ? t.slice(0, 79) + '…' : t;
  const lack = gaps[0] ?? '（从改进项生成：X能力待加强——已启动Y学习）';
  return [
    '## 核心成果',
    ...core.map(e => `### ${e.text}\n- 数据：${e.metric?.name} ${e.metric?.from}→${e.metric?.to}`),
    '## 数据看板\n| 指标 | 期初 | 期末 | 基线 |\n|---|---|---|---|\n' + board,
    '## 协作影响',
    ...testimonials.slice(0, 2).map(t => `- "${quote(t.text)}" —— ${t.from}`),
    '## 不足与改进\n' + lack,
  ].join('\n\n');
}
function matchScore(e, goals) {                     // 与对齐目标匹配
  return goals.reduce((a, g) => a + (e.text.includes(g.keyword) ? 1 : 0), 0);
}
```

**评分点**:
- 核心成果按领导对齐目标匹配度排序（自评的读者是校准会）。
- 不足段强制（防全优点自评被降权）；证言引用截断防冗长。
- 空周期抛错（没证据就别硬写）。

