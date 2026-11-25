---
title: [AIC-703] 结对中如何让 AI 主动暴露不确定性而不是自信地出错
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-703：结对中如何让 AI 主动暴露不确定性而不是自信地出错

**答**：
- 结论先行：要在 prompt 层面强制「不确定性标注」——要求 AI 对每个结论给出置信度与依据来源，无法确定的地方显式说「我不确定 / 需要确认」，而不是用流畅语言编造。
- 三个手法：1) 让 AI 输出「假设清单」并逐条标注是否需人确认；2) 要求引用具体文件/行号或 API 签名，引用不到的标为「推测」；3) 让 AI 自问「哪一处最可能出错」做自我质疑。
- 反直觉点：给 AI 留「退出通道」——明确告诉它「不知道就说不知道」不会被惩罚，能显著降低幻觉式自信。
- 追问钩子：如何区分「AI 真的不确定」和「AI 学会了偷懒全标不确定」？——用已知答案的探针题校准标注可信度。

```typescript
// 让 AI 输出带置信度的结构化结论
type Claim = { text: string; confidence: number; source?: string };
function formatUncertainty(claims: Claim[]): string {
  return claims.map(c => {
    if (c.confidence >= 0.8 && c.source) return `[确定] ${c.text} (${c.source})`;
    if (c.confidence >= 0.5) return `[待确认] ${c.text}`;
    return `[推测] ${c.text} —— 需人工核实`;
  }).join('\n');
}
console.log(formatUncertainty([
  { text: 'fetch 在 Node18 原生可用', confidence: 0.9, source: 'node:18 docs' },
  { text: '该依赖已弃用', confidence: 0.6 },
  { text: '此处不会 N+1', confidence: 0.3 },
]));
// [确定] ... [待确认] ... [推测] ... 需人工核实
```
