---
title: [AGT-161] 跨 Agent 的分布式 trace 怎么串联与排查？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-161：跨 Agent 的分布式 trace 怎么串联与排查？
**答**：
- 串联机制：入口生成 traceId 后随任务单透传，每个 Agent 无论跨进程还是跨机，收到任务先取出 traceId，自己所有调用都携带，回传结果也带回——traceId 是任务单的必填字段。
- 层级结构：traceId（整条链）→ runId（某 Agent 内的一次运行）→ stepId（单次调用），父子用 span 引用；跨 Agent 的「委托」关系单独记 `delegatedFrom`。
- 排查三板斧：按 traceId 重建完整时间线（谁在什么时候调了什么、花了多少）、按耗时找瓶颈 span（通常发现 80% 时间在等某个慢工具）、按错误码聚合找共性根因。
- 前端联动：把 traceId 暴露到 UI（错误卡片「复制 traceId」），用户报障时一条命令拉出全链，支持效率天差地别。

```typescript
// 跨 Agent trace 上下文透传与时间线重建
import { AsyncLocalStorage } from 'async_hooks';
import { z } from 'zod';

const TraceCtx = z.object({ traceId: z.string(), parentSpanId: z.string().nullable(), delegatedFrom: z.string().optional() });
type TraceCtx = z.infer<typeof TraceCtx>;
const als = new AsyncLocalStorage<TraceCtx>();

export function withTrace<T>(ctx: TraceCtx, fn: () => Promise<T>): Promise<T> {
  return als.run(ctx, fn);
}
export function currentTrace(): TraceCtx {
  const c = als.getStore();
  if (!c) throw new Error('trace 上下文缺失：任务单必须携带 traceId');
  return c;
}

// Agent 收到任务单：透传 traceId，自己的 run 记为子 run
export async function handleDelegatedTask(ticket: { traceId?: string; from?: string; payload: unknown }) {
  const ctx = TraceCtx.parse({ traceId: ticket.traceId ?? crypto.randomUUID(), parentSpanId: null, delegatedFrom: ticket.from });
  return withTrace(ctx, async () => {
    const runId = crypto.randomUUID();
    trace.emit({ runId, kind: 'run', name: 'delegated-task', ...currentTrace() });
    const result = await doWork(runId);
    return { result, traceId: ctx.traceId };          // 结果回传也带 traceId
  });
}

// 时间线重建：按 traceId 聚合所有 Agent 的 span，输出排查视图
export async function rebuildTimeline(traceId: string) {
  const spans = await traceStore.query({ traceId });  // 跨 Agent 落在同一个 trace 存储
  return spans
    .sort((a, b) => a.startedAt - b.startedAt)
    .map((s) => `${new Date(s.startedAt).toISOString()} [${s.agent ?? '-'}] ${s.kind}:${s.name} ${s.durationMs}ms $${s.costUsd} ${s.status}`);
}
async function doWork(runId: string) { void runId; return 'ok'; }
const trace = { emit: (x: unknown) => { void x; } };
const traceStore = { query: async (_q: unknown) => [] as any[] };
```

---

## 二十八、领域 Agent 设计模式
