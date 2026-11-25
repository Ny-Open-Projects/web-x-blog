---
title: [SOFT-655] 手写 prepReview：材料核对、预设问题生成、异议材料准备、演练提示？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-655：手写 prepReview：材料核对、预设问题生成、异议材料准备、演练提示

**需求与边界**：
- 实现 prepReview(context)：context 含 { selfReview, evidenceGaps, expectedVsActual }。
- 边界要求：① 材料核对：自评引用的数据每条必须能在证据库找到（找不到标 MATERIAL_MISSING）；② 预设问题生成三类（依据/差距/行动指南）按顺序输出；③ expectedVsActual 有差距时自动生成书面补充材料骨架（事实/证据/诉求）；④ 输出演练提示（每问排练提示）。

**答**：
```javascript
function prepReview({ selfReview, evidenceLog, expectedVsActual }) {
  const missing = selfReview.metrics.filter(m =>
    !evidenceLog.find(e => e.metric?.name === m.name))
    .map(m => m.name);                              // 材料核对
  const questions = [
    { q: '评级的主要依据是哪几条？', why: '抓权重', drill: '追问不超过两层' },
    { q: '到下一档的差距清单？2-3条可执行的。',
      why: '行动指南', drill: '要求书面化' },
    { q: '下周期我做到什么，您在校准会上最有把握为我辩护？',
      why: '共同规划者转换', drill: '最后问' },
  ];
  const out = { materialCheck: { missing,
    fix: missing.length ? '自评数据须补证据链接' : 'OK' },
    questions,
    rehearsal: '三问各排练一遍；敏感问题（同侪位置）最后问' };
  if (expectedVsActual?.diff) {
    out.appealDraft = [
      '## 补充说明（24h内发）',
      `事实：${expectedVsActual.facts}`,
      `证据：${expectedVsActual.evidenceLinks}`,
      '诉求：请复核事实认定（非要求改评级）',
    ].join('\n');
  }
  return out;
}
```

**评分点**:
- 材料核对闭环（自评数据必须在证据库可查——引用无据是自评大忌）。
- 三类预设问题按序生成+收尾金句（共同规划者转换）。
- 有差距自动生成申诉骨架（24h 书面补充流程化）。

