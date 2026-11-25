---
title: [AGT-060] 工具调用的可观测性如何做？trace 每次调用要记录什么？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-060：工具调用的可观测性如何做？trace 每次调用要记录什么？
**答**：
- Agent 一次任务可能调几十次工具，出问题必须能回答「哪一步、什么参数、耗时多少、返回了什么」。
- 统一在执行器包一层 span：toolName、脱敏后的 args、duration、resultLen、status、parentSpanId，输出结构化日志并上报 tracing 系统。
- trace 与会话关联：一次用户请求一个 traceId，工具 span、LLM span 都挂在下面，能还原完整决策链。
- 大结果只记 hash 与长度，日志不落敏感数据（复用 AGT-099 脱敏管道）。

```typescript
// 工具执行 trace 包装器
async function tracedToolRun(
  name: string,
  args: unknown,
  run: () => Promise<string>,
  ctx: { traceId: string; parentSpan: string },
) {
  const spanId = crypto.randomUUID();
  const start = performance.now();
  const base = { traceId: ctx.traceId, parentSpanId: ctx.parentSpan, spanId, tool: name };
  try {
    const result = await run();
    log.info(JSON.stringify({
      ...base, status: 'ok', ms: Math.round(performance.now() - start),
      argPreview: JSON.stringify(args).slice(0, 200),   // 脱敏 + 截断
      resultLen: result.length, resultHash: stableHash(result),
    }));
    return result;
  } catch (e) {
    log.error(JSON.stringify({ ...base, status: 'error', ms: Math.round(performance.now() - start), error: String(e) }));
    throw e;
  }
}

// 所有工具统一走这里，天然获得全链路 trace
const ctx = { traceId: currentTraceId, parentSpan: 'agent-loop' };
const registry = new Map<string, (a: any) => Promise<string>>([
  ['search_docs',   (a) => tracedToolRun('search_docs', a, () => searchDocs(a), ctx)],
  ['create_ticket', (a) => tracedToolRun('create_ticket', a, () => createTicket(a), ctx)],
]);
```
