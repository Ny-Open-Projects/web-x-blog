---
title: [SOFT-888] 手写 patternMiner：多次面试复盘数据的模式挖掘（答好/答差题型聚类、状态模式、负面印象关键词）？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-888：手写 patternMiner：多次面试复盘数据的模式挖掘（答好/答差题型聚类、状态模式、负面印象关键词）

**需求与边界**：
- 实现 patternMiner(sessions)。
- 边界要求：① 输入为 InterviewLog 的多场 sessions（SOFT-883）；② 题型聚类：问题按主题聚类（原理/项目/系统设计/行为），统计各类的通过率（答好/差模式 SOFT-879）；③ 状态模式：按场次时间（上午/下午/当日序）统计通过率（SOFT-870 状态依据）；④ 负面印象关键词：outcome=failed 的追问关键词聚类（≥3 次出现标 SYSTEMIC）；⑤ 输出利用建议（扬长/规避/补齐 SOFT-879）。

**答**：
```javascript
function patternMiner(sessions) {
  const byType = {};
  const bySlot = {};
  const negKeywords = {};
  for (const s of sessions) {
    const slot = s.timeOfDay ?? 'unknown';
    bySlot[slot] = bySlot[slot] ?? { pass: 0, total: 0 };
    for (const q of s.questions) {
      const type = q.type ?? 'other';
      byType[type] = byType[type] ?? { pass: 0, total: 0 };
      byType[type].total++;
      if (q.outcome === 'passed') { byType[type].pass++;
        bySlot[slot].pass++; }
      bySlot[slot].total++;
      if (q.outcome === 'failed' && q.keyword) {
        negKeywords[q.keyword] = (negKeywords[q.keyword] ?? 0) + 1;
      }
    }
  }
  const typeRates = Object.entries(byType).map(([t, v]) => ({
    type: t, rate: +(v.pass / v.total).toFixed(2) }));
  const strong = typeRates.filter(r => r.rate >= 0.7);
  const weak = typeRates.filter(r => r.rate <= 0.3);
  const systemic = Object.entries(negKeywords)
    .filter(([, n]) => n >= 3).map(([k]) => k);       // SYSTEMIC SOFT-879
  return {
    strong, weak,
    use: { strengthen: strong.map(s => `${s.type}——放进自我介绍与案例选择（SOFT-862扬长）`),
      fixOrAvoid: weak.map(w => `${w.type}——${w.type === '原理' ? '盲区补齐（SOFT-866）' : '话术强化（SOFT-867）'}`) },
    stateMode: bySlot,
    systemic,
    systemicNote: systemic.length
      ? `SYSTEMIC负面印象：${systemic}——系统性问题，找过来人模拟（SOFT-870铁律）` : null };
}
```

**评分点**:
- 题型聚类通过率（扬长/补齐分流——SOFT-879 利用）。
- 状态模式统计（上午下午与当日序——排期依据 SOFT-870）。
- 负面关键词 ≥3 次标 SYSTEMIC（系统性问题的发现）。

