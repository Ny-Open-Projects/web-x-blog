---
title: [AIC-562] 多模型协作的结果一致性验证
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-562：多模型协作的一致性验证

**答**:
- 多模型协作的一致性：1) **双模型对比**（同一 prompt 发两个模型 → 对比输出（一致 = 高置信度；不一致 = 需要人工裁决）；2) **n-of-m 投票**（N 个模型同 prompt → 多数派结果（3 选 2 / 5 选 3——多数投票提升可靠性）；3) **成本 vs 置信度**：单模型（最便宜/置信度低）vs 双模型对比（2x 成本/置信度中）vs n-of-m 投票（Nx 成本/置信度高）——「验证成本 = 置信度提升的代价」。
- 一致性的判定：1) **精确一致**（代码完全相同——极罕见但最高置信）；2) **语义一致**（实现不同但行为相同——测试通过即可——normalize 后比较 RBL-667）；3) **不一致**（行为不同——需要人工裁决或第三模型投票）；「一致的类型」决定验证策略。
- 追问钩子：为什么「多模型不一致」比「单模型输出」更有信息量？——单模型 = 只有一个答案（不知道是"对"还是"碰巧对"）；双模型一致 = 两个独立生成器得出相同结论（高置信度——"独立验证"的原理）；双模型不一致 = 至少一个错（需要人工裁决——但人的裁决有了"对比"参考——更容易判断）；「不一致的信息量」：不一致的 diff 区域 = 可能的 bug 区域（精确聚焦人的注意力——比看全量代码更高效）。

```typescript
// 多模型一致性验证
async function multiModelVerify(prompt: string, models: LLMClient[], { mode = 'pair' } = {}) {
  const results = await Promise.all(models.slice(0, mode === 'pair' ? 2 : models.length)
    .map(m => m.generate(prompt)));
  if (mode === 'pair' && results.length === 2) {
    const consistent = normalizeOutput(results[0]) === normalizeOutput(results[1]);
    return { consistent, results, verdict: consistent ? 'high-confidence' : 'needs-review',
      diffArea: consistent ? null : diffRegion(results[0], results[1]) };
  }
  // 投票模式
  const normalized = results.map(normalizeOutput);
  const counts = new Map<string, number>();
  normalized.forEach(r => counts.set(r, (counts.get(r) ?? 0) + 1));
  const [winner, count] = [...counts.entries()].sort((a, b) => b[1] - a[1])[0];
  const unanimous = count === results.length;
  return { results, verdict: unanimous ? 'unanimous' : 'majority',
    winner, confidence: +(count / results.length * 100).toFixed(0) + '%' };
}
function normalizeOutput(code: string) {
  return code.replace(/\s+/g, ' ').trim();               // 空白规范化
}
```
