---
title: [SOFT-886] 手写 jobChangeChecklist：跳槽决策复盘的四问检查、教训条目积累（个人 checklist 迭代）？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-886：手写 jobChangeChecklist：跳槽决策复盘的四问检查、教训条目积累（个人 checklist 迭代）

**需求与边界**：
- 实现 jobChangeChecklist(decision, outcome)。
- 边界要求：① 四问结构化：依据验证（当时判断的依据实际如何）/盲区盘点（该查没查的——SOFT-871）/代价收益对账（预期 vs 实际逐项）/检查项沉淀；② 决策质量与结果分离评估（结果好但依据草率→标 LUCKY 警告 SOFT-871 原则）；③ 检查单迭代：新教训并入个人 checklist（与旧条目去重）；④ 输出 markdown。

**答**：
```javascript
function jobChangeChecklist(d, o, { existing = [] } = {}) {
  const fourQ = [
    { q: '依据验证：当时判断的团队/发展空间实际如何？',
      ans: o.verification },
    { q: '盲区盘点：该查没查的？', ans: o.blindspots ?? [] },
    { q: '对账：预期vs实际（薪资/成长/氛围逐项）',
      ans: o.reconciliation },
    { q: '沉淀：教训→checklist条目', ans: o.lessons ?? [] },
  ];
  const luckyWarn = o.resultGood && (d.basis === 'rumor'
    || d.basis === 'hasty')
    ? '⚠️LUCKY：结果好但依据草率——下次会输回去（SOFT-871：决策质量≠结果）'
    : null;
  const merged = [...new Set([...existing,
    ...(o.lessons ?? [])])];                        // 去重并入
  return {
    fourQ,
    luckyWarn,
    checklist: merged.map(item => `□ ${item}`),
    note: '决策质量评估=当时信息下的合理性（SOFT-750判断力），
      结果好也可能决策差' };
}
```

**评分点**:
- 四问结构化复盘（依据验证/盲区/对账/沉淀——SOFT-871 落地）。
- 决策质量与结果分离（LUCKY 警告——结果好掩盖决策缺陷的防线）。
- checklist 去重迭代（个人检查单的复利积累 SOFT-549 模式）。

