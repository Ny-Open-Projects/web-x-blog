---
title: [AGT-140] Agent 的 trace 日志结构怎么设计？一次运行要记录哪些字段？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-140：Agent 的 trace 日志结构怎么设计？一次运行要记录哪些字段？
**答**：
- 分层结构：run（一次任务）→ step（一次模型调用或工具执行）→ span（更细的 IO/解析阶段）；每层有唯一 id 与父子引用，跨 Agent 用统一 traceId 串联。
- step 必记字段：类型（llm/tool）、输入摘要（大输入截断+哈希）、输出摘要、token 用量（prompt/completion）、延迟、成本、状态与错误码、重试次数。
- 隐私与体积平衡：默认只存「摘要+指纹」，原始大 payload 按 TTL 单独冷存；用户标识做假名化。
- 设计验收标准：拿到一条 trace 能离线重放出「模型当时看到了什么、为什么这么决策、花了多少钱」——这是排查与评测复用的基础。

```typescript
// trace 数据结构与记录器
import { z } from 'zod';

export const StepTrace = z.object({
  traceId: z.string(), runId: z.string(), stepId: z.string(), parentSpanId: z.string().nullable(),
  kind: z.enum(['llm', 'tool', 'retrieval', 'guard']),
  name: z.string(),
  status: z.enum(['ok', 'error', 'timeout', 'aborted']),
  startedAt: z.number(), durationMs: z.number(),
  tokens: z.object({ prompt: z.number(), completion: z.number() }).default({ prompt: 0, completion: 0 }),
  costUsd: z.number().default(0),
  retries: z.number().default(0),
  inputDigest: z.string(),   // sha256(输入) + 长度，原文冷存
  outputDigest: z.string(),
  inputPreview: z.string().max(2000),  // 截断预览，便于人读
  outputPreview: z.string().max(2000),
  error: z.object({ code: z.string(), message: z.string() }).nullable(),
  attrs: z.record(z.unknown()).default({}), // 自定义维度：模型名、工具名、命中率等
});
export type StepTrace = z.infer<typeof StepTrace>;

export class Tracer {
  constructor(private traceId = crypto.randomUUID(), private sink: (t: StepTrace) => void = console.info) {}

  async step<T>(meta: Pick<StepTrace, 'runId' | 'kind' | 'name' | 'parentSpanId'>,
                fn: (t: StepTraceDraft) => Promise<T>): Promise<T> {
    const start = Date.now();
    const draft: StepTraceDraft = { tokens: { prompt: 0, completion: 0 }, retries: 0, attrs: {} };
    try {
      const out = await fn(draft);
      this.emit({ ...meta, status: 'ok', error: null, output: out }, draft, start);
      return out;
    } catch (e) {
      this.emit({ ...meta, status: /timeout/i.test((e as Error).name) ? 'timeout' : 'error', output: null,
                  error: { code: (e as Error).name, message: (e as Error).message } }, draft, start);
      throw e;
    }
  }

  private emit(meta: any, d: StepTraceDraft, start: number) {
    this.sink(StepTrace.parse({
      traceId: this.traceId, stepId: crypto.randomUUID(), startedAt: start, durationMs: Date.now() - start,
      inputDigest: d.inputDigest ?? '', outputDigest: d.outputDigest ?? '',
      inputPreview: d.inputPreview ?? '', outputPreview: d.outputPreview ?? '',
      ...meta, tokens: d.tokens, costUsd: d.costUsd ?? 0, retries: d.retries, attrs: d.attrs,
    }));
  }
}
type StepTraceDraft = { tokens: { prompt: number; completion: number }; retries: number; costUsd?: number;
  attrs: Record<string, unknown>; inputDigest?: string; outputDigest?: string; inputPreview?: string; outputPreview?: string; };
```
