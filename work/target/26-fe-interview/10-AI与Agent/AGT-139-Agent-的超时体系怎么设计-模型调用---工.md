---
title: [AGT-139] Agent 的超时体系怎么设计（模型调用 / 工具执行 / 整体任务的超时树）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-139：Agent 的超时体系怎么设计（模型调用 / 工具执行 / 整体任务的超时树）？
**答**：
- 超时要建成「树」：整体任务 > 单步（模型调用或工具）> 底层 IO（HTTP 连接/读超时），父级预算必须大于子级之和的可能值，否则父级先炸导致子级结果作废。
- 三层各司其职：底层 IO 超时防挂死连接；单步超时触发换路（重试/换模型/换工具）；整体预算超时把「部分产出」返回给用户而不是全部丢弃。
- 关键机制：AbortController 层层传递——用户取消或父级超时要能真正中断进行中的子调用，而不是只放弃等待（放弃等待但子任务继续跑会浪费成本）。
- 所有超时都要打点区分「慢在哪层」，否则线上只能看到「任务超时」一个模糊信号。

```typescript
// 超时树：整体 > 单步 > IO，AbortSignal 层层传递
export function withTimeout<T>(p: (signal: AbortSignal) => Promise<T>, ms: number, parent?: AbortSignal): Promise<T> {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(new DOMException('timeout', 'TimeoutError')), ms);
  const onParentAbort = () => ctrl.abort(parent!.reason);
  parent?.addEventListener('abort', onParentAbort, { once: true });
  return p(ctrl.signal).finally(() => {
    clearTimeout(timer);
    parent?.removeEventListener('abort', onParentAbort);
  });
}

export class TimeoutBudget {
  constructor(public totalMs: number, private deadline = Date.now() + 0) { this.deadline = Date.now() + totalMs; }

  // 分配给某一步的超时：剩余预算的份额，且不超过该步的单步上限
  slice(singleStepCap: number, share = 0.4): number {
    const remain = this.deadline - Date.now();
    if (remain <= 500) throw new DOMException('整体预算耗尽', 'TimeoutError'); // 保留 500ms 收尾
    return Math.min(singleStepCap, Math.floor(remain * share));
  }
}

export async function agentRun(task: () => Promise<string>, plan: ((sig: AbortSignal, b: TimeoutBudget) => Promise<unknown>)[], signal: AbortSignal) {
  const budget = new TimeoutBudget(120_000);
  // L3：整体任务超时，超时后带部分产出返回
  const results: unknown[] = [];
  try {
    for (const step of plan) {
      const ms = budget.slice(30_000);          // L2：单步上限 30s
      results.push(await withTimeout((sig) => step(sig, budget), ms, signal)); // L1：IO 超时由步骤内部再切
    }
    return { status: 'done' as const, results };
  } catch (e) {
    return { status: 'partial' as const, results, reason: (e as Error).message }; // 部分产出不丢弃
  }
}
```
