---
title: [AGT-137] 多步任务中途失败，如何用 checkpoint 实现部分失败恢复与重放？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-137：多步任务中途失败，如何用 checkpoint 实现部分失败恢复与重放？
**答**：
- 思路：把 Agent 执行过程建模为「可序列化的步骤日志」——每步完成后持久化（输入、输出、状态、耗时），崩溃恢复时从最后成功步骤重放，而不是从头再来（浪费 token 且可能重复副作用）。
- 幂等是前提：工具调用要带幂等键（stepId 派生），恢复重放时同一键重复执行，服务端去重返回首次结果，避免「重复建单/重复扣款」。
- checkpoint 粒度：LLM 调用与无副作用工具可自动重放；有副作用的工具（写库/发消息）必须依赖幂等键或人工确认后重放。
- 恢复策略可选：自动续跑（信任 checkpoint）、降级为向用户展示「已完成部分 + 剩余步骤」。

```typescript
// checkpoint 持久化 + 幂等重放
import { z } from 'zod';

const StepRecord = z.object({
  runId: z.string(), stepIndex: z.number(),
  kind: z.enum(['llm', 'tool']),
  request: z.unknown(), result: z.unknown(),
  status: z.enum(['done', 'failed']),
  ts: z.number(),
});
type StepRecord = z.infer<typeof StepRecord>;

export class CheckpointStore {
  constructor(private db: Map<string, StepRecord> = new Map()) {}

  async save(r: StepRecord) { this.db.set(`${r.runId}:${r.stepIndex}`, r); }
  async load(runId: string): Promise<StepRecord[]> {
    return [...this.db.values()].filter((r) => r.runId === runId).sort((a, b) => a.stepIndex - b.stepIndex);
  }
}

export async function runWithCheckpoint(runId: string, plan: Step[], store: CheckpointStore) {
  const done = await store.load(runId);
  const results: unknown[] = done.filter((d) => d.status === 'done').map((d) => d.result);
  const idempotencyKey = (i: number) => `${runId}-step-${i}`; // 幂等键：同 runId 同步骤重放去重

  for (let i = done.length; i < plan.length; i++) {
    try {
      const result = await executeStep(plan[i], results, idempotencyKey(i)); // 副作用工具端按 key 去重
      results.push(result);
      await store.save({ runId, stepIndex: i, kind: plan[i].kind, request: plan[i].input, result, status: 'done', ts: Date.now() });
    } catch (e) {
      await store.save({ runId, stepIndex: i, kind: plan[i].kind, request: plan[i].input, result: null, status: 'failed', ts: Date.now() });
      // 自动重试 2 次后交还上层：已完成部分先返回
      throw new RecoverableError(`步骤 ${i} 失败：${(e as Error).message}`, results, i);
    }
  }
  return results;
}

class RecoverableError extends Error {
  constructor(msg: string, public partialResults: unknown[], public failedAt: number) { super(msg); }
}
type Step = { kind: 'llm' | 'tool'; input: unknown; run: (input: unknown, prev: unknown[]) => Promise<unknown> };
async function executeStep(s: Step, prev: unknown[], key: string) { return s.run(s.input, prev); }
```
