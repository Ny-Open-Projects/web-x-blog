---
title: [AGT-029] MCP 与 Function Calling 是什么关系？如何把 MCP 工具桥接给只用 Function Calling 的模型？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-029：MCP 与 Function Calling 是什么关系？如何把 MCP 工具桥接给只用 Function Calling 的模型？
**答**：
- 二者不在同一层：Function Calling 是模型侧的"意图表达"机制；MCP 是应用侧的"工具发现、传输与执行"协议。
- MCP 不取代 FC，而是给 FC 供货：Host 通过 MCP 拿到工具清单，转成 FC 的 tools 参数喂给模型；模型发出 tool_call 后，再经 MCP client 转发执行。
- 好处是解耦：模型与工具实现互相不感知，加一个 MCP server 不用改业务代码。
- 桥接核心是字段映射：MCP 的 `inputSchema` 直接充当 OpenAI tools 的 `parameters`，返回的 `content` 序列化后回填 `role: 'tool'` 消息。

```typescript
// MCP 工具描述 → OpenAI tools 参数的桥接层
interface McpTool {
  name: string;
  description: string;
  inputSchema: Record<string, unknown>;
}

interface McpClient {
  listTools(): Promise<McpTool[]>;
  callTool(name: string, args: unknown): Promise<{ content: Array<{ type: string; text: string }> }>;
}

// 1. 工具发现：MCP tools/list 的结果转成 FC 的 tools 定义
function mcpToolsToOpenAI(mcpTools: McpTool[]) {
  return mcpTools.map((t) => ({
    type: 'function',
    function: {
      name: t.name,
      description: t.description,
      parameters: t.inputSchema, // MCP 的 inputSchema 就是 JSON Schema，直接复用
    },
  }));
}

// 2. 工具执行：模型的 tool_call 经 MCP client 转发给对应 server
async function dispatchToolCall(
  mcpClient: McpClient,
  call: { name: string; arguments: string },
): Promise<string> {
  const result = await mcpClient.callTool(call.name, JSON.parse(call.arguments));
  return JSON.stringify(result.content); // 回填进 role 为 tool 的消息
}
```

---
## 七、前端集成
