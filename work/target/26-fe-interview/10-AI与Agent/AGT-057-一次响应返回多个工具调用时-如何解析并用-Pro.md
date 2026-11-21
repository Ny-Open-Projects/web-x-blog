---
title: [AGT-057] 一次响应返回多个工具调用时，如何解析并用 Promise.all 并行执行？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-057：一次响应返回多个工具调用时，如何解析并用 Promise.all 并行执行？
**答**：
- 一次模型响应可携带多个 `tool_calls`（parallel tool calls）：必须全部解析、并行执行、以多条 tool 消息一次性回传，不能逐个串行来回（轮次与延迟翻倍）。
- 并行执行用 `Promise.allSettled`：单个工具失败不拖垮其他，失败也要作为结果回传（错误信息对模型同样有价值）。
- 有依赖的调用不能并行（先查 id 再查详情）：这应由模型分开轮次表达；执行器无需强猜依赖。
- 回传顺序不要求与请求一致，靠 `tool_call_id` 精确对齐。

```typescript
// 并行执行一轮全部 tool_calls，按 tool_call_id 回填
async function runParallelToolCalls(
  toolCalls: { id: string; function: { name: string; arguments: string } }[],
  registry: Map<string, (args: any) => Promise<string>>,
): Promise<ChatMessage[]> {
  const results = await Promise.allSettled(
    toolCalls.map(async (tc) => {
      const fn = registry.get(tc.function.name);
      if (!fn) throw new Error(`未知工具 ${tc.function.name}`);
      return withTimeout(fn(JSON.parse(tc.function.arguments || '{}')), 30_000);
    }),
  );
  // 关键：每条结果用对应 tool_call_id 对齐，且一次性全部回传
  return toolCalls.map((tc, i) => ({
    role: 'tool' as const,
    tool_call_id: tc.id,
    content: results[i].status === 'fulfilled'
      ? results[i].value
      : `工具执行失败：${String((results[i] as PromiseRejectedResult).reason)}`,
  }));
}

// 主循环接入
const assistantMsg = data.choices[0].message;            // 含多个 tool_calls
const toolResults = await runParallelToolCalls(assistantMsg.tool_calls ?? [], registry);
nextMessages.push(assistantMsg, ...toolResults);         // assistant + 全部 tool 消息一次追加
```
