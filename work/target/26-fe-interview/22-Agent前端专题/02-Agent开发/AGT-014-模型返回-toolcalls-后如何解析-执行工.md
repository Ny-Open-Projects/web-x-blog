---
title: [AGT-014] 模型返回 tool_calls 后如何解析、执行工具并回填结果？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-014：模型返回 tool_calls 后如何解析、执行工具并回填结果？
**答**：
- 检查 `finish_reason === 'tool_calls'`，从 `message.tool_calls` 取出工具名和 `arguments`（是 JSON 字符串，要 parse）。
- 执行本地工具后，把结果以 `role: 'tool'`、带 `tool_call_id` 的消息追加进 messages 再请求一次。
- assistant 的 tool_calls 消息本体也必须原样回传，否则服务端校验会报错。
- `tool_call_id` 与结果一一对应，多工具场景绝不能错位。

```typescript
// 解析 tool_calls → 执行 → role 为 tool 的消息回填 → 二次请求
const registry: Record<string, (args: any) => Promise<unknown>> = {
  get_weather: async ({ city }: { city: string }) => ({ city, temp: 26, condition: '晴' }),
};

async function handleToolCall(userMessage: string): Promise<string> {
  const messages: any[] = [{ role: 'user', content: userMessage }];
  const first = await fetchCompletion({ messages, tools });
  const msg = first.choices[0].message;

  if (first.choices[0].finish_reason !== 'tool_calls') return msg.content;

  messages.push(msg); // assistant 的 tool_calls 消息必须原样回传
  for (const call of msg.tool_calls) {
    const fn = registry[call.function.name];
    const result = await fn(JSON.parse(call.function.arguments));
    messages.push({
      role: 'tool',
      tool_call_id: call.id, // 与 tool_call 一一对应
      content: JSON.stringify(result),
    });
  }
  const second = await fetchCompletion({ messages, tools });
  return second.choices[0].message.content;
}
```
