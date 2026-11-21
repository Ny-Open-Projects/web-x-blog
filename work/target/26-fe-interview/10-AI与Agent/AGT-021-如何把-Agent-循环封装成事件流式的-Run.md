---
title: [AGT-021] 如何把 Agent 循环封装成事件流式的 Runtime，方便前端逐步渲染过程？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-021：如何把 Agent 循环封装成事件流式的 Runtime，方便前端逐步渲染过程？
**答**：
- 把 Agent 内部过程建模为事件：thought / tool_call / tool_result / answer / error。
- 用 `AsyncGenerator` 逐个 yield 事件，调用方 `for await` 消费，天然支持流式渲染到 UI。
- 事件流让"展示思考过程"成为可能，也是可观测性的数据源（见 AGT-040）。
- 工具执行复用 AGT-016 的 safeExecute，保证同样的安全护栏。

```typescript
// 最小 Agent Runtime：AsyncGenerator 事件流
type AgentEvent =
  | { type: 'tool_call'; name: string; args: unknown }
  | { type: 'tool_result'; name: string; result: unknown }
  | { type: 'answer'; content: string }
  | { type: 'error'; message: string };

async function* runRuntime(question: string): AsyncGenerator<AgentEvent> {
  const messages: any[] = [
    { role: 'system', content: '遇到需要计算或查询的问题先调用工具。' },
    { role: 'user', content: question },
  ];

  for (let step = 0; step < 10; step++) {
    let choice;
    try {
      choice = (await fetchCompletion({ messages, tools })).choices[0];
    } catch (err) {
      yield { type: 'error', message: String(err) };
      return;
    }

    if (choice.finish_reason !== 'tool_calls') {
      yield { type: 'answer', content: choice.message.content };
      return;
    }
    messages.push(choice.message);
    for (const call of choice.message.tool_calls) {
      yield { type: 'tool_call', name: call.function.name, args: JSON.parse(call.function.arguments) };
      const result = await safeExecute(call); // 复用 AGT-016 的安全执行器
      yield { type: 'tool_result', name: call.function.name, result };
      messages.push({ role: 'tool', tool_call_id: call.id, content: result });
    }
  }
  yield { type: 'error', message: '超出最大步数' };
}

// 消费端：逐事件推给 UI 渲染
for await (const event of runRuntime('北京今天适合跑步吗')) {
  renderEvent(event);
}
```

---

## 五、RAG 检索增强
