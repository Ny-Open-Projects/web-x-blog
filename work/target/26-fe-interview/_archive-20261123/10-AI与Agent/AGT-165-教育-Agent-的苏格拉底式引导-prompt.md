---
title: [AGT-165] 教育 Agent 的苏格拉底式引导 prompt 怎么设计？如何防止直接报答案？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-165：教育 Agent 的苏格拉底式引导 prompt 怎么设计？如何防止直接报答案？
**答**：
- 核心 prompt 策略：把「回答正确性」的目标替换为「学习者最近一步的进步」——系统提示明确 Agent 的产出是下一个引导问题而非答案；给答案的许可条件显式写死（学习者连续 N 次明确请求或情绪信号）。
- 结构化教学状态机：维护 learner model（已掌握概念/易错点/当前卡点），每轮先评估学生回复属于哪类（正确/部分对/典型错误/跑题），按状态选策略（强化推进/提示拆解/苏格拉底反问/拉回主题）。
- 防泄漏机制：输出侧校验——回复中不得包含最终答案的关键量（正则/模型自查双检），发现泄漏自动改写为提示。
- 难度校准：提示的「梯度」要受控（先概念澄清，再给方向，再给相似例题，最后才给半成品步骤），每级之间至少间隔一次学生尝试。

```typescript
// 苏格拉底式教学 Agent：状态机 + 泄漏防御
import { z } from 'zod';

const StudentMove = z.object({
  kind: z.enum(['correct', 'partial', 'typical_error', 'off_topic', 'ask_answer']),
  misconception: z.string().nullable(),
});
const LearnerModel = z.object({ mastered: z.array(z.string()), stuckOn: z.string(), hintLevel: z.number().default(0) });
type LearnerModel = z.infer<typeof LearnerModel>;

const SocraticSystem = `你是数学引导老师，绝不可能直接给答案。
规则：
1. 每次回复只能是一个问题或一个提示，不得包含最终答案的数值或结论。
2. 学生答对时，先要求其解释推理，再进入下一层。
3. 学生答错时，用反问指向错误前提，而不是纠正本身。
4. 同一难度提示最多两次，之后给一个结构相似但数字不同的例题。
5. 学生第 3 次明确索要答案且情绪低落时，给出分步解的第一步。`;

export async function teach(turn: { history: { role: string; content: string }[]; learner: LearnerModel; answer: string }) {
  const raw = await llm({ system: SocraticSystem, messages: turn.history });
  const move = StudentMove.parse(JSON.parse(await judgeStudentMove(turn.history.at(-1)!.content, turn.answer)));

  // 输出侧防泄漏：回复不得包含最终答案
  const finalAnswer = turn.answer;
  let reply = raw;
  if (containsAnswer(reply, finalAnswer) && move.kind !== 'ask_answer') {
    reply = await rewriteAsHint(reply, finalAnswer);             // 检出泄漏自动改写
  }
  const learner = advanceLearnerModel(turn.learner, move);
  trace.emit({ kind: 'teach', move: move.kind, hintLevel: learner.hintLevel });
  return { reply, learner };
}

function containsAnswer(reply: string, answer: string): boolean {
  return reply.includes(answer) || new RegExp(answer.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).test(reply);
}
async function judgeStudentMove(student: string, answer: string) { void student; void answer; return JSON.stringify({ kind: 'partial', misconception: null }); }
async function rewriteAsHint(reply: string, answer: string) { return reply.replace(answer, '（此处应为提示，不出现答案）'); }
async function llm(m: any) { return '你检查一下这一步用到的公式前提成立吗？'; }
function advanceLearnerModel(l: LearnerModel, m: z.infer<typeof StudentMove>): LearnerModel {
  return { ...l, hintLevel: m.kind === 'typical_error' ? l.hintLevel + 1 : Math.max(0, l.hintLevel - 1) };
}
function answerEscape(s: string) { return s; }
const trace = { emit: (x: unknown) => { void x; } };
```
