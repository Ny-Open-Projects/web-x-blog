---
title: [AGT-177] Agent 应用市场有哪些商业模式？抽成与计费怎么设计？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-177：Agent 应用市场有哪些商业模式？抽成与计费怎么设计？
**答**：
- 四类商业角色：Agent 发布者（卖 Agent/技能包）、工具提供者（卖 MCP server/API 配额）、平台方（抽成 + 订阅）、用户（按用量或订阅付费）——前端面试重点在「计量与计费的工程实现」而非商业分析。
- 计费模型三选：按调用次数（简单但被滥用）、按 token 成本加价（透明但用户难预估）、按任务结果计费（价值定价，难在完成判定）。混合：基础订阅 + 超额按成本加价 20%~30%。
- 工程核心：计量流水（每次调用的 token/工具次数实时落账，幂等防重复计）、预扣与结算（任务开始预扣额度，失败按实际用量结算）、发布者分成对账（月账单 + 抽样审计）。
- 防薅羊毛：新账号限额、免费额度与设备/支付指纹绑定、异常用量风控（同用户高频同请求模式）。

```typescript
// Agent 市场计量计费：计量流水 + 预扣结算 + 分成
import { z } from 'zod';

const UsageRecord = z.object({
  userId: z.string(), agentId: z.string(), runId: z.string(),
  kind: z.enum(['llm_token', 'tool_call', 'agent_invoke']),
  quantity: z.number(), unitCostUsd: z.number(),
  idempotencyKey: z.string(),                              // 幂等：重试不重复计费
});
type UsageRecord = z.infer<typeof UsageRecord>;

export class MeteringService {
  private seen = new Set<string>();

  record(r: UsageRecord): boolean {
    if (this.seen.has(r.idempotencyKey)) return false;      // 幂等去重
    this.seen.add(r.idempotencyKey);
    const cost = r.quantity * r.unitCostUsd;
    ledger.append({ ...r, costUsd: cost, ts: Date.now() });
    quota.consume(r.userId, cost);                          // 预扣额度
    return true;
  }

  settleRun(runId: string, status: 'done' | 'failed') {
    const items = ledger.byRun(runId);
    const total = items.reduce((s, i) => s + i.costUsd, 0);
    if (status === 'failed') refund(items.filter((i) => i.kind !== 'llm_token')); // 失败：只收已消耗的模型成本
    const platformCut = total * 0.2, devShare = total * 0.8;                     // 平台抽成 20%
    payoutQueue.push({ runId, platformCut, devShare });
  }
}

// 免费额度风控：指纹绑定 + 异常用量检测
export function guardFreeTier(userId: string, fingerprint: string, todayCount: number) {
  if (fingerprintSeen(fingerprint) !== userId && todayCount > 0) return 'denied';  // 同指纹多账号
  if (todayCount > 50 && isHighFrequencyPattern(userId)) return 'captcha';          // 异常高频
  return 'allow';
}
const ledger = {
  append: (x: unknown) => { void x; },
  byRun: (id: string) => [] as { kind: string; costUsd: number }[],
};
const quota = { consume: (u: string, c: number) => { void u; void c; } };
const payoutQueue = { push: (x: unknown) => { void x; } };
function refund(items: unknown[]) { void items; }
function fingerprintSeen(f: string) { return 'user-a'; }
function isHighFrequencyPattern(u: string) { return false; }
```
