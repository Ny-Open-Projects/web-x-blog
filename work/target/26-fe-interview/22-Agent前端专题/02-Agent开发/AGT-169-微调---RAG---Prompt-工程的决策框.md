---
title: [AGT-169] 微调 / RAG / Prompt 工程的决策框架怎么搭？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-169：微调 / RAG / Prompt 工程的决策框架怎么搭？
**答**：
- 先问「错在哪」：知识不对 → RAG（知识外置，可随时更新）；行为/格式不对 → Prompt（改指令成本最低）；知识、行为都对但风格/延迟/成本不行 → 微调（把能力内化）。
- 决策四象限按「知识变化频率 × 任务模式稳定性」：知识高频变 + 模式稳定 → 纯 RAG；知识稳定 + 模式稳定 + 量大 → 可微调；两者都不稳 → Prompt + 强校验兜底。
- 组合而非互斥：生产常是「微调小模型打底（格式/语气/工具调用习惯）+ RAG 供给知识 + Prompt 控制单次行为」；先 Prompt 打 baseline，量化 gap 后再决定要不要引入更重的手段。
- 成本视角：RAG 按查询付推理与检索费、微调一次付训练费后推理更便宜——调用量大且知识稳定的场景微调反而更省。

```typescript
// 微调 vs RAG vs Prompt 决策器（把框架做成可执行的打分）
interface Signals {
  knowledgeChurn: 'daily' | 'monthly' | 'yearly' | 'static';   // 知识更新频率
  taskPattern: 'stable' | 'evolving';                          // 任务模式稳定性
  failureKind: 'wrong_facts' | 'wrong_behavior' | 'wrong_style' | 'too_slow_expensive';
  dailyCalls: number;
}

export function decideStrategy(s: Signals): { primary: string; secondary?: string; rationale: string } {
  if (s.failureKind === 'wrong_facts') {
    if (s.knowledgeChurn === 'daily' || s.knowledgeChurn === 'monthly')
      return { primary: 'RAG', rationale: '事实性错误且知识高频更新，外置知识库 + 检索是唯一能实时跟进的方案' };
    if (s.dailyCalls > 100_000)
      return { primary: 'RAG + 评估微调', secondary: 'SFT', rationale: '知识稳定但调用量大：先用 RAG 打通，再评估把高频知识蒸馏进模型降低检索成本' };
    return { primary: 'RAG', rationale: '事实性错误优先修知识供给' };
  }
  if (s.failureKind === 'wrong_behavior')
    return { primary: 'Prompt 工程', secondary: s.taskPattern === 'stable' ? 'SFT' : undefined,
      rationale: '行为错误先改指令；模式稳定且 Prompt 已到极限（指令过长达不到）再微调固化' };
  if (s.failureKind === 'wrong_style')
    return { primary: 'SFT', secondary: 'few-shot Prompt', rationale: '风格/语气类目标是把分布内化，few-shot 是低成本替代' };
  return { primary: '模型/架构优化', rationale: '慢和贵不是 prompt 问题：换小模型、缓存、批处理（AGT-082/083）' };
}
```
