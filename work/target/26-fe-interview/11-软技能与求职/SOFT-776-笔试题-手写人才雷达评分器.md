---
title: [SOFT-776] 手写 talentRadar：五信号评分（问题定义/杠杆/判断/口碑/逆境）、潜力排序、培养动作生成？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-776：手写 talentRadar：五信号评分（问题定义/杠杆/判断/口碑/逆境）、潜力排序、培养动作生成

**需求与边界**：
- 实现 talentRadar(people)。
- 边界要求：① people 每条含 { id, problemDef, leverage, judgmentAccuracy, peerFeedback, crisisHandling }（各 1~5）；② 潜力分 = 加权（judgmentAccuracy 与 problemDef 权重最高——SOFT-753 信号）；③ 判断准确率必须有验证记录（无记录按 3 分中性计并标 UNVERIFIED）；④ 排序输出 topN+每人生成培养动作（舞台/反馈/连接/保护四件——SOFT-753）。

**答**：
```javascript
function talentRadar(people, { topN = 3 } = {}) {
  const W = { problemDef: 1.5, leverage: 1, judgmentAccuracy: 1.5,
    peerFeedback: 1, crisisHandling: 1 };
  const rows = people.map(p => {
    const unverified = p.judgmentUnverified === true;
    const j = unverified ? 3 : p.judgmentAccuracy;  // 中性分
    const score = +(Object.entries(W).reduce((a, [k, w]) =>
      a + (k === 'judgmentAccuracy' ? j * w : p[k] * w), 0) /
      Object.values(W).reduce((a, b) => a + b, 0)).toFixed(2);
    return { id: p.id, score,
      flags: unverified ? ['判断准确率UNVERIFIED——需补验证记录'] : [],
      actions: [
        p.leverage <= 3 && '给舞台：关键项目给一个owner位子',
        p.problemDef >= 4 && '给视野：拉入方向级讨论',
        '给反馈：1次具体成长反馈（本月）',
        '给连接：介绍1个关键人脉',
      ].filter(Boolean) };
  }).sort((a, b) => b.score - a.score);
  return { top: rows.slice(0, topN), all: rows,
    note: '培养四件：舞台/反馈/连接/保护（SOFT-753）；不越权不轻许' };
}
```

**评分点**:
- 五信号加权（判断与问题定义权重最高——P7 核心信号）。
- 未验证判断中性计分并标 flag（不凭感觉拔高）。
- 培养动作四件生成（舞台/反馈/连接/保护可执行）。

