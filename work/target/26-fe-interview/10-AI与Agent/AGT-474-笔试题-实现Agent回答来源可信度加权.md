---
title: [AGT-474] 笔试题——实现来源可信度加权（信任分级+多源交叉+降权）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-474：手写可信度加权：来源分级、多源交叉要求、被举报来源降权

**需求与边界**：
- 输入：召回来源（含来源类型与历史记录）、结论生成请求；输出：加权后的证据与策略。
- 边界要求：① 来源分级（官方文档>内部库>社区>UGC）；② 关键结论要求 ≥2 独立来源支撑；③ 被举报来源降权（举报计数影响权重）；④ 低可信单源结论标注"可信度有限"。

**答**：
```javascript
const TRUST = { official: 1.0, internal: 0.9, community: 0.6,
  ugc: 0.4 };
function weightedEvidence(sources, { reports }) {
  const scored = sources.map(s => {
    const base = TRUST[s.type] ?? 0.5;
    const penalty = Math.min(0.5, (reports[s.id] ?? 0) * 0.1);
    return { ...s, weight: Math.max(0.1, base - penalty) };
  }).sort((a, b) => b.weight - a.weight);
  const top = scored[0];
  const independent = scored.filter(s =>
    s.sourceId !== top.sourceId && s.weight > 0.3);
  // 关键结论策略：需要多源交叉
  const needCross = top.topic?.critical ?? false;
  if (needCross && independent.length === 0)
    return { usable: false, strategy: 'low_confidence_single',
      note: '关键结论仅有单一来源，将标注"可信度有限"并建议核实',
      evidence: scored.slice(0, 3) };
  return {
    usable: true,
    strategy: independent.length >= 1
      ? 'cross_validated' : 'single_source',
    evidence: scored.slice(0, 5),
    weightsNote: scored.slice(0, 3).map(s =>
      `${s.type}:${s.weight.toFixed(2)}`),
    // 生成规则：结论强度 ∝ 最低证据权重
    // low_confidence 标注条件 = min(weight) < 0.5
  };
}
// 举报运营：reports 来自用户"来源可疑"上报（AGT-287 投毒防线）。
```

**评分点**:
- 来源分级权重表 + 举报惩罚（降权下限保护）。
- 关键结论多源交叉要求，单源低可信标注策略。
- 结论强度与最低证据权重挂钩的生成规则。
- 与举报运营闭环（reports 数据回流）。
