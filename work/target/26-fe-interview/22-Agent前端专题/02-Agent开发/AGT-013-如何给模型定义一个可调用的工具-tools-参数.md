---
title: [AGT-013] 如何给模型定义一个可调用的工具（tools 参数）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-013：如何给模型定义一个可调用的工具（tools 参数）？
**答**：
- 请求体传 `tools` 数组，每项是 `type: 'function'` + JSON Schema 描述的参数结构。
- `description` 是模型决定"调不调、怎么调"的唯一依据，必须写清楚用途、何时调用、参数含义。
- 参数用 `enum`、`required` 收紧，越确定的 schema 模型生成的参数越准。
- 模型不会真的执行工具，它只返回"想调用"的意图，执行永远在你的代码里（见 AGT-014）。

```typescript
// 工具定义：description 决定调用准确率，JSON Schema 约束参数
const tools = [
  {
    type: 'function',
    function: {
      name: 'get_weather',
      description: '查询指定城市当前天气，当用户询问天气相关问题时调用',
      parameters: {
        type: 'object',
        properties: {
          city: { type: 'string', description: '城市名，如 北京' },
          unit: {
            type: 'string',
            enum: ['celsius', 'fahrenheit'],
            description: '温度单位，默认 celsius',
          },
        },
        required: ['city'],
      },
    },
  },
] as const;

async function runWithTools(messages: ChatMessage[]) {
  const res = await fetch(`${OPENAI_BASE_URL}/chat/completions`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
    },
    body: JSON.stringify({ model: 'gpt-4o-mini', messages, tools }),
  });
  const data = await res.json();
  // finish_reason 为 tool_calls 表示模型请求调工具
  return data.choices[0];
}
```
