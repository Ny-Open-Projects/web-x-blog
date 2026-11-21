---
title: [AGT-027] 什么是 MCP（Model Context Protocol）？它的架构和解决的问题是怎样的？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-027：什么是 MCP（Model Context Protocol）？它的架构和解决的问题是怎样的？
**答**：
- MCP 是 Anthropic 提出的开放协议，标准化"LLM 应用与外部工具/数据源"的连接方式，告别每家 Host 一套私有插件协议。
- 三种角色：Host（如 Claude Desktop、你的 Agent 应用）、Client（Host 内管理连接的组件）、Server（提供 tools / resources / prompts 的服务）。
- 传输层常见 stdio（本地子进程）与 Streamable HTTP（远程服务）；消息是 JSON-RPC 2.0。
- 价值在生态复用：一个 MCP server 写一次，任何支持 MCP 的 Host 都能接入；客户端配置形如注册一组子进程命令。

```json
{
  "mcpServers": {
    "weather": {
      "command": "node",
      "args": ["/path/to/mini-mcp-server.js"]
    },
    "remote-tools": {
      "url": "https://mcp.example.com/sse"
    }
  }
}
```
