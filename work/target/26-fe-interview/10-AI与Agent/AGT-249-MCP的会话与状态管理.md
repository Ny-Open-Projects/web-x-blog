---
title: [AGT-249] MCP 的会话管理——有状态 Server 与重连续传怎么做？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-249：远程 MCP Server 的会话状态与断线重连怎么处理？

**答**:
- 会话生命周期：Streamable HTTP 传输下 Client initialize 时获得 session id，后续请求携带——Server 用会话维护状态（分页游标/长任务进度/订阅关系）；会话有 TTL，过期需重新 initialize。
- 无状态优先：能放 Client 的状态（对话历史）不要放 Server——Server 只保存"必要的服务端状态"（长任务/订阅），无状态 Server 才好水平扩展。
- 断线重连：流式响应中断后 Client 带 Last-Event-ID 重连续传（SSE 语义）；长任务用任务 id 轮询/订阅进度而非依赖单连接不中断——把"连接"当可随时断的资源设计。
- 多实例部署：有状态会话要么粘性路由（session→固定实例），要么状态外置（Redis）共享——粘性简单但故障恢复差，外置是生产首选。

```javascript
// Server：会话 + 可恢复流
app.get('/mcp', async (req, res) => {
  const session = await sessions.get(req.get('mcp-session-id'))
                 ?? await sessions.create();
  const lastId = req.get('last-event-id');  // 断点续传
  const stream = events.replay(session.id, lastId);
  stream.pipe(res);                          // SSE
});
// Client：重连退避 + 会话过期重新 initialize
// 长任务：taskId 轮询进度，不依赖长连接
```
