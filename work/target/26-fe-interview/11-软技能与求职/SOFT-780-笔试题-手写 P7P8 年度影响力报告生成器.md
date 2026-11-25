---
title: [SOFT-780] 手写 impactReport：四维证据（体系/杠杆/人/外部）年度汇总、缺口提示、下年目标锚定？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-780：手写 impactReport：四维证据（体系/杠杆/人/外部）年度汇总、缺口提示、下年目标锚定

**需求与边界**：
- 实现 impactReport(year, assets)。
- 边界要求：① 四维：体系（方法论产品化引用数 SOFT-757）/杠杆（杠杆系数 SOFT-734）/人（培养出的人数与去向）/外部（分享/开源/社区次数）；② 每维必须有数据（缺数据的维度标 GAP 而非留空——不编数字）；③ 下年目标：按最弱维度自动锚定（短板优先）；④ 输出 markdown 一页报告。

**答**：
```javascript
function impactReport(year, a) {
  const dims = {
    system: { v: a.system?.citations, label: '体系化：方法论被引用' },
    leverage: { v: a.leverage?.total, label: '杠杆：四类杠杆系数' },
    people: { v: a.people?.grown?.length, label: '人：培养出能独当一面者' },
    external: { v: a.external?.events, label: '外部：分享/开源/社区' },
  };
  const rows = Object.entries(dims).map(([k, d]) => ({
    dim: d.label, value: d.v ?? 'GAP（补数据，不编）' }));
  const filled = Object.entries(dims).filter(([k, d]) => d.v != null);
  const weakest = filled.sort((x, y) => x[1].v - y[1].v)[0];
  return {
    report: `# ${year} 影响力报告\n\n` +
      rows.map(r => `- ${r.dim}：${r.value}`).join('\n'),
    gaps: Object.entries(dims).filter(([k, d]) => d.v == null)
      .map(([k]) => k),
    nextYearFocus: weakest ? `短板锚定：${weakest[1].label}——` +
      FOCUS[weakest[0]] : null };
}
const FOCUS = { system: '把1个方法论产品化（模板+工具）',
  leverage: '做1个被≥3团队使用的工具/机制',
  people: '带出1个可独立owner的骨干',
  external: '完成2次对外分享+1项开源贡献' };
```

**评分点**:
- 四维结构对应 P7P8 影响力的完整证据面（体系/杠杆/人/外部）。
- 缺数据标 GAP 不编（诚实性纪律）。
- 最弱维度自动锚定下年目标（短板优先的年度规划）。

