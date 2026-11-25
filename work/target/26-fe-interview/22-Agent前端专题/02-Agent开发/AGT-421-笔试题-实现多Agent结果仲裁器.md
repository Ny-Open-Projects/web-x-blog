---
title: [AGT-421] 笔试题——实现多 Agent 结果仲裁器（证据/权重/升级三阶梯）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-421：手写冲突仲裁：证据强度比较、域权重加权、升级通道与留痕

**需求与边界**：
- 输入：结果数组 [{agent, conclusion, evidence, confidence, domain}]；输出：最终结论+仲裁审计。
- 边界要求：① 硬证据（数字/来源）一方独有→按证据判；② 双方都有依据→按域权重（安全域结论优先于效率域）；③ 仍冲突→标记 escalation 而非强行拍板；④ 仲裁过程全程留痕。

**答**：
```javascript
const DOMAIN_WEIGHT = { security: 3, finance: 2.5, legal: 2.5,
  tech: 1.5, general: 1 };
function arbitrate(results) {
  if (results.length === 1) return { conclusion: results[0].conclusion,
    audit: { mode: 'single' } };
  const audit = [];
  // 1. 证据强度：数字+来源数
  const strength = (r) => (r.evidence?.numeric ? 2 : 0) +
    (r.evidence?.sources?.length ?? 0);
  const scores = results.map(r => ({ ...r,
    s: strength(r) * 2 + (DOMAIN_WEIGHT[r.domain] ?? 1) *
       r.confidence }));
  const best = scores.reduce((a, b) => b.s > a.s ? b : a);
  const runner = scores.filter(r => r !== best)
    .reduce((a, b) => b.s > a.s ? b : a);
  // 2. 分差极小 → 升级（不可强行拍板）
  if (best.s - runner.s < 0.5)
    return { conclusion: null, escalation: true,
      candidates: scores.map(r => r.conclusion),
      audit: { mode: 'escalated', gap: best.s - runner.s } };
  // 3. 结论 + 留痕
  audit.push({ winner: best.agent, loser: runner.agent,
    basis: `证据强度 ${strength(best)} vs ${strength(runner)}，` +
      `域权重 ${best.domain}` });
  return {
    conclusion: best.conclusion,
    dissent: runner.conclusion,               // 保留少数意见
    audit: { mode: 'resolved', gap: best.s - runner.s, log: audit },
  };
}
// 下游消费：escalation=true → 转人工/追加验证子任务。
```

**评分点**:
- 三阶梯完整：证据强度→域权重×置信度→差距过小升级（不强行拍板）。
- 少数意见保留（dissent）——冲突不掩盖，下游可知确定性。
- 权重表可配置且安全/金融域优先（风险敏感设计）。
- 审计完整（winner/loser/basis/gap），升级时附全部候选供裁决。
