---
title: [AGT-059] MCP 工具如何动态发现与热更新？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-059：MCP 工具如何动态发现与热更新？
**答**：
- MCP 的 `tools/list` 是动态的：server 升级后工具集可能变化，客户端不能启动时拉一次就缓存到永远。
- 双通道更新：启动全量拉取 + 监听 `notifications/tools/list_changed` 通知后增量重拉；配置文件 watch 变更后重连对应 server。
- 工具集变化要同步到 LLM 侧：tools 参数实时重新生成；进行中会话引用旧工具名要做兼容映射或明确报错。
- 变更必须留审计：谁在什么时间增删改了哪些工具，防止「悄悄多了个高危工具」。

```typescript
// MCP 客户端：动态发现 + list_changed 热更新
interface McpTool { server: McpServerConn; def: { name: string; description: string; inputSchema: unknown } }

class McpToolHub {
  private tools = new Map<string, McpTool>();

  async refresh(server: McpServerConn) {
    const { tools } = await server.listTools();
    const names = new Set(tools.map((t) => t.name));
    for (const [name, t] of this.tools) {
      if (t.server === server && !names.has(name)) this.tools.delete(name); // 删除已下线工具
    }
    for (const t of tools) {
      const old = this.tools.get(t.name);
      if (!old || JSON.stringify(old.def) !== JSON.stringify(t)) {
        this.tools.set(t.name, { server, def: t });                          // 增量更新
        log.info({ event: 'mcp_tool_changed', tool: t.name, server: server.name });
      }
    }
  }

  async start() {
    await Promise.all(this.servers.map((s) => this.refresh(s)));
    for (const s of this.servers) {
      s.onNotification('notifications/tools/list_changed', () => this.refresh(s)); // 热更新通知
    }
  }

  // 提供给 LLM 的工具列表实时取自 hub，而非启动时快照
  toOpenAITools() {
    return [...this.tools.values()].map(({ def }) => toOpenAISchema(def));
  }
}
```
