---
title: [TST-877] 笔试：手写一个「AI 测试结果的置信度校准器」（置信分数→是否自动合并）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-877：笔试：手写一个「AI 测试结果的置信度校准器」（置信分数→是否自动合并）
**答**：
- 需求：实现 calibrate(aiResults, policy) —— 把 AI 给出的原始置信分数校准后，决定自动合并/人工复核/丢弃。
- 规则：校准分数 = 原始分 × 历史准确率系数（calibrationFactor）；>= high 自动合并，>= low 人工复核，否则丢弃。
- 边界：分数越界（<0 或 >1）钳制；历史样本不足时系数取 1；返回每条决策与统计。

```javascript
function calibrate(aiResults, policy) {
  const { calibrationFactor = 1, high = 0.9, low = 0.6 } = policy;
  const decisions = aiResults.map(r => {
    const clamped = Math.max(0, Math.min(1, r.score)); // 钳制越界
    const calibrated = Number((clamped * calibrationFactor).toFixed(3));
    const decision = calibrated >= high ? 'auto-merge'
      : calibrated >= low ? 'human-review' : 'drop';
    return { id: r.id, raw: r.score, calibrated, decision };
  });
  const stats = decisions.reduce((s, d) => {
    s[d.decision] = (s[d.decision] || 0) + 1; return s;
  }, {});
  return { decisions, stats };
}
console.log(calibrate([
  { id: 1, score: 0.95 }, { id: 2, score: 0.7 }, { id: 3, score: 1.5 }
], { calibrationFactor: 0.9 })); // 1 auto-merge(0.855? ->human-review), 2 review, 3 clamp->0.9 auto-merge

// 历史准确率高时系数上修，更多结果可自动合并
console.log(calibrate([{ id: 4, score: 0.95 }],
  { calibrationFactor: 1.05 }).decisions[0].decision); // auto-merge
```
**评分点**：
- 校准分数 = 原始分 × 历史系数，体现置信度校准而非盲信。
- 分数钳制在 0-1，样本不足系数默认 1，边界处理到位。
- 三档决策（自动合并/人工复核/丢弃）+ 统计，可直接驱动流水线。
- 能点出「AI 置信度往往过度自信，需历史数据校准」这一关键认知。
