---
title: [AGT-122] MCP 传输层 stdio 与 Streamable HTTP 如何选型？各自的适用边界是什么？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-122：MCP 传输层 stdio 与 Streamable HTTP 如何选型？各自的适用边界是什么？
**答**：
- stdio：MCP server 作为宿主的子进程，通过标准输入输出通信——零网络开销、天然同机隔离、随宿主退出而退出，适合本地开发工具（文件系统、本地命令）。
- Streamable HTTP：server 是独立 HTTP 服务，支持多客户端共享、远程部署、鉴权（Bearer/OAuth），适合团队共享的内部服务与 SaaS 提供的 MCP 端点。
- 选型三问：数据在哪（本地 vs 远端）、谁来用（单用户 vs 多人）、生命周期（随宿主 vs 常驻服务）。
- 注意旧版 HTTP+SSE 传输已被 Streamable HTTP 取代：单端点同时承载 POST 请求与可选的 SSE 推送，通过 `Mcp-Session-Id` 维持会话。

```typescript
// 同一个 server 实例的两种传输接入：本地用 stdio，远端用 Streamable HTTP
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import express from 'express';

async function serveLocal(server: any) {
  // 本地模式：宿主 spawn 本进程，stdin/stdout 就是信道
  await server.connect(new StdioServerTransport());
}

function serveRemote(serverFactory: () => any, port: number) {
  const app = express();
  app.use(express.json());
  app.post('/mcp', async (req, res) => {
    // 有状态模式：每个会话一个 transport 实例，用 Session-Id 关联
    const sessionId = req.header('mcp-session-id');
    const transport = transports.get(sessionId) ?? new StreamableHTTPServerTransport({
      sessionIdGenerator: () => crypto.randomUUID(),
      enableJsonResponse: false, // false 表示用 SSE 流式返回
    });
    transports.set(transport.sessionId, transport);
    res.on('close', () => transport.sessionId && transports.delete(transport.sessionId));
    await serverFactory().connect(transport);
    await transport.handleRequest(req, res, req.body);
  });
  app.listen(port);
}
const transports = new Map<string, StreamableHTTPServerTransport>();

// 选型结论：文件/本机命令 → stdio；数据库/内部 API/团队共享 → Streamable HTTP + 鉴权
```
