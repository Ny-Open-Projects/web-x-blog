---
title: [AGT-158] 多 Agent 协作中，下游如何校验上游输出的可信度？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-158：多 Agent 协作中，下游如何校验上游输出的可信度？
**答**：
- 零信任原则：上游 Agent 的输出一律当不可信输入——包括结构（schema 校验）、事实（可复核项抽查）、完整性（验收标准逐条核对）三层。
- 校验成本分层：结构性校验（JSON schema、类型）每次必做且便宜；事实性校验按风险抽样（关键决策全查，背景信息抽 20%）；高风险产出（涉及资金/删除）强制复核后才能执行。
- 信任评分动态化：为每个上游 Agent 维护历史通过率，评分低的自动升级校验强度（抽查率 100%），评分高的维持轻量校验——把信任做成可观测的滑块。
- 校验失败的处理要有出口：单次打回上游修订，连续失败熔断改走人工，避免两 Agent 互相修补的死循环。

```typescript
// 下游校验层：结构 → 事实抽查 → 动态信任评分
import { z } from 'zod';

export class TrustGate {
  private passCount = new Map<string, { pass: number; total: number }>();

  private trustScore(upstreamId: string): number {
    const s = this.passCount.get(upstreamId);
    return !s || s.total < 5 ? 0.5 : s.pass / s.total;          // 冷启动按 0.5
  }

  async accept(upstreamId: string, output: unknown, schema: z.ZodTypeAny,
               factCheck: (o: unknown) => Promise<{ ok: boolean; detail: string }>): Promise<unknown> {
    const parsed = schema.safeParse(output);                    // L1 结构校验：必做
    if (!parsed.success) throw new RejectError(upstreamId, 'schema', parsed.error.message);

    const score = this.trustScore(upstreamId);
    const sampleRate = score >= 0.9 ? 0.2 : score >= 0.7 ? 0.5 : 1.0;  // 信任越低查得越狠
    if (Math.random() < sampleRate) {                           // L2 事实抽查：按风险抽样
      const fc = await factCheck(parsed.data);
      if (!fc.ok) { this.bump(upstreamId, false); throw new RejectError(upstreamId, 'fact', fc.detail); }
    }
    this.bump(upstreamId, true);
    return parsed.data;
  }

  private bump(id: string, pass: boolean) {
    const s = this.passCount.get(id) ?? { pass: 0, total: 0 };
    s.total++; if (pass) s.pass++;
    this.passCount.set(id, s);
  }
}

export class RejectError extends Error {
  constructor(public upstreamId: string, public stage: 'schema' | 'fact', detail: string) {
    super(`上游 ${upstreamId} 输出被拒（${stage}）：${detail}`);
  }
}
```
