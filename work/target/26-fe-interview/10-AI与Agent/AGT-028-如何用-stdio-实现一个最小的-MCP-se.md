---
title: [AGT-028] 如何用 stdio 实现一个最小的 MCP server（tools/list 与 tools/call）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 笔试题, 14]
type: 笔试题
---

## AGT-028：如何用 stdio 实现一个最小的 MCP server（tools/list 与 tools/call）？
**答**：
- MCP 消息是 JSON-RPC 2.0，按行读写 stdin/stdout，天然适合子进程方式启动。
- 必须实现的方法：`initialize`（握手，声明能力与协议版本）、`tools/list`（工具清单 + inputSchema）、`tools/call`（执行并返回 `content` 数组）。
- 最小实现不需要官方 SDK，一个 readline 循环即可；生产建议用 `@modelcontextprotocol/sdk` 处理协议细节。
- 验证方式：往 stdin 喂一条 `tools/list` 消息看 stdout 回包。

```javascript
// 最小 MCP server：stdio 上的 JSON-RPC 2.0，无 SDK 依赖
const readline = require('node:readline');

const TOOLS = [
  {
    name: 'add',
    description: '计算两个数之和',
    inputSchema: {
      type: 'object',
      properties: { a: { type: 'number' }, b: { type: 'number' } },
      required: ['a', 'b'],
    },
  },
];

function handleInitialize(id) {
  return {
    jsonrpc: '2.0',
    id,
    result: {
      protocolVersion: '2024-11-05',
      capabilities: { tools: {} },
      serverInfo: { name: 'mini-mcp-server', version: '0.1.0' },
    },
  };
}

function handleToolCall(id, params) {
  if (params.name !== 'add') {
    return { jsonrpc: '2.0', id, error: { code: -32601, message: `未知工具 ${params.name}` } };
  }
  const { a, b } = params.arguments;
  return {
    jsonrpc: '2.0',
    id,
    result: { content: [{ type: 'text', text: String(a + b) }] },
  };
}

const rl = readline.createInterface({ input: process.stdin });
rl.on('line', (line) => {
  if (!line.trim()) return;
  const msg = JSON.parse(line);
  let response = null;
  if (msg.method === 'initialize') response = handleInitialize(msg.id);
  else if (msg.method === 'tools/list') response = { jsonrpc: '2.0', id: msg.id, result: { tools: TOOLS } };
  else if (msg.method === 'tools/call') response = handleToolCall(msg.id, msg.params);
  else if (msg.id !== undefined) response = { jsonrpc: '2.0', id: msg.id, error: { code: -32601, message: '方法不存在' } };
  if (response) process.stdout.write(`${JSON.stringify(response)}\n`);
});
```

```bash
# 启动并验证 tools/list：向 stdin 喂一条 JSON-RPC 消息，观察 stdout 回包
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | node mini-mcp-server.js
```
