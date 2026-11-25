---
title: [AGT-019] Agent 的终止条件有哪些？为什么要做最大步数与成本保护？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-019：Agent 的终止条件有哪些？为什么要做最大步数与成本保护？
**答**：
- 正常终止：模型给出最终回答（`finish_reason === 'stop'`）。
- 异常终止必须多元：最大步数、token/金额预算、外部中断（用户点击停止）、单步超时。
- 模型可能陷入"调工具-失败-再调"死循环，没有护栏就是烧钱无底洞。
- 终止要返回结构化结果（stopReason），让上层能区分"答完了"和"被迫停"，分别渲染不同的 UI。

```typescript
// 多重终止护栏的 Agent 运行器
type StopReason = 'final_answer' | 'max_steps' | 'budget_exceeded' | 'aborted';

interface AgentResult {
  answer: string;
  stopReason: StopReason;
  steps: number;
  totalTokens: number;
}

async function runAgentWithGuards(
  question: string,
  opts = { maxSteps: 10, maxTokens: 100_000, signal: new AbortController().signal },
): Promise<AgentResult> {
  let steps = 0;
  let totalTokens = 0;
  const messages: any[] = [{ role: 'user', content: question }];

  while (true) {
    if (opts.signal.aborted) {
      return { answer: '已中断', stopReason: 'aborted', steps, totalTokens };
    }
    if (steps >= opts.maxSteps) {
      return { answer: '任务过于复杂，已停止执行', stopReason: 'max_steps', steps, totalTokens };
    }
    if (totalTokens >= opts.maxTokens) {
      return { answer: 'token 预算耗尽', stopReason: 'budget_exceeded', steps, totalTokens };
    }

    const res = await fetchCompletion({ messages, tools });
    totalTokens += res.usage.total_tokens;
    steps++;

    const { message, finish_reason } = res.choices[0];
    if (finish_reason === 'stop') {
      return { answer: message.content, stopReason: 'final_answer', steps, totalTokens };
    }
    messages.push(message);
    messages.push(...(await runParallelToolCalls(message.tool_calls)));
  }
}
```
