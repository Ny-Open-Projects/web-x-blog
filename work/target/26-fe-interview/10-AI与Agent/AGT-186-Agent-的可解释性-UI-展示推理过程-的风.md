---
title: [AGT-186] Agent 的可解释性 UI（展示推理过程）的风险与收益怎么权衡？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-186：Agent 的可解释性 UI（展示推理过程）的风险与收益怎么权衡？
**答**：
- 收益：建立信任（用户看到依据什么得出结论）、辅助纠错（用户能指出「你检索错了文件」）、降低黑盒焦虑（尤其是高代价操作前的决策过程展示）。
- 风险一：思维链原文暴露会教用户注入（「原来你说不要透露系统提示，我在对话里这么说就行」），且 CoT 可能包含模型的「胡思乱想」被当官方理由——展示的是「结构化步骤摘要」而非原始 CoT。
- 风险二：过度展示制造虚假确定感——步骤清晰 ≠ 结论正确，要在 UI 上明确「过程展示不构成对结论的保证」。
- 分级展示策略：低风险任务只给结论 + 依据引用；中风险给步骤摘要（可展开）；高风险（资金/删除）给完整决策链 + 关键证据原文，并在执行前强制确认。
- 实现上与 trace 打通：UI 展示层消费 AGT-140 的结构化 trace，而不是另建一套「解释生成」。

```typescript
// 可解释性 UI 的分级展示：从 trace 生成面向用户的解释
import { z } from 'zod';

const ExplainLevel = z.enum(['summary', 'steps', 'full_chain']);
type TraceStep = { kind: string; name: string; status: string; durationMs: number; attrs: Record<string, unknown> };

export function buildExplanation(trace: TraceStep[], level: z.infer<typeof ExplainLevel>, risk: 'low' | 'medium' | 'high') {
  const level_ = risk === 'high' ? 'full_chain' : level;     // 高风险强制全链
  const base = {
    conclusionBasis: trace.filter((t) => t.kind === 'retrieval').map((t) => t.attrs.sourceRef), // 依据引用
    disclaimer: '过程展示不构成对结论正确性的保证。',           // 虚假确定感防御
  };
  if (level_ === 'summary') return { ...base, steps: undefined };

  // 步骤摘要：隐藏原始 CoT 与系统细节，只留动作序列
  const steps = trace
    .filter((t) => t.kind !== 'guard')
    .map((t) => ({ action: humanize(t), status: t.status, ms: t.durationMs }));
  if (level_ === 'steps') return { ...base, steps };

  return { ...base, steps, evidence: trace.filter((t) => t.kind === 'tool' && t.status === 'ok')
      .map((t) => ({ tool: t.name, input: redact(t.attrs.input), output: redact(t.attrs.output) })) }; // 脱敏后展示
}

function humanize(t: TraceStep): string {
  const map: Record<string, string> = { llm: '思考', tool: `调用 ${t.name}`, retrieval: '检索资料', guard: '安全检查' };
  return map[t.kind] ?? t.name;
}
function redact(v: unknown): string {
  return JSON.stringify(v ?? null).replace(/sk-[\w-]+|1[3-9]\d{9}/g, '[已脱敏]').slice(0, 500);
}
```
