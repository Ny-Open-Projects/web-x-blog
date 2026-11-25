---
title: [SOFT-733] 手写 levelSelfAssess：按层级能力模型逐项自评、达标率计算、目标层级差距清单？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-733：手写 levelSelfAssess：按层级能力模型逐项自评、达标率计算、目标层级差距清单

**需求与边界**：
- 实现 levelSelfAssess(current, target)。
- 边界要求：① 能力模型按层级定义（P6: 交付/协作/小影响力；P7: 体系/杠杆/跨团队/带人——每维度 0~5 分）；② 达标率 = 达标维度数/总维度（得分 ≥ 模型要求即达标）；③ 差距清单输出（未达标维度：当前分→要求分+补齐建议）；④ 未知层级抛错；⑤ 输出含时机建议（达标率 >80% 可报 SOFT-682）。

**答**：
```javascript
const MODELS = {
  P6: { 交付: 4, 协作: 4, 小影响力: 3 },
  P7: { 体系: 4, 杠杆: 4, 跨团队: 3, 带人: 3 },
};
function levelSelfAssess(current, target, myScores) {
  const model = MODELS[target];
  if (!model) throw new Error(`未知层级：${target}`);
  const rows = Object.entries(model).map(([dim, req]) => {
    const mine = myScores[dim] ?? 0;
    return { dim, mine, req, ok: mine >= req,
      advice: mine >= req ? null :
        `补齐${dim}：当前${mine}/要求${req}——` +
        SUGGEST[dim] ?? '参与对应场景积累证据' };
  });
  const pass = rows.filter(r => r.ok).length;
  const rate = pass / rows.length;
  return { rows, rate,
    timing: rate >= 0.8 ? '可报（>80%）'
      : rate >= 0.6 ? '补半年再报（60-80%）' : '先沉淀（<60%）',
    gaps: rows.filter(r => !r.ok) };
}
const SUGGEST = {
  体系: '把重复工作抽象成机制/文档（SOFT-705）',
  杠杆: '工具/机制/知识/决策四杠杆盘点（SOFT-704）',
  跨团队: '主动承担跨团队协作与技术外交（SOFT-728）',
  带人: '先带2人mentor试金石（SOFT-708）',
};
```

**评分点**:
- 层级模型结构化（各维度分值门槛）；未知层级抛错。
- 达标率→时机建议联动（>80% 可报，量化决策）。
- 差距清单带具体补齐建议（可行动）。

