---
title: [SOFT-890] 手写 failPointDiagnose：按挂点轮次路由诊断与修正工具（简历关/一面/二面/HR面/终面/薪酬）？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-890：手写 failPointDiagnose：按挂点轮次路由诊断与修正工具（简历关/一面/二面/HR面/终面/薪酬）

**需求与边界**：
- 实现 failPointDiagnose(failHistory)。
- 边界要求：① failHistory 每条 { company, round, note? }；② 轮次路由：resume→SOFT-861 双轮/r1→866 盲区/r2→813+689 表达与分层/hr→364 信号/final→综合画像/offer→493 谈薪；③ 同轮 ≥2 次→SYSTEMIC 升级（找过来人模拟 SOFT-870 铁律）；④ 输出诊断清单与修正动作。

**答**：
```javascript
function failPointDiagnose(failHistory) {
  const ROUTE = {
    resume: { diag: '简历双轮（广告+证据）', fix: 'SOFT-861自检+881三视角模拟' },
    r1: { diag: '技术盲区', fix: 'SOFT-866四分类补齐+884计划器' },
    r2: { diag: '表达结构与深度分层', fix: 'SOFT-813话术+689分层边界+887三形态' },
    hr: { diag: '动机/稳定性/文化信号', fix: 'SOFT-364价值观题+876心态' },
    final: { diag: '综合画像与竞争位', fix: 'SOFT-870梯度策略+861叙事' },
    offer: { diag: '谈薪锚点与信息', fix: 'SOFT-493攻防+867情报' },
  };
  const counts = {};
  const rows = failHistory.map(f => {
    counts[f.round] = (counts[f.round] ?? 0) + 1;
    const r = ROUTE[f.round] ?? { diag: '未知轮次', fix: '复盘note字段补充信息' };
    return { company: f.company, round: f.round,
      diag: r.diag, fix: r.fix, note: f.note };
  });
  const systemic = Object.entries(counts)
    .filter(([, n]) => n >= 2).map(([round]) => ({
      round,
      action: `同轮挂≥2次=SYSTEMIC——找该轮过来人模拟（SOFT-870铁律），非运气归因` }));
  return { rows, systemic,
    priority: systemic.length ? systemic[0].action
      : rows[0]?.fix ?? '无挂点记录' };
}
```

**评分点**:
- 六轮次路由表（每挂点对应诊断与工具卡——SOFT-870 落地）。
- 同轮 ≥2 次 SYSTEMIC 升级（系统性问题的发现与模拟方案）。
- 按频次输出优先修正项。

