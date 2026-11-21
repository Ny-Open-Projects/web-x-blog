---
title: [AGT-017] 模型一次返回多个 tool_calls（并行工具调用）时怎么处理？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-017：模型一次返回多个 tool_calls（并行工具调用）时怎么处理？
**答**：
- OpenAI 兼容接口支持单轮返回多个 tool_calls，互相独立的调用应并行执行，串行会成倍拉长延迟。
- 用 `Promise.allSettled` 而不是 `Promise.all`：单个工具失败不应拖垮整轮，失败信息也回填给模型让它自行调整。
- 回填时每个结果都要带各自的 `tool_call_id`，顺序与 tool_calls 一一对应。
- 有依赖关系的工具调用模型通常会分两轮请求，不需要你在客户端做 DAG。

```typescript
// 并行执行全部 tool_calls，全部完成后按原顺序回填
interface ToolCall {
  id: string;
  function: { name: string; arguments: string };
}

async function runParallelToolCalls(
  toolCalls: ToolCall[],
): Promise<Array<{ role: 'tool'; tool_call_id: string; content: string }>> {
  const results = await Promise.allSettled(toolCalls.map((c) => safeExecute(c)));

  return toolCalls.map((call, i) => {
    const r = results[i];
    return {
      role: 'tool' as const,
      tool_call_id: call.id,
      content: r.status === 'fulfilled' ? r.value : JSON.stringify({ error: String(r.reason) }),
    };
  });
}
```

---
## 四、Agent 核心架构
