---
title: [SOFT-885] 手写 jobSearchPlanner：多线面试的梯度排期（保底/匹配/冲刺）、精力约束、offer deadline 协调？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-885：手写 jobSearchPlanner：多线面试的梯度排期（保底/匹配/冲刺）、精力约束、offer deadline 协调

**需求与边界**：
- 实现 planSearch(companies, myConstraints)。
- 边界要求：① companies 分级 { name, tier: 'safety'|'match'|'dream' }；② 排期规则：safety 先（练习+校准 SOFT-870）→match→dream（最佳状态），同日 ≤2 场、间隔 ≥3 天（复盘时间 SOFT-865）；③ offer deadline 冲突检测：dream 流程预计完成时间晚于已有 offer 到期→生成延 offer 动作（SOFT-485）；④ 精力约束：每周面试 ≤myConstraints.maxPerWeek。

**答**：
```javascript
function planSearch(companies, { maxPerWeek = 3, offerDeadlines = [] } = {}) {
  const order = { safety: 0, match: 1, dream: 2 };
  const sorted = [...companies].sort((a, b) =>
    order[a.tier] - order[b.tier]);
  const schedule = [];
  let cursor = Date.now(); let perWeek = 0;
  for (const c of sorted) {
    cursor += 3 * 864e5;                           // 间隔≥3天
    perWeek = Math.floor((cursor - schedule[0]?.date ?? cursor) / (7 * 864e5));
    schedule.push({ company: c.name, tier: c.tier,
      date: new Date(cursor).toISOString().slice(0, 10),
      note: c.tier === 'safety' ? '练习+市场校准（SOFT-865）'
        : c.tier === 'dream' ? '最佳状态场——提前2周备（SOFT-678功课）'
        : '匹配评估场' });
  }
  const conflicts = offerDeadlines.filter(o =>
    sorted.find(c => c.tier === 'dream') &&
    cursor > o.deadline).map(o => ({
      offer: o.company,
      action: `dream流程晚于offer到期——发延offer请求（SOFT-485话术）` }));
  return { schedule, conflicts,
    rule: '同日≤2场｜间隔≥3天（复盘时间）｜每周≤' + maxPerWeek + '场' };
}
```

**评分点**:
- 梯度排期（safety→match→dream——最佳状态留给最重要的 SOFT-870）。
- 间隔 3 天与周上限（复盘时间的结构保障）。
- offer deadline 冲突检测与延 offer 动作（博弈协调 SOFT-485）。

