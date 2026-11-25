---
title: [SOFT-856] 手写 knowledgeGapMap：关键知识盘点、断层分级（高风险/低风险）、补齐动作与收敛跟踪？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-856：手写 knowledgeGapMap：关键知识盘点、断层分级（高风险/低风险）、补齐动作与收敛跟踪

**需求与边界**：
- 实现 knowledgeGapMap(knowledge, skills)。
- 边界要求：① knowledge 每条 { name, critical, holders: [人] }；② 分级：critical 且 holders≤1→高风险（结对+文档双管 SOFT-846）；critical 多人→低风险（文档即可）；非 critical→归档即可；③ 覆盖率 = 多人持有的 critical 知识/总 critical（收敛指标 SOFT-846）；④ 高风险断层按 holder 离职风险排序（离职风险字段）输出优先补齐清单。

**答**：
```javascript
function knowledgeGapMap(knowledge, skills) {
  const rows = knowledge.map(k => {
    const holders = k.holders.filter(h =>
      skills.some(p => p.id === h && p.skills.includes(k.name)));
    const level = k.critical && holders.length <= 1 ? 'high'
      : k.critical ? 'low' : 'archive';
    const fix = level === 'high'
      ? `结对1次+文档1篇（双管 SOFT-846）；持有人：${holders}`
      : level === 'low' ? '文档归档即可' : '归档';
    return { name: k.name, holders, level, fix,
      exitRisk: holders.length === 1 &&
        (skills.find(p => p.id === holders[0])?.flightRisk ?? false) };
  });
  const critical = rows.filter(r => r.level !== 'archive');
  const covered = critical.filter(r => r.holders.length >= 2).length;
  return { rows,
    coverage: critical.length
      ? +(covered / critical.length * 100).toFixed(1) + '%' : '100%',
    priority: rows.filter(r => r.level === 'high' && r.exitRisk)
      .map(r => `${r.name}：单点+离职风险——本周结对`),
    trend: '季度对比覆盖率（SOFT-846收敛检验）' };
}
```

**评分点**:
- 三级分级（high/low/archive）与差异化补齐动作（SOFT-846 落地）。
- 覆盖率收敛指标（季度趋势可跟踪）。
- 离职风险×单点的优先排序（最危险的断层先补）。

