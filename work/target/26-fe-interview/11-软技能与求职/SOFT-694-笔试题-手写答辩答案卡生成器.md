---
title: [SOFT-694] 手写答案卡生成器：高频问题×10 的答案卡结构、证据引用映射、背诵要点提取？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-694：手写答案卡生成器：高频问题×10 的答案卡结构、证据引用映射、背诵要点提取

**需求与边界**：
- 实现 genAnswerCards(case)：case 含 { decisions, metrics, alternatives, risks }。
- 边界要求：① 十类高频问题自动生成（为什么这么设计/替代方案/数据口径/个人贡献/失败与坑/重来/对比竞品/边界/影响面/风险处置）；② 每卡结构：问题+结论+依据（引用证据编号）+边界；③ 依据必须引用证据包编号（无对应证据标 MISSING 需补）；④ 每卡输出背诵要点（≤3 行）。

**答**：
```javascript
function genAnswerCards(case) {
  const Q = [
    ['为什么选这个设计', c => c.decisions.map(d =>
      `${d.name}：选${d.choice}，依据${d.evidence}`)],
    ['有替代方案吗', c => c.alternatives.map(a =>
      `${a.name}被否：${a.reason}（${a.evidence}）`)],
    ['数据口径', c => c.metrics.map(m =>
      `${m.name}：口径${m.scope}，基线${m.baseline}`)],
    ['个人贡献边界', () => case.contribution || 'MISSING：需贡献切割表'],
    ['失败与坑', () => case.pitfalls || 'MISSING：需至少2个真实坑'],
    ['如果重来', () => case.hindsight || 'MISSING'],
    ['与业界方案对比', () => case.benchmark || 'MISSING：需1个外部对照'],
    ['方案的适用边界', c => c.risks.map(r => `不适用：${r.trigger}场景`)],
    ['影响面', c => `${c.scope}（受益方${c.beneficiaries}）`],
    ['风险处置', c => c.risks.map(r => `${r.name}→${r.fallback}`)],
  ];
  return Q.map(([q, gen], i) => {
    const body = gen(case);
    const missing = String(body).includes('MISSING');
    return { no: i + 1, q, body,
      missing,                                        // 证据缺口
      memo: String(body).split('。').slice(0, 3).join('。') }; // 背诵要点≤3句
  });
}
```

**评分点**:
- 十类高频问题全覆盖；答案必须引用证据（无证据标 MISSING 驱动补齐）。
- 每卡带 ≤3 句背诵要点（可背性设计）。

