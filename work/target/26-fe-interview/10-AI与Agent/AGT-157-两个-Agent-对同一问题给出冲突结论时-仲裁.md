---
title: [AGT-157] 两个 Agent 对同一问题给出冲突结论时，仲裁怎么设计？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-157：两个 Agent 对同一问题给出冲突结论时，仲裁怎么设计？
**答**：
- 先区分冲突类型：事实冲突（数据/引用不一致，可程序化复核）、判断冲突（方案权衡不同，需价值排序）、格式冲突（schema 不同，便宜修复）——仲裁策略完全不同。
- 三层仲裁：规则层（能程序验证的直接验证：跑测试、查数据源）；裁判层（LLM-as-judge 带双方案原文 + 冲突点提示，要求输出裁决与理由）；升级层（裁判置信度低或涉及业务红线时交人工，附双方论据摘要）。
- 仲裁输入要「对称公平」：两个结论匿名化（方案 A/B 随机顺序）防位置偏差，且都带完整证据链，防止裁判只看结论不看依据。
- 结果回流：裁决要写进共享记忆，同类冲突的裁决标准沉淀为 prompt 里的裁决原则，减少重复仲裁。

```typescript
// 冲突仲裁器：规则层 → 裁判层 → 升级层
import { z } from 'zod';

const Verdict = z.object({
  winner: z.enum(['A', 'B', 'tie']),
  confidence: z.number().min(0).max(1),
  reasoning: z.string(),
});
type Verdict = z.infer<typeof Verdict>;

export async function arbitrate(conflict: {
  question: string; type: 'fact' | 'judgment' | 'format';
  a: { answer: string; evidence: string[] }; b: { answer: string; evidence: string[] };
}): Promise<{ resolution: string; by: 'rule' | 'judge' | 'human'; verdict?: Verdict }> {

  if (conflict.type === 'fact') {                              // 规则层：事实冲突查数据源复核
    const truth = await verifyFacts(conflict.a.evidence, conflict.b.evidence);
    if (truth !== null) return { resolution: truth, by: 'rule' };
  }
  if (conflict.type === 'format') return { resolution: mergeFormats(conflict.a.answer, conflict.b.answer), by: 'rule' };

  // 裁判层：匿名 + 随机顺序，防位置偏差
  const swap = Math.random() < 0.5;
  const [A, B] = swap ? [conflict.b, conflict.a] : [conflict.a, conflict.b];
  const raw = await llm(`问题：${conflict.question}\n方案A：${JSON.stringify(A)}\n方案B：${JSON.stringify(B)}
    请裁决并输出 JSON { winner, confidence, reasoning }。依据证据强度与可验证性，不接受无证据偏好。`);
  const v = Verdict.parse(JSON.parse(raw));
  const realWinner = v.winner === 'tie' ? 'tie' : (swap ? (v.winner === 'A' ? 'B' : 'A') : v.winner);

  if (v.confidence < 0.6) {                                    // 升级层：低置信度交人工
    await humanQueue.push({ question: conflict.question, a: conflict.a, b: conflict.b });
    return { resolution: '已转人工仲裁，附双方论据', by: 'human' };
  }
  return { resolution: realWinner === 'tie' ? '双方结论各取所长合并' : `采纳方案 ${realWinner}`, by: 'judge', verdict: v };
}

async function verifyFacts(ea: string[], eb: string[]): Promise<string | null> { void ea; void eb; return null; }
function mergeFormats(a: string, b: string) { return `${a}\n${b}`; }
async function llm(p: string) { return JSON.stringify({ winner: 'A', confidence: 0.7, reasoning: '证据更完整' }); }
const humanQueue = { push: async (x: unknown) => { void x; } };
```
