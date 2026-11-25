---
title: [AIC-895] 笔试：实现 AI 采纳成熟度评估器（问卷打分 + 分级）
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-895：笔试：实现 AI 采纳成熟度评估器（问卷打分 + 分级）
**答**：
- 核心需求：实现 `assess(answers, weights)`。`answers: { questionId, score: 0-4, dimension }[]`；按维度加权汇总得到 0~100 分，并映射到等级 1~4（<40:L1，40~65:L2，65~85:L3，>85:L4）。返回 `{ score, level, byDimension, weakest, advice }`。
- 规则：缺失题目不按 0 计（跳过并对已有题目的权重重新归一化，AIC-858 同理）；score 超出 0~4 裁剪；无有效答案返回 level 1 与空维度；`weakest` 指出最低维度给出改进建议。
- 边界：weights 中未出现的维度用默认权重 1；answers 为空返回安全结果；输出 advice 要具体（「维度 X 得分最低，建议…」）。
- 追问钩子：追问「自评问卷可靠吗」——能答出「问卷只是信号，要结合客观数据（规则文件覆盖率、评测集数量）交叉验证，避免自我美化」的候选人，理解评估的多源验证。

```typescript
type Answer = { questionId: string; score: number; dimension: string };

function assess(answers: Answer[], weights: Record<string, number> = {}) {
  const byDim = new Map<string, { sum: number; w: number }>();
  for (const a of answers ?? []) {
    const s = Math.max(0, Math.min(4, Number.isFinite(a.score) ? a.score : 0));
    const w = weights[a.dimension] ?? 1;
    const x = byDim.get(a.dimension) ?? { sum:0, w:0 };
    x.sum += s * w; x.w += w;         // 缺失题目不按 0 计
    byDim.set(a.dimension, x);
  }
  if (!byDim.size) return { score:0, level:1, byDimension:{}, weakest:null, advice:'无有效答案' };
  const norm: Record<string, number> = {};
  let total = 0, tw = 0;
  for (const [d, x] of byDim) {
    norm[d] = +(x.sum / x.w / 4 * 100).toFixed(1); // 维度分 0~100
    const w = weights[d] ?? 1;
    total += norm[d] * w; tw += w;
  }
  const score = +(total / tw).toFixed(1);
  const level = score < 40 ? 1 : score < 65 ? 2 : score < 85 ? 3 : 4;
  const weakest = Object.entries(norm).sort((a, b) => a[1] - b[1])[0][0];
  return { score, level, byDimension:norm, weakest,
    advice:`维度「${weakest}」得分最低，优先改进；问卷需结合客观数据交叉验证` };
}
console.log(assess([
  { questionId:'q1', score:4, dimension:'规范' },
  { questionId:'q2', score:2, dimension:'评测' },
]));
// level 评估 + 指出「评测」为短板
```
**评分点**：
- 缺失题目跳过并对权重重归一化，不按 0 计（避免误判）。
- score 裁剪 0~4，非法值归 0；空输入返回安全结果。
- 等级映射边界正确（40/65/85 分界），维度分归一到 0~100。
- weakest 与具体 advice，可驱动改进。
- 能指出问卷需结合客观数据交叉验证是加分项。
