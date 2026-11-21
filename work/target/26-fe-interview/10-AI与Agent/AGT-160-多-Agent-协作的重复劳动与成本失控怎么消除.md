---
title: [AGT-160] 多 Agent 协作的重复劳动与成本失控怎么消除？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-160：多 Agent 协作的重复劳动与成本失控怎么消除？
**答**：
- 重复劳动三大来源：多个 Agent 独立检索同一份资料、相似子任务重复规划、失败重试导致同一 LLM 调用重发——分别用「共享工作区缓存」「计划去重」「调用级 memo」消除。
- 调用级 memo：以「prompt 模板版本 + 输入哈希 + 工具集版本」为 key 缓存 LLM 响应，temperature > 0 时也可对确定性子任务（分类/抽取）启用。
- 任务级去重：分派前查「进行中任务登记表」（按 goal 哈希），同 goal 已在跑则挂接等待而不是再派一个——fan-out 场景尤其重要。
- 预算硬约束：每 agent、每 run、每租户三级预算，超限即拒绝派发；老板 Agent 的分派也要过预算检查，防止「审批别人的人自己失控」。

```typescript
// 多 Agent 成本治理：调用 memo + 任务去重 + 三级预算
import { createHash } from 'crypto';

const memo = new Map<string, string>();
function llmKey(model: string, promptVersion: string, input: string) {
  return createHash('sha256').update(`${model}|${promptVersion}|${input}`).digest('hex');
}
export async function memoLlm(model: string, promptVersion: string, input: string): Promise<string> {
  const key = llmKey(model, promptVersion, input);
  const hit = memo.get(key);
  if (hit) { metrics.inc('llm.memo.hit'); return hit; }
  const out = await rawLlm(model, input);
  memo.set(key, out);
  return out;
}

const inflight = new Map<string, Promise<unknown>>();
export async function dispatchDedup(goal: string, run: () => Promise<unknown>): Promise<unknown> {
  const goalKey = createHash('sha256').update(goal).digest('hex');
  const existing = inflight.get(goalKey);
  if (existing) { metrics.inc('agent.dedup.join'); return existing; }   // 同目标挂接等待
  const p = run().finally(() => inflight.delete(goalKey));
  inflight.set(goalKey, p);
  return p;
}

// 三级预算闸门
const BUDGET = { agent: 2, run: 10, tenant: 100 };
export function assertBudget(spent: Record<string, number>, who: { agent: string; run: string; tenant: string }) {
  const levels: [string, number, number][] = [
    [spent[who.agent] ?? 0, BUDGET.agent, who.agent],
    [spent[who.run] ?? 0, BUDGET.run, who.run],
    [spent[who.tenant] ?? 0, BUDGET.tenant, who.tenant],
  ];
  for (const [used, cap, id] of levels) {
    if (used >= cap) throw new Error(`预算耗尽：${id} 已花费 $${used.toFixed(2)} / 上限 $${cap}`);
  }
}
async function rawLlm(m: string, i: string) { void m; void i; return ''; }
const metrics = { inc: (n: string) => { void n; } };
```
