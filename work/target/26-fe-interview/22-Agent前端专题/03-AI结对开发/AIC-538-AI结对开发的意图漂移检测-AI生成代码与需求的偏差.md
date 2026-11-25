---
title: [AIC-538] AI 生成代码的意图漂移检测
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-538：意图漂移检测

**答**:
- 意图漂移（Intent Drift）的定义：AI 生成代码随对话轮次增加逐渐偏离原始需求——1) **轮次间语义漂移**（第 1 轮生成搜索功能、第 3 轮 AI 混入了排序功能（用户没要求——LLM 的"热情过度"）；2) **需求覆盖递减**（轮次越多原始需求覆盖越低（LLM 上下文遗忘——前文的需求在后轮被丢失）；3) **需求膨胀**（AI 添加了需求外的功能（"我还帮你加了 X"——超出 scope）；漂移的检测：原始需求的关键词在最终代码中的覆盖率（RBL-532 意图验证的自动化版）。
- 漂移的度量：1) **需求覆盖度**（原始需求的功能点在代码中的实现比例——100% = 完全覆盖；2) **scope 膨胀度**：代码中的功能点不在原始需求中的比例——> 20% = 漂移；3) **轮次衰减**：每轮对话后需求覆盖度的变化趋势（递减 = 漂移）。
- 追问钩子：为什么「意图漂移」在多轮对话中比「单轮生成」更严重？——单轮生成：AI 只有一次机会（prompt 明确——意图清晰）；多轮对话：上下文累积（LLM 的注意力被后续对话分散——原始需求的权重递减）；「LLM 的注意力稀释」：context window 的注意力分配不均匀（最近的对话权重高、最早的 prompt 权重低）——原始需求在对话后期被"遗忘"；解法：每轮 re-state 需求（重复原始需求——强化注意力）或用系统 prompt 固定需求（RBL-510 rules 的对话版）。

```typescript
// 意图漂移检测
interface Requirement { keyword: string; weight: number; }
function detectIntentDrift(
  requirements: Requirement[],
  codePerTurn: string[],                                // 每轮的代码
) {
  // 1) 最终代码的需求覆盖度
  const finalCode = codePerTurn.at(-1) ?? '';
  const covered = requirements.filter(r =>
    finalCode.toLowerCase().includes(r.keyword.toLowerCase()));
  const coverage = requirements.length
    ? +(covered.length / requirements.length * 100).toFixed(1) : 100;
  // 2) 每轮覆盖度趋势（递减 = 漂移）
  const coveragePerTurn = codePerTurn.map(code =>
    requirements.filter(r => code.toLowerCase().includes(r.keyword.toLowerCase())).length /
    requirements.length * 100);
  const driftTrend = coveragePerTurn.length >= 2
    ? coveragePerTurn.at(-1)! - coveragePerTurn[0]
    : 0;
  // 3) scope 膨胀：新增功能的关键词（不在需求中的）
  const reqKeywords = new Set(requirements.map(r => r.keyword.toLowerCase()));
  const codeKeywords = extractFunctionNames(finalCode);
  const scopeCreep = codeKeywords.filter(k => !reqKeywords.has(k.toLowerCase()));
  return {
    coverage,
    driftTrend: +driftTrend.toFixed(1),
    scopeCreep,
    drifted: coverage < 80 || driftTrend < -10 || scopeCreep.length > 3,
  };
}
function extractFunctionNames(code: string): string[] {
  return [...code.matchAll(/(?:function|const)\s+(\w+)/g)].map(m => m[1]);
}
```
