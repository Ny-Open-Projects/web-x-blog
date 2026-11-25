---
title: [SOFT-775] 手写 memoryAudit：ADR/案例库的更新节奏检查、覆盖缺口（决策未归档）清单？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-775：手写 memoryAudit：ADR/案例库的更新节奏检查、覆盖缺口（决策未归档）清单

**需求与边界**：
- 实现 memoryAudit(decisions, docs)。
- 边界要求：① decisions 每条含 { id, date, kind: 'rfc'|'adr'|'memo', archived }；② 缺口清单：决策未归档（archived=false 超 30 天——组织记忆断层）；③ 文档时效：ADR 超 2 年未复核的提示（结论可能失效——带时间戳的判断 SOFT-763）；④ 输出审计报告（归档率/缺口/建议）。

**答**：
```javascript
function memoryAudit(decisions, docs, { now = Date.now() } = {}) {
  if (!decisions?.length) throw new Error('无决策数据');
  const unarchived = decisions.filter(d => !d.archived
    && now - d.date > 30 * 864e5);
  const staleDocs = (docs ?? []).filter(d => d.kind === 'adr'
    && now - d.date > 2 * 365 * 864e5 && !d.reviewed);
  const archived = decisions.length - unarchived.length;
  return {
    archiveRate: +(archived / decisions.length * 100).toFixed(1) + '%',
    gaps: unarchived.map(d => ({
      id: d.id, daysOpen: Math.round((now - d.date) / 864e5),
      fix: '30天内补ADR（决策+理由+复核条件）' })),
    staleADR: staleDocs.map(d => ({
      id: d.id, note: 'ADR超2年未复核——结论可能失效，安排复查' })),
    advice: unarchived.length > decisions.length * 0.3
      ? '归档率<70%：组织记忆断层风险——指定归档责任人'
      : '记忆体系健康' };
}
```

**评分点**:
- 决策未归档 30 天即缺口（组织记忆断层的前置发现）。
- ADR 超 2 年未复核提示（结论带时间戳可失效——非教条）。
- 归档率阈值触发责任人指定（审计有牙齿）。

